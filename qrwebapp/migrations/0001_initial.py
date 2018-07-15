# Generated by Django 2.0.7 on 2018-07-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Passanger Details',
                'verbose_name': 'Passanger Detail',
            },
        ),
        migrations.CreateModel(
            name='RazorpayPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Razorpay Order Id')),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Razorpay Payment Id')),
                ('razorpay_signature', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Razorpay Signature')),
                ('entity', models.CharField(blank=True, max_length=64, null=True, verbose_name='Entity')),
                ('currency', models.CharField(blank=True, max_length=3, null=True, verbose_name='Currency')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Amount')),
                ('payment_status', models.CharField(blank=True, max_length=64, null=True, verbose_name='Payment Status')),
                ('method', models.CharField(blank=True, max_length=64, null=True, verbose_name='Mode of Payment')),
                ('captured', models.BooleanField(verbose_name='Captured')),
                ('card_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Card ID')),
                ('bank', models.CharField(blank=True, max_length=64, null=True, verbose_name='Bank (Code)')),
                ('wallet', models.CharField(blank=True, max_length=64, null=True, verbose_name='Wallet')),
                ('vpa', models.CharField(blank=True, max_length=64, null=True, verbose_name='vpa')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='Email')),
                ('contact', models.CharField(blank=True, max_length=64, null=True, verbose_name='Contact')),
                ('fee', models.CharField(blank=True, max_length=64, null=True, verbose_name='Fee')),
                ('error_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Error code')),
                ('error_description', models.CharField(blank=True, max_length=128, null=True, verbose_name='Error Description')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Ticket → Payments',
                'verbose_name': 'Ticket → Payment',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=32, verbose_name='Starting Point')),
                ('destination', models.CharField(max_length=32, verbose_name='Ending Point')),
                ('fare', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Journey Fare')),
            ],
            options={
                'verbose_name_plural': 'Routes',
                'verbose_name': 'Route',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=32, verbose_name='Starting Point')),
                ('destination', models.CharField(max_length=32, verbose_name='Ending Point')),
                ('fare', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Journey Fare')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Ticket Time')),
                ('passanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrwebapp.Passenger')),
            ],
        ),
        migrations.AddField(
            model_name='razorpaypayment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrwebapp.Ticket'),
        ),
    ]