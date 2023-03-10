# Generated by Django 4.1.5 on 2023-01-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionSurveyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('party_name', models.CharField(choices=[('AAA', 'AAA'), ('AAB', 'AAB'), ('AAC', 'AAC'), ('AAD', 'AAD')], max_length=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
