# Generated by Django 4.2.4 on 2024-08-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_height', models.FloatField()),
                ('max_height', models.FloatField()),
                ('min_width', models.FloatField()),
                ('max_width', models.FloatField()),
                ('min_size', models.FloatField()),
                ('max_size', models.FloatField()),
                ('is_jpg', models.BooleanField()),
                ('is_png', models.BooleanField()),
                ('is_jpeg', models.BooleanField(default=True)),
                ('bgcolor_threshold', models.FloatField(default=50)),
                ('blurness_threshold', models.FloatField(default=35)),
                ('pixelated_threshold', models.FloatField(default=50)),
                ('greyness_threshold', models.FloatField(default=0)),
                ('symmetry_threshold', models.FloatField(default=20)),
                ('bypass_height_check', models.BooleanField(default=False)),
                ('bypass_width_check', models.BooleanField(default=False)),
                ('bypass_size_check', models.BooleanField(default=False)),
                ('bypass_format_check', models.BooleanField(default=False)),
                ('bypass_background_check', models.BooleanField(default=False)),
                ('bypass_blurness_check', models.BooleanField(default=False)),
                ('bypass_greyness_check', models.BooleanField(default=False)),
                ('bypass_symmetry_check', models.BooleanField(default=False)),
                ('bypass_head_check', models.BooleanField(default=False)),
                ('bypass_eye_check', models.BooleanField(default=False)),
                ('bypass_corrupted_check', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.FileField(upload_to='photo_folder/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]