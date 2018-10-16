# Generated by Django 2.0.9 on 2018-10-16 02:37

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageBlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_pages', to='blog.BlogCategory')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories2', to='blog.PostPage')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='blogpageblogcategory',
            unique_together={('page', 'blog_category')},
        ),
    ]