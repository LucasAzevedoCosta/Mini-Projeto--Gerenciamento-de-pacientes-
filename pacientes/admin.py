from django.contrib import admin
from .models import Pacientes, Consultas,Tarefas, Visualizacoes

# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Consultas)
admin.site.register(Tarefas)
admin.site.register(Visualizacoes)