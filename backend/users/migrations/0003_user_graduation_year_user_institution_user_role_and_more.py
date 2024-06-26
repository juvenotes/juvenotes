# Generated by Django 5.0.4 on 2024-05-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='graduation_year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2024),
        ),
        migrations.AddField(
            model_name='user',
            name='institution',
            field=models.CharField(choices=[('UON', 'University of Nairobi'), ('KU', 'Kenyatta University'), ('AKU', 'Aga Khan University'), ('MKU', 'Mount Kenya University'), ('JKUAT', 'JKUAT'), ('EG', 'Egerton'), ('MMUST', 'MMUST'), ('MSU', 'Maseno University')], default='UON', max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ST', 'Student'), ('PR', 'Professional')], max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='student_profession',
            field=models.CharField(choices=[('MS', 'Medical Student'), ('NS', 'Nursing Student'), ('PS', 'Pharmacy Student'), ('DS', 'Dental Surgery Student'), ('DR', 'Doctor'), ('NR', 'Nurse'), ('PH', 'Pharmacist'), ('DT', 'Dentist')], default='MS', max_length=2),
        ),
    ]
