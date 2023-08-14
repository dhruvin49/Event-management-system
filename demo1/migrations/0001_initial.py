# Generated by Django 3.2.18 on 2023-03-27 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('parent_category', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deactive')], default=1)),
                ('deleted', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('id_number', models.IntegerField()),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('Event Coordinator', 'Event Coordinator'), ('Event Planner', 'Event Planner'), ('Event Manager', 'Event Manager'), ('Registration Coordinator', 'Registration Coordinator'), ('Volunteer Coordinator', 'Volunteer Coordinator'), ('Marketing Coordinator', 'Marketing Coordinator'), ('Social Media Coordinator', 'Social Media Coordinator'), ('Logistics Coordinator', 'Logistics Coordinator'), ('Audiovisual Coordinator', 'Audiovisual Coordinator'), ('Catering Coordinator', 'Catering Coordinator'), ('Security Coordinator', 'Security Coordinator'), ('Sponsorship Coordinator', 'Sponsorship Coordinator'), ('Speaker Coordinator', 'Speaker Coordinator'), ('Production Assistant', 'Production Assistant'), ('Technical Support Staff', 'Technical Support Staff'), ('Onsite Support Staff', 'Onsite Support Staff'), ('Event Host or Emcee', 'Event Host or Emcee'), ('Photographer', 'Photographer'), ('Videographer', 'Videographer'), ('Graphic Designer', 'Graphic Designer'), ('Web Designer', 'Web Designer'), ('Copywriter', 'Copywriter'), ('Event Consultant', 'Event Consultant'), ('Data Analyst', 'Data Analyst'), ('Event Operations Manager', 'Event Operations Manager'), ('Sales Manager', 'Sales Manager'), ('Finance Manager', 'Finance Manager'), ('Customer Service Representative', 'Customer Service Representative'), ('Event Attendant', 'Event Attendant')], default=1, help_text='Select Job Role', max_length=200)),
                ('profile', models.ImageField(upload_to='')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deactive')], default=1)),
                ('deleted', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('datetime_from', models.DateTimeField()),
                ('datetime_to', models.DateTimeField()),
                ('has_tickets', models.BooleanField()),
                ('total_count', models.IntegerField()),
                ('total_cost', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('event_grand_total', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('pending_amount', models.IntegerField()),
                ('has_sabevent', models.BooleanField()),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.client')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('datetime_from', models.DateTimeField()),
                ('datetime_to', models.DateTimeField()),
                ('sub_location', models.CharField(default='', max_length=200)),
                ('eventID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_number', models.IntegerField()),
                ('paymentMethod', models.CharField(choices=[('Credit cards', 'Credit cards'), ('Debit cards', 'Debit cards'), ('PayPal', 'PayPal'), ('Apple Pay', 'Apple Pay'), ('Google Pay', 'Google Pay'), ('Stripe', 'Stripe'), ('Square', 'Square'), ('Bank transfers', 'Bank transfers'), ('Electronic wallets', 'Electronic wallets'), ('Cryptocurrencies', 'Cryptocurrencies')], default=1, max_length=200)),
                ('amount', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_locations',
            fields=[
                ('event_location_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('street_detail', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('Aruba', 'Aruba'), ('Afghanistan', 'Afghanistan'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Åland Islands', 'Åland Islands'), ('Albania', 'Albania'), ('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('American Samoa', 'American Samoa'), ('Antarctica', 'Antarctica'), ('French Southern Territories', 'French Southern Territories'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Burundi', 'Burundi'), ('Belgium', 'Belgium'), ('Benin', 'Benin'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Burkina Faso', 'Burkina Faso'), ('Bangladesh', 'Bangladesh'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Bahamas', 'Bahamas'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Bermuda', 'Bermuda'), ('Bolivia, Plurinational State of', 'Bolivia, Plurinational State of'), ('Brazil', 'Brazil'), ('Barbados', 'Barbados'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Central African Republic', 'Central African Republic'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Switzerland', 'Switzerland'), ('Chile', 'Chile'), ('China', 'China'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Cameroon', 'Cameroon'), ('Congo, The Democratic Republic of the', 'Congo, The Democratic Republic of the'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Cabo Verde', 'Cabo Verde'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cayman Islands', 'Cayman Islands'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Denmark', 'Denmark'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('Eritrea', 'Eritrea'), ('Western Sahara', 'Western Sahara'), ('Spain', 'Spain'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('France', 'France'), ('Faroe Islands', 'Faroe Islands'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Gabon', 'Gabon'), ('United Kingdom', 'United Kingdom'), ('Georgia', 'Georgia'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Gambia', 'Gambia'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('French Guiana', 'French Guiana'), ('Guam', 'Guam'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Ireland', 'Ireland'), ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'), ('Iraq', 'Iraq'), ('Iceland', 'Iceland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Macao', 'Macao'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Maldives', 'Maldives'), ('Mexico', 'Mexico'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Myanmar', 'Myanmar'), ('Montenegro', 'Montenegro'), ('Mongolia', 'Mongolia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Mozambique', 'Mozambique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Martinique', 'Martinique'), ('Mauritius', 'Mauritius'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mayotte', 'Mayotte'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Niue', 'Niue'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Pitcairn', 'Pitcairn'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Palau', 'Palau'), ('Papua New Guinea', 'Papua New Guinea'), ('Poland', 'Poland'), ('Puerto Rico', 'Puerto Rico'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Portugal', 'Portugal'), ('Paraguay', 'Paraguay'), ('Palestine, State of', 'Palestine, State of'), ('French Polynesia', 'French Polynesia'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Senegal', 'Senegal'), ('Singapore', 'Singapore'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Solomon Islands', 'Solomon Islands'), ('Sierra Leone', 'Sierra Leone'), ('El Salvador', 'El Salvador'), ('San Marino', 'San Marino'), ('Somalia', 'Somalia'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Serbia', 'Serbia'), ('South Sudan', 'South Sudan'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Suriname', 'Suriname'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Sweden', 'Sweden'), ('Eswatini', 'Eswatini'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Seychelles', 'Seychelles'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Chad', 'Chad'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Timor-Leste', 'Timor-Leste'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Uruguay', 'Uruguay'), ('United States', 'United States'), ('Uzbekistan', 'Uzbekistan'), ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Venezuela, Bolivarian Republic of', 'Venezuela, Bolivarian Republic of'), ('Virgin Islands, British', 'Virgin Islands, British'), ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=265)),
                ('zipcode', models.CharField(max_length=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_note', models.CharField(max_length=200)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.employees')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catgory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.categories')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_location_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='demo1.event_locations'),
        ),
    ]
