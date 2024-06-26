# Generated by Django 4.1.2 on 2024-04-25 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_item_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('rating', models.PositiveIntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location'),
        ),
    ]
