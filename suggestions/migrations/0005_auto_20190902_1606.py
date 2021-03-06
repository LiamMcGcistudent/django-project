# Generated by Django 2.2.4 on 2019-09-02 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestions', '0004_auto_20190822_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='suggestionUpvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoted_suggestion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='suggestions.Suggestion')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Upvotes',
        ),
    ]
