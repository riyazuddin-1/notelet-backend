from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid

"""
Django has its own User model containing the following fields:-
id: Primary key for the user, automatically generated unless customized.
username: Stores a unique username for user authentication.
password: Stores the hashed password for secure authentication.
first_name: Optional field for the user's first name.
last_name: Optional field for the user's last name.
email: Optional field for the user's email, used for authentication if specified.
is_staff: Indicates whether the user can access the Django admin site.
is_active: Specifies if the user account is active and able to authenticate.
is_superuser: Grants the user full permissions and access to all Django admin parts.
last_login: Timestamp of the user's most recent login.
date_joined: Timestamp of when the user account was created.

We need to create 'custom manager' if we want a custom User model for the application.
"""

# UserManager extends BaseUserManager class to manage model instances
class UserManager(BaseUserManager):
    """
    BaseUserManager: A helper class that simplifies the creation of users and superusers for custom user models.
    """

    def create_user(self, email, name=None, password=None, **extra_fields):
        # Ensure an email is provided, otherwise raise an error
        if not email:
            raise ValueError('Email is required')
        
        # Normalize the email to ensure it follows a consistent format (e.g., lowercase)
        email = self.normalize_email(email)
        
        # Create a user instance with the given email, name, and extra fields
        user = self.model(email=email, name=name or '', **extra_fields)
        
        # Hash the provided password and set it on the user instance
        user.set_password(password)
        
        # Save the user instance to the database (using the correct database if there are multiple)
        user.save(using=self._db)
        
        # Return the created user instance
        return user

    def create_superuser(self, email, name=None, password=None, **extra_fields):
        # Ensure that the superuser is marked as both staff and superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Create a superuser using the create_user method, passing all extra fields
        return self.create_user(email, name, password, **extra_fields)

# Custom User model that extends AbstractBaseUser and PermissionsMixin for authentication and permissions functionality
class User(AbstractBaseUser, PermissionsMixin):
    """
    AbstractBaseUser: A base class for creating a custom user model. It provides basic functionality like password hashing, authentication, etc.
    PermissionsMixin: A mixin that adds fields like is_staff, is_superuser, and groups, which are needed for handling user permissions.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Link the custom manager to the model (handles user creation logic)
    objects = UserManager()

    # Define the field to be used for authentication (email instead of username)
    USERNAME_FIELD = 'email'
    
    # This list contains any additional fields that are required when creating a superuser (none here)
    REQUIRED_FIELDS = []

    # String representation of the User model instance (returns the user's email)
    def __str__(self):
        return self.email
    