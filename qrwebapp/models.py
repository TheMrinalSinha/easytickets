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

PAYMENT_STATUS = (
    ('DONE',    'DONE'),
    ('PENDING', 'PENDING'))

class Ticket(models.Model):
    passanger      = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    source         = models.CharField('Starting Point', max_length=32)
    destination    = models.CharField('Ending Point', max_length=32)
    fare           = models.DecimalField('Journey Fare', max_digits=5, decimal_places=2)
    payment_status = models.CharField('Payment Status', choices=PAYMENT_STATUS, default='PENDING', max_length=16)
    created_on     = models.DateTimeField('Ticket Time', auto_now_add=True)

    def __str__(self):
        return str(self.passanger) + '(' + self.source + '→' + self.destination + ')'

    @property
    def reference(self):
        return 'TK%05d' % self.pk

class Route(models.Model):
    source      = models.CharField('Starting Point', max_length=32)
    destination = models.CharField('Ending Point', max_length=32)
    fare        = models.DecimalField('Journey Fare', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.source + '→' + self.destination

    class Meta:
        verbose_name        = 'Route'
        verbose_name_plural = 'Routes'
        unique_together     = ('source', 'destination')

class RazorpayPayment(models.Model):
    ticket              = models.ForeignKey(Ticket, on_delete=models.CASCADE)
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
