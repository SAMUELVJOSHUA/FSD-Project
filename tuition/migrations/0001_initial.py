# Generated by Django 2.2.2 on 2019-07-05 11:37

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
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('subjects', models.CharField(max_length=1000, verbose_name='Subjects')),
                ('type', models.CharField(max_length=200, verbose_name='Type')),
                ('grade', models.CharField(max_length=200, verbose_name='Class')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
                ('pref_gender', models.CharField(max_length=20, verbose_name='Preferred Gender')),
                ('std_count', models.IntegerField(max_length=10, verbose_name='Student Count')),
                ('time', models.CharField(max_length=200, verbose_name='Teaching Time')),
                ('days', models.IntegerField(max_length=10, verbose_name='How many days a week')),
                ('location', models.CharField(max_length=1000, verbose_name='Location')),
                ('salary', models.IntegerField(max_length=10, verbose_name='Monthly Salary')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]