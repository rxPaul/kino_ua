from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_alter_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='movies',
            field=models.ManyToManyField(to='movies.movie', verbose_name='Movie'),
        ),
    ]
