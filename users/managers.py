from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password = None , **kwargs):
        if not email:
            raise ValueError("Please Email must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email , **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None, **kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)

        if not kwargs.get('is_staff'):
            raise ValueError("superuser must hove to is staff is True")
        if not kwargs.get('is_superuser'):
            raise ValueError("superuser must have is_superuser is True")
        
        return self.create_user(email,password,**kwargs)