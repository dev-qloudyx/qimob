from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.utils.translation import gettext as _

# Create your models here.

class UserRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name
    

class UserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None, role = None):
        if not email:
            raise ValueError(_('Users must have an email address.'))
        if not username:
            raise ValueError(_('Users must have a username.'))
        if role is None:
            raise ValueError(_('Users must have a role.'))
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role
          
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            role=UserRole.objects.get(role_name="admin")
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT, default=2)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_active = models.DateTimeField(verbose_name='Data Última Activação', blank=True, null=True)
    last_inactive = models.DateTimeField(verbose_name='Data Última Inactivação', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # team_leader_relation = models.ForeignKey('TeamLeader', on_delete=models.SET_NULL, blank=True, null=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def role_is_admin(self):
        return self.role == UserRole.objects.get(role_name="admin")
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=80, verbose_name=_('Full Name'), blank=True)
    about = models.TextField(
        max_length=240, verbose_name=_('About'), blank=True)
    image = models.ImageField(upload_to='profile_pics', verbose_name=_('Photo') , blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

class TeamLeader(models.Model):
    team_leader = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
