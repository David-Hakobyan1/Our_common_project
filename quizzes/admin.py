from django.contrib import admin
from .models import SportQuestion, CountriesQuestion, DifferentQuestion

admin.site.register(SportQuestion)
admin.site.register(CountriesQuestion)
admin.site.register(DifferentQuestion)
