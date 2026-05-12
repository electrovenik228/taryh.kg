#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Load fixture data (safe to run on every deploy — replaces existing records)
python manage.py loaddata fixtures/initial_data.json

# Create admin user if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@taryh.kg', 'admin123')
    print('Admin user created.')
else:
    print('Admin user already exists.')
"
