# Generated by Django 3.2.10 on 2022-01-05 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chambre', '0015_rename_nom_chambre_nom_ch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='date_d',
            new_name='date_d_r',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='date_f',
            new_name='date_f_r',
        ),
    ]