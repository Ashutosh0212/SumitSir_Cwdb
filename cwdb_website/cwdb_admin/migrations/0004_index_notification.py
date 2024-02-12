# Generated by Django 4.2.6 on 2024-02-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwdb_admin', '0003_alter_proposal_expected_outcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
