# Generated by Django 2.1.2 on 2018-10-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_anchor_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '记录', 'verbose_name_plural': '记录'},
        ),
        migrations.AlterField(
            model_name='record',
            name='a_update_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='录入时间'),
        ),
    ]
