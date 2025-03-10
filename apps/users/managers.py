from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    """Custom manager for the User model."""

    def create_user(self, email: str, password=None) -> AbstractBaseUser:
        """
        Creates and saves a User with the given email.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None) -> AbstractBaseUser:
        """
        Creates and saves a superuser with the given email..
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
