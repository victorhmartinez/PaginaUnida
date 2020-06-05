# Generated by Django 2.1.7 on 2019-06-04 19:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCategory', models.AutoField(primary_key=True, serialize=False)),
                ('nameCategory', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('idItemCategory', models.AutoField(primary_key=True, serialize=False)),
                ('nameItemCategory', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('first_last_name', models.CharField(max_length=255)),
                ('second_last_name', models.CharField(max_length=255)),
                ('Persons_role', models.ManyToManyField(to='login.ItemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Persons_Contacts',
            fields=[
                ('contact_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ItemCategory')),
                ('persons_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persons')),
            ],
        ),
        migrations.CreateModel(
            name='Persons_departaments',
            fields=[
                ('persons_departaments_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ItemCategory')),
                ('persons_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persons')),
            ],
        ),
        migrations.CreateModel(
            name='Persons_media',
            fields=[
                ('persons_media_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ItemCategory')),
                ('persons_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persons')),
            ],
        ),
        migrations.CreateModel(
            name='Persons_role',
            fields=[
                ('persons_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ItemCategory')),
                ('persons_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persons')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persons'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]