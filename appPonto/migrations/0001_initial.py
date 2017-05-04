# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 11:19
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcao', models.CharField(max_length=200, verbose_name='Nome da função')),
            ],
            options={
                'permissions': (('view_cargo', 'Can see cargo'),),
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'permissions': (('view_departamento', 'Can see departamento'),),
            },
        ),
        migrations.CreateModel(
            name='Dias_sem_expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('hora_entrada', models.TimeField(default=django.utils.timezone.now)),
                ('hora_saida', models.TimeField(default=django.utils.timezone.now)),
                ('local', models.CharField(max_length=200, verbose_name='local')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('Email', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matricula')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('senha', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia_funcionario',
            fields=[
                ('frequencia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Frequencia')),
            ],
            options={
                'permissions': (('view_frequencia_funcionario', 'Can see frequencia'), ('view_frequencia_funcionario_admin', 'Can see frequencia a mais')),
            },
            bases=('appPonto.frequencia',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Pessoa')),
            ],
            options={
                'permissions': (('view_funcionario', 'Can see funcionario'),),
            },
            bases=('appPonto.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Cargo', verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='frequencia_funcionario',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Funcionario', verbose_name='Funcionario'),
        ),
    ]
