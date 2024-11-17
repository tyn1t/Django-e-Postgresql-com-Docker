from django.db import models
from datetime import date

# Create your models here.
class Usuario(models.Model):
    sexo = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]
    tipo_curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, null=False)
    sobrenome = models.CharField(max_length=30, null=False)
    genero = models.CharField(max_length=20,choices=sexo) 
    numero = models.CharField(max_length=11,  blank=True, null=True, verbose_name='Nº telefone celular')
    Email = models.EmailField(max_length=250, default='', null=False)
    

    pub_data = models.DateField(default=date.today)


    
    def __str__(self) -> str:
        return f""" Id: {self.id} Nome: {self.nome} 
                    Sobrenome: {self.sobrenome}, Numero: {self.numero}
                    Email: {self.Email}, Genero: {[sexo for sexo in self.genero][0]}
                """

class Curso(models.Model):
    tipo = [
        ("Desenha","Curso desenha"),
        ("Programador","Curso Programador"),
        ("BackEnd","Curso BackEnd"),
        ("FrondEnD","Curso FrondEnd"),
        ("Trabalha","Curso Com Trabalha em casa"),
    ]
    cursos = models.CharField(max_length=100, choices=tipo)     
        
    def __str__(self) -> str:
        return f"{self.cursos}"
    
