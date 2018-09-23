<<<<<<< HEAD
# Generated by Django 2.1b1 on 2018-09-22 14:24

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 2.1.1 on 2018-09-20 14:14

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
>>>>>>> a4af1d00283fb766ff8537be5ed1082455fb0442


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('avatar', models.ImageField(default='profile.png', upload_to='profile_pic')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desp', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='../static/images/')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('minimum_price', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('start', models.DateTimeField(default=datetime.datetime(2018, 9, 20, 14, 14, 2, 308652, tzinfo=utc), null=True)),
                ('end_date', models.DateTimeField(default=datetime.date(2018, 9, 21))),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('current_bid', models.IntegerField(default=0)),
>>>>>>> a4af1d00283fb766ff8537be5ed1082455fb0442
            ],
        ),
    ]
