# Generated by Django 2.2 on 2019-04-18 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('authtools', '0003_auto_20160128_0912'),
        ('profiles', '0001_initial'),
        ('workflow', '0027_auto_20190418_1057'),
        ('ontask_oauth', '0004_auto_20181208_1306'),
        ('logs', '0017_auto_20190213_1623'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('scheduler', '0035_remove_scheduledaction_deleted'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnTaskUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
