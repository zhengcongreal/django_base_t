# Generated by Django 2.2.5 on 2020-10-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30, verbose_name='学生姓名')),
                ('sage', models.IntegerField(default=0, verbose_name='年龄')),
                ('semail', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'db_table': 'tb_students',
            },
        ),
    ]