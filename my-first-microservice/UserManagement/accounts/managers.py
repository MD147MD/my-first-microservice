from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    

    def create_user(self,full_name,email,password):
        if not email:
            raise ValueError('Email Cannot Be Null')

        if not full_name:
            raise ValueError('Full Name Cannot Be Null')
        
        user = self.model(email=self.normalize_email(email),full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user


    
    def create_superuser(self,full_name,email,password):
        if not email:
            raise ValueError('Email Cannot Be Null')

        if not full_name:
            raise ValueError('Full Name Cannot Be Null')
        user = self.create_user(full_name,email,password)
        user.is_admin = True
        user.save(using=self._db)
        return user