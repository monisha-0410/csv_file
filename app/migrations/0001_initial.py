# Generated by Django 4.2.6 on 2024-02-14 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=100)),
                ('Branch', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
            ],
        ),
    ]