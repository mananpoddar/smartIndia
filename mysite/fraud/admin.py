from django.contrib import admin
from fraud.models import Aadhar,Bank_formalities,tracked,Bank_details,bank_statement,predicted_features,report
# Register your models here.
admin.site.register(Bank_details)
admin.site.register(Bank_formalities)
admin.site.register(tracked)
admin.site.register(Aadhar)
admin.site.register(bank_statement)
admin.site.register(predicted_features)
admin.site.register(report)
