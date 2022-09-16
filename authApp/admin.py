from django.contrib import admin
from .models.acudiente import acudiente
from .models.paciente import paciente
from .models.user import User

# Register your models here.
admin.site.register(acudiente)
admin.site.register(paciente)
admin.site.register(User)