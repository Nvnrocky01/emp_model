from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Dept)

admin.site.register(Employee)

admin.site.register(Bonus)

admin.site.register(Salgrade)