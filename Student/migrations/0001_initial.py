# Generated by Django 2.1.15 on 2023-04-05 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
                ('domain_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'domains',
                'ordering': ('domain_name',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student_images')),
                ('gpa', models.FloatField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Student.Domain')),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
        ),
    ]
