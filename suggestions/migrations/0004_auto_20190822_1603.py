# Generated by Django 2.2.4 on 2019-08-22 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestions', '0003_suggestion_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='upvotes',
            new_name='suggestion_upvotes',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='price',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='upvote_price',
        ),
        migrations.CreateModel(
            name='Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suggestions.Suggestion')),
                ('upvote_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Up votes',
            },
        ),
    ]
