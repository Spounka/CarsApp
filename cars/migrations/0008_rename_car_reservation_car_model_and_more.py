# Generated by Django 4.1.3 on 2022-12-03 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_reservation_car_brand_alter_reservation_car_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='car',
            new_name='car_model',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_model',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_price',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='image_url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='reservation',
            name='engine_type',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_time',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='service',
            name='is_piece',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=30)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.service')),
            ],
        ),
    ]
