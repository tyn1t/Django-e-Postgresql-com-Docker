from django.contrib import admin
from .models import Usuario, Curso

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
     model = Usuario
     list_display  = ["nome", "sobrenome", "Email", "numero", "tipo_curso", "genero",]
     
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Curso)
