# Generated by Django 4.0.6 on 2022-07-25 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whytingapp', '0003_alter_store_owner_id_alter_store_waiting_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primary Key')),
                ('description', models.CharField(max_length=100, verbose_name='좌석 정보')),
                ('name', models.CharField(max_length=30, verbose_name='카테고리 이름')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='end_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='start_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='store_image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_image', to='whytingapp.store'),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_store', to='whytingapp.store')),
            ],
        ),
        migrations.CreateModel(
            name='SeatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='store_image')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_image', to='whytingapp.seat')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_store', to='whytingapp.store'),
        ),
    ]