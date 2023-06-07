# Generated by Django 4.2.1 on 2023-06-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseigant',
            fields=[
                ('idenseignant', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=40, null=True)),
                ('prenom', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'enseigant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('idgroupe', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'groupe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('idetudiant', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=40, null=True)),
                ('prenom', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('photo', models.ImageField(null=True, upload_to='ecole/')),
                ('groupe', models.ForeignKey(blank=True, db_column='groupe', null=True, on_delete=django.db.models.deletion.CASCADE, to='sae23.groupe')),
            ],
            options={
                'db_table': 'etudiant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idcours', models.SmallAutoField(primary_key=True, serialize=False)),
                ('titre_cours', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('duree', models.TimeField(blank=True, null=True)),
                ('enseigant', models.ForeignKey(blank=True, db_column='enseigant', null=True, on_delete=django.db.models.deletion.CASCADE, to='sae23.enseigant')),
            ],
            options={
                'db_table': 'cours',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('idabsence', models.SmallAutoField(primary_key=True, serialize=False)),
                ('justifier', models.TextField(blank=True, null=True)),
                ('justification', models.CharField(blank=True, max_length=5000, null=True)),
                ('cours', models.ForeignKey(blank=True, db_column='cours', null=True, on_delete=django.db.models.deletion.CASCADE, to='sae23.cours')),
                ('etudiant', models.ForeignKey(blank=True, db_column='etudiant', null=True, on_delete=django.db.models.deletion.CASCADE, to='sae23.etudiant')),
            ],
            options={
                'db_table': 'absence',
                'managed': True,
            },
        ),
    ]
