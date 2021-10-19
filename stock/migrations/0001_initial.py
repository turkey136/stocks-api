# Generated by Django 3.2.8 on 2021-10-19 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=10)),
                ('name', models.TextField(max_length=100)),
                ('industry', models.TextField(max_length=500)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.market')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.sector')),
            ],
        ),
    ]