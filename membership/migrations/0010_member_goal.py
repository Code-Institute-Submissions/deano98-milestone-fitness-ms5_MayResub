# Generated by Django 3.2 on 2022-04-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_alter_member_tdee_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='goal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
