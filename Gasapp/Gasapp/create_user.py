from django.contrib.auth.models import User

# Create a user with username "abc" and password "123"
user = User.objects.create_user(username='abc', password='123')
user.save()

print("User created successfully!")
