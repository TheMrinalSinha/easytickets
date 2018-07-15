from django.db import models

class Passenger(models.Model):
    name  = models.CharField('Name', max_length=64)
    phone = models.CharField('Phone', max_length=10)
    email = models.EmailField('Email', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Passanger Detail'
        verbose_name_plural = 'Passanger Details'

class Ticket(models.Model):
    passanger = models.ForeignKey(Passenger)

class RazorpayPayment(models.Model):
    ticket              = models.ForeignKey(Ticket)
    razorpay_order_id   = models.CharField('Razorpay Order Id',   max_length=128, null=True, blank=True)
    razorpay_payment_id = models.CharField('Razorpay Payment Id', max_length=128, null=True, blank=True)
    razorpay_signature  = models.CharField('Razorpay Signature',  max_length=2048,null=True, blank=True)
    entity              = models.CharField('Entity',          max_length=64,  null=True, blank=True)
    currency            = models.CharField('Currency',        max_length=3,   null=True, blank=True)
    amount              = models.DecimalField('Amount',       max_digits=5,  decimal_places=2, null=True, blank=True)
    payment_status      = models.CharField('Payment Status',  max_length=64,  null=True, blank=True)
    method              = models.CharField('Mode of Payment', max_length=64,  null=True, blank=True)
    captured            = models.BooleanField('Captured')
    card_id             = models.CharField('Card ID',     max_length=128, null=True, blank=True)
    bank                = models.CharField('Bank (Code)', max_length=64,  null=True, blank=True)
    wallet              = models.CharField('Wallet',      max_length=64,  null=True, blank=True)
    vpa                 = models.CharField('vpa',         max_length=64,  null=True, blank=True)
    email               = models.CharField('Email',       max_length=128, null=True, blank=True)
    contact             = models.CharField('Contact',     max_length=64,  null=True, blank=True)
    fee                 = models.CharField('Fee',         max_length=64,  null=True, blank=True)
    error_code          = models.CharField('Error code',  max_length=64,  null=True, blank=True)
    error_description   = models.CharField('Error Description', max_length=128, null=True, blank=True)
    created_at          = models.DateTimeField('Created at',    null=True, blank=True)

    class Meta:
        verbose_name        = 'Ticket → Payment'
        verbose_name_plural = 'Ticket → Payments'

    def __str__(self):
        return self.ticket.reference
