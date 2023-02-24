from django.contrib import admin

from client_management.models import Work
from client_management.models import Client
from client_management.models import Assignment
from client_management.models import Artist

admin.site.register(Work)
admin.site.register(Client)
admin.site.register(Assignment)
admin.site.register(Artist)