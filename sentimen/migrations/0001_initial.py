# Generated by Django 4.0.3 on 2022-03-29 20:29

from django.db import migrations, models
import django.db.models.deletion
import sentimen.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
                ('semester', models.SmallIntegerField(choices=[('SATU', 1), ('DUA', 2), ('TIGA', 3), ('EMPAT', 4), ('LIMA', 5), ('ENAM', 6), ('TUJUH', 7), ('DELAPAN', 8)], default=sentimen.models.Semester['SATU'], null=True)),
            ],
            options={
                'db_table': 'tb_matkul',
            },
        ),
        migrations.CreateModel(
            name='LearningJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, null=True)),
                ('nama', models.CharField(max_length=100, null=True)),
                ('nim', models.CharField(max_length=10, null=True)),
                ('semester', models.SmallIntegerField(choices=[('SATU', 1), ('DUA', 2), ('TIGA', 3), ('EMPAT', 4), ('LIMA', 5), ('ENAM', 6), ('TUJUH', 7), ('DELAPAN', 8)], default=sentimen.models.Semester['SATU'], null=True)),
                ('golongan', models.CharField(max_length=2, null=True)),
                ('minggu', models.SmallIntegerField(null=True)),
                ('tanggal_kuliah', models.DateField(null=True)),
                ('topik', models.CharField(max_length=255, null=True)),
                ('pembahasan', models.TextField(null=True)),
                ('cleaning', models.TextField(null=True)),
                ('casefolding', models.TextField(null=True)),
                ('tokenizing', models.TextField(null=True)),
                ('normalisasi', models.TextField(null=True)),
                ('stopword', models.TextField(null=True)),
                ('stemming', models.TextField(null=True)),
                ('cleaned', models.TextField(null=True)),
                ('matkul', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sentimen.matakuliah')),
            ],
            options={
                'db_table': 'tb_journal',
            },
        ),
        migrations.CreateModel(
            name='JurnalSimilarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True)),
                ('score_percentage', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('doc1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fn_lj_doc1', to='sentimen.learningjournal')),
                ('doc2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fn_lj_doc2', to='sentimen.learningjournal')),
            ],
            options={
                'db_table': 'jurnal_similarity',
            },
        ),
    ]
