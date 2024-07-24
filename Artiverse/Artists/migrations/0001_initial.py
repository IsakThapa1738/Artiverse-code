# Generated by Django 5.0.6 on 2024-06-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('biography', models.TextField(null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='artist_profiles/')),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('social_links', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]