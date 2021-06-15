# Generated by Django 3.2 on 2021-05-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Actions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomcode', models.TextField(blank=True, null=True)),
                ('trainee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.people')),
                ('trainerChat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.trainer')),
            ],
        ),
    ]