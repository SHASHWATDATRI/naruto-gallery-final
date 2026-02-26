set -o errexit

pip install -r requirements.txt

python manage.py migrate

# Ye line niche add karein (Isse admin/admin123 account ban jayega)
python -c "import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"