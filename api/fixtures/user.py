from api.user.models import User

user_data = {"username": "admin", "password": "1234567890", "email": "admin@example.com"}

User.objects.create_user(**user_data)
