# Generated by Django 4.0.7 on 2023-03-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PEDIDO REALIZADO', 'Realizado'), ('EM ANDAMENTO', 'Andamento'), ('ENTREGUE', 'Entregue')], default='PEDIDO REALIZADO', max_length=40)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
