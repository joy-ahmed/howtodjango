# Generated by Django 4.2.4 on 2023-12-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='users/avatar/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(choices=[('', '---Select account type---'), ('blogger', 'Blogger'), ('user', 'User')], max_length=10),
        ),
    ]
