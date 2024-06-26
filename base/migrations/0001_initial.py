# Generated by Django 4.2.10 on 2024-02-20 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(auto_created=True, verbose_name='Holati')),
                ('name', models.CharField(max_length=2000, verbose_name='Kategoriya nomi')),
                ('sort', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratilgan Sana')),
            ],
            options={
                'verbose_name': 'Katagoriya',
            },
        ),
        migrations.CreateModel(
            name='ishch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='Ishlab chiqaruvchi Nomi')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon nomer uz')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratlgan sana')),
                ('status', models.BooleanField(max_length=20, verbose_name='Holati')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('sahifa', models.CharField(max_length=20000000)),
            ],
            options={
                'verbose_name': 'Ishlab chiqaruvchi (tovarlar shu odamdan olinadi)',
            },
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, verbose_name='F.I.O')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon nomer')),
                ('eskiqarz', models.FloatField(blank=True, max_length=20000, verbose_name='Eski qarz')),
                ('pasport', models.CharField(blank=True, max_length=20200, verbose_name='Pasport s/r')),
                ('kimtomon', models.CharField(blank=True, max_length=20000, verbose_name='Kim tomonidan berilgan')),
                ('date', models.DateField(verbose_name='Amal qillish muddati')),
                ('inn', models.IntegerField(verbose_name='INN')),
                ('bankname', models.CharField(blank=True, max_length=20000, verbose_name='Bank nomi')),
                ('hisob', models.CharField(blank=True, max_length=2000, verbose_name='Hisob raqam')),
                ('mfo', models.CharField(blank=True, max_length=2000, verbose_name='MFO')),
                ('oked', models.CharField(blank=True, max_length=2000, verbose_name='OKED')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('address', models.CharField(blank=True, max_length=999999999, verbose_name='Manzili')),
            ],
            options={
                'verbose_name': 'Kilent',
            },
        ),
        migrations.CreateModel(
            name='sharnoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2131232, verbose_name='sharnoma nomi')),
                ('data', models.FileField(upload_to='static/shartnomalar')),
            ],
            options={
                'verbose_name': 'Shart noma',
            },
        ),
        migrations.CreateModel(
            name='Sklad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=2000, verbose_name='Unique ID')),
                ('name', models.CharField(max_length=2000, verbose_name='Nomi')),
                ('soni', models.IntegerField(verbose_name='Soni(donada)')),
                ('price1', models.FloatField(max_length=2000, verbose_name='Kelgan narxi')),
                ('price2', models.FloatField(max_length=2000, verbose_name='Sotish narxi')),
                ('num', models.IntegerField(verbose_name='..dan kam qolganda ogohlantirish')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Yaratilgan Sana')),
                ('new_date', models.DateField(auto_now=True, verbose_name='Yangilanga Sana')),
                ('status', models.BooleanField(max_length=2000, verbose_name='Holati')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ishch')),
            ],
            options={
                'verbose_name': 'Sklad (Ombor)',
            },
        ),
        migrations.CreateModel(
            name='Tranzaksiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.CharField(max_length=2000, verbose_name='Summa')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.mijoz')),
            ],
        ),
        migrations.CreateModel(
            name='sotilgan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.IntegerField(verbose_name='Soni')),
                ('price', models.FloatField(max_length=20000, verbose_name='Narxi')),
                ('skidka', models.CharField(max_length=20000, verbose_name='Skidka')),
                ('skidkali_narxi', models.FloatField(max_length=20000, verbose_name='Skidkali narxi')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sklad', verbose_name='Product ID')),
                ('transaction_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tranzaksiya', verbose_name='Transaction ID')),
            ],
            options={
                'verbose_name': 'Sotilgan Maxsulot',
            },
        ),
        migrations.CreateModel(
            name='sotibol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.IntegerField(verbose_name='Maxsulot soni')),
                ('prices', models.FloatField(max_length=200, verbose_name='Ummumiy narxi')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('ish_ch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ishch', verbose_name='Ishlab chiqarivchi ID')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sklad', verbose_name='Product ID')),
            ],
            options={
                'verbose_name': 'Sotib olingan produktlar',
            },
        ),
        migrations.CreateModel(
            name='kassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(max_length=2000, verbose_name='SO`M(UZS-so`m)')),
                ('qogpz', models.FloatField(max_length=2000, verbose_name='Qog`oz(USD-$)')),
                ('bankhisob', models.CharField(max_length=20000, verbose_name='Bank hisobi')),
                ('perechisleniya', models.CharField(max_length=20000, verbose_name='Perechisleniya')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Sanasi')),
                ('comment', models.CharField(max_length=2000000000000, verbose_name='Comment')),
                ('kilent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mijoz', verbose_name='Mijoz ID')),
            ],
            options={
                'verbose_name': 'KASSA',
            },
        ),
    ]
