# Generated by Django 5.1.2 on 2024-10-23 02:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cursos', models.CharField(choices=[('Desenha', 'Curso desenha'), ('Programador', 'Curso Programador'), ('BackEnd', 'Curso BackEnd'), ('FrondEnD', 'Curso FrondEnd'), ('Trabalha', 'Curso Com Trabalha em casa')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=20)),
                ('numero', models.CharField(max_length=11)),
                ('Email', models.EmailField(default='', max_length=250)),
                ('pub_data', models.DateField(default=datetime.date.today)),
                ('tipo_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='python.curso')),
            ],
        ),
    ]
