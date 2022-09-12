# send email function
from django.core.mail.message import EmailMessage, BadHeaderError
from decouple import config

"""
    EMAIL HANDLER
"""


class Emails:
    def __init__(
        self,
        message,
        email_address,
    ):
        self.message = message
        self.email_address = email_address
        self.from_email = config("EMAIL_HOST_USER")

    def send(self, message, recipient):
        try:
            email = EmailMessage(
                to=self.email_address,
                from_email=self.from_email,
                subject="Loan Application",
                body=message,
            )
            email.send()
            return True
        except BadHeaderError:
            return False
