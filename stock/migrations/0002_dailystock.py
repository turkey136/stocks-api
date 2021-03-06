# Generated by Django 3.2.8 on 2021-10-19 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('low', models.FloatField()),
                ('high', models.FloatField()),
                ('amount_of_change', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_stocks', to='stock.stock')),
            ],
        ),
    ]
