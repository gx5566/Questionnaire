# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 03:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('job_id', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=32)),
                ('industry', models.CharField(max_length=16)),
                ('web_site', models.CharField(max_length=128)),
                ('uscc', models.CharField(max_length=128)),
                ('create_date', models.DateField(max_length=128)),
                ('regist_amount', models.IntegerField()),
                ('corporation', models.CharField(max_length=128)),
                ('wechat', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('employee_number', models.IntegerField()),
                ('business_nature', models.CharField(max_length=128)),
                ('business_scope', models.TextField()),
                ('description', models.TextField()),
                ('stock_code', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
                ('savename', models.CharField(max_length=128)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='JoinQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField()),
                ('is_done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('is_checkbox', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('create_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('left', models.IntegerField()),
                ('state', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('comment', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Admin')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('birthday', models.DateField()),
                ('marital_status', models.CharField(max_length=128)),
                ('mobile', models.CharField(max_length=32)),
                ('qq', models.CharField(max_length=32)),
                ('wechat', models.CharField(max_length=128)),
                ('job', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('education', models.CharField(max_length=128)),
                ('major', models.CharField(max_length=128)),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Question.Image')),
                ('user', models.OneToOneField(help_text='系统登录用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Questionnaire'),
        ),
        migrations.AddField(
            model_name='joinquestionnaire',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Questionnaire'),
        ),
        migrations.AddField(
            model_name='joinquestionnaire',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.UserInfo'),
        ),
        migrations.AddField(
            model_name='item',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Question'),
        ),
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Question.Image'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(help_text='系统登录用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answerquestionnaire',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.Item'),
        ),
        migrations.AddField(
            model_name='answerquestionnaire',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.UserInfo'),
        ),
    ]
