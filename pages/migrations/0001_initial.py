# Generated by Django 4.1.5 on 2023-05-08 03:27

from django.db import migrations, models
import pages.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, validators=[pages.models.validate_email])),
                ('message', models.TextField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, validators=[pages.models.validate_email])),
                ('rating', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='JobPortal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=255)),
                ('descriptions', models.CharField(max_length=555)),
                ('exprience', models.IntegerField()),
                ('salary', models.CharField(max_length=254)),
                ('apply_link', models.CharField(max_length=255)),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OnlineApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('application_no', models.CharField(default=pages.models.application_id, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, validators=[pages.models.validate_email])),
                ('mobile', models.CharField(max_length=10)),
                ('current_company', models.CharField(max_length=255)),
                ('current_salary', models.CharField(max_length=255)),
                ('expected_salary', models.IntegerField()),
                ('exprience', models.IntegerField()),
                ('skills', models.TextField(max_length=555)),
                ('project_done', models.TextField(blank=True, max_length=555, null=True)),
                ('address', models.TextField(blank=True, max_length=555, null=True)),
                ('awards', models.TextField(blank=True, max_length=555, null=True)),
                ('resume', models.FileField(upload_to='upload', validators=[pages.models.resume_size])),
                ('photo', models.ImageField(upload_to='upload', validators=[pages.models.photo_size])),
                ('sign', models.ImageField(upload_to='upload', validators=[pages.models.sign_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]