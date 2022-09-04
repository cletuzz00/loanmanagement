from datetime import datetime
from rest_framework import serializers
from loans.models import Loan, Clients, InterestRate
from users.models import User

class LoanSerializer(serializers.ModelSerializer):
    repayment_date = serializers.DateField(format="%Y-%m-%d",required=True)
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ('total_amount', 'interest')

    
    def create(self, validated_data):
        if validated_data['repayment_date'] < datetime.now().date():
            raise serializers.ValidationError("Repayment date cannot be in the past")
        if Clients.objects.filter(id=validated_data['client'].id) == None:
            raise serializers.ValidationError("Client does not exist")
        interest = InterestRate.objects.get(is_active=True)
        if interest:
            # calculate days between current date and incoming date
            days = (validated_data['repayment_date'] - datetime.now().date()).days
            total_amount = validated_data['amount'] + (validated_data['amount'] * interest.rate * days)
            validated_data['total_amount'] = total_amount
            validated_data['interest'] = interest.rate
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("Interest rate not set")

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

    def create(self, validated_data):
        if Clients.objects.filter(id_number=validated_data['id_number']):
            raise serializers.ValidationError("Client already exists")
        # save client and create user account
        client = Clients.objects.create(**validated_data)
        try:
            User.create_client(client.first_name,client.last_name,client.email,client.phone_number,client.id_number)
            print('account created')
        except:
            raise serializers.ValidationError("Error creating user account")
        return client

class InterestRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestRate
        fields = '__all__'
    
    def create(self, validated_data):
        # limit to only one interest rate
        if InterestRate.objects.all().count() > 0:
            raise serializers.ValidationError("Interest rate already exists")
        return super().create(validated_data)