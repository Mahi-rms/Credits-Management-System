# CREDITS MANAGEMENT SYSTEM

To Run the Project follow the steps:
1. Install the modules updated in "requirements.txt"
2. Create a ".env" file and fill the following details:

[

SECRET_KEY=''

EMAIL_ADDRESS=''

EMAIL_PASSWORD=''

RAZORPAY_ID=''

RAZORPAY_KEY=''

]

3. Enable less-secure app access in Gmail Account settings.
4. You can edit the constant 'EXPIRY' in settings
5. Run the following commands:

i) python manage.py makemigrations

ii) python manage.py migrate

iii) python manage.py createsuperuser (if you want to see the Admin Panel)

iv) python manage.py runserver
