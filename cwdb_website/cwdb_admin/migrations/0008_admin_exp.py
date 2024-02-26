# Generated by Django 4.2.6 on 2024-02-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwdb_admin', '0007_alter_proposal_location_of_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_exp', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Admin Exp (in lakhs)')),
                ('quarter', models.CharField(choices=[('Q1', 'Quarter 1 (April-June)'), ('Q2', 'Quarter 2 (July-September)'), ('Q3', 'Quarter 3 (October-December)'), ('Q4', 'Quarter 4 (January-March)')], max_length=9)),
                ('financial_year', models.CharField(choices=[('2000-2001', '2000-2001'), ('2001-2002', '2001-2002'), ('2002-2003', '2002-2003'), ('2003-2004', '2003-2004'), ('2004-2005', '2004-2005'), ('2005-2006', '2005-2006'), ('2006-2007', '2006-2007'), ('2007-2008', '2007-2008'), ('2008-2009', '2008-2009'), ('2009-2010', '2009-2010'), ('2010-2011', '2010-2011'), ('2011-2012', '2011-2012'), ('2012-2013', '2012-2013'), ('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], max_length=9)),
            ],
        ),
    ]
