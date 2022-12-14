# Generated by Django 3.2.12 on 2022-09-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_loan_repayment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date_approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='date_requested',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
