from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import status, generics
from loans.models import Loan, Clients, InterestRate
from api.serializers.loans import LoanSerializer, ClientSerializer, InterestRateSerializer
from rest_framework.decorators import action
import datetime
from loans.helper_function import Emails

class LoanViewset(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    @action(methods=['get'],detail=False,url_path='client')
    def client(self, request):
        # search client by name or id number
        client = request.query_params.get('client', None)
        if client:
            queryset = Loan.objects.filter(client=client)
        else:
            queryset = Loan.objects.all()
        serializer = LoanSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['get'],detail=False,url_path='notifications')
    def notifications(self, request):
        # notify all clients with loans that are due
        queryset = Loan.objects.filter(is_active=True, is_paid=False, is_defaulted=False)
        for loan in queryset:
            if loan.repayment_date < datetime.datetime.now().date():
                loan.is_overdue = True if loan.is_overdue == False else loan.is_overdue
                loan.save()
        # send email to clients with overdue loans
        for loan in queryset:
            if loan.is_overdue:
                print(f"send email to {loan.client.email}")
                # send email
                Emails.send(f"Loan is Due , your repayment date is {loan.repayment_date}",loan.client.email)
        return JsonResponse(status=status.HTTP_200_OK,data={'message':'notifications sent'}, safe=False)
        


class ClientViewset(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    @action(methods=['get'], detail=False, url_path='search')
    def search(self, request):
        # search client by name or id number
        name = request.query_params.get('first_name', None)
        lname = request.query_params.get('last_name', None)
        id_number = request.query_params.get('id_number', None)
        if name:
            queryset = Clients.objects.filter(first_name__icontains=name)
        elif lname:
            queryset = Clients.objects.filter(last_name__icontains=lname)
        elif id_number:
            queryset = Clients.objects.filter(id_number=id_number)
        else:
            queryset = Clients.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
        


class InterestRateViewset(viewsets.ModelViewSet):
    queryset = InterestRate.objects.all()
    serializer_class = InterestRateSerializer

