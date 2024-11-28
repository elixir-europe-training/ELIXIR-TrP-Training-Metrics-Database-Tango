# Generated by Django 4.2.16 on 2024-11-13 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0002_alter_event_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demographic",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="demographic",
                to="metrics.event",
            ),
        ),
        migrations.AlterField(
            model_name="impact",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="impact",
                to="metrics.event",
            ),
        ),
        migrations.AlterField(
            model_name="quality",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quality",
                to="metrics.event",
            ),
        ),
    ]