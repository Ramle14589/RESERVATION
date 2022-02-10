# Generated by Django 3.2.10 on 2021-12-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chambre', '0004_remove_reservation_id_concerne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='Tag',
            field=models.ManyToManyField(to='chambre.Tag'),
        ),
    ]
