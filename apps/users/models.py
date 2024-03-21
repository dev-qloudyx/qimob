from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.users.validators import only_char, only_int, validate_file
from PIL import Image
# from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _

# Create your models here.


class MasterConfig(models.Model):
    is_active = models.BooleanField(default=True)
    short_desc = models.CharField(max_length=100, verbose_name=_('short description'))
    long_desc = models.CharField(max_length=254, verbose_name=_('long description'), blank=True, null=True)

    def __str__(self):
        return f'{self.short_desc}'

class License(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name=_('Client'))
    nif = models.CharField(max_length=9, verbose_name='NIF', validators=[only_int])
    # address_token = 
    email = models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')
    phone = models.CharField(max_length=15, verbose_name=_('Phone Number'), validators=[only_int])
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    limit_date = models.DateField(verbose_name=_('Limit Date'))
    config = models.ForeignKey(MasterConfig, on_delete=models.CASCADE, verbose_name=_('configuration id'))
    logo = models.ImageField(verbose_name=_('Logo'), upload_to='license_logos')

    def __str__(self):
        return self.customer_name




class UserRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.role_name}'
    

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
    license = models.ForeignKey(License,related_name='user_related_license', on_delete=models.CASCADE, default = 1, null=True, blank= True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT, default='1')
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_active = models.DateTimeField(verbose_name='Data Última Activação', blank=True, null=True)
    last_inactive = models.DateTimeField(verbose_name='Data Última Inactivação', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
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
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team_leader.username}'

class Teams(models.Model):
    team_leader = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team_leader.team_leader.username} - {self.team_member.username}'







class StatusCode(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=2, verbose_name='Código Status', validators=[only_int])
    name = models.CharField(max_length=50)

    @staticmethod
    def get_default():
        default_code = '10'
        default_name = 'Aberto'
        default_status = StatusCode.objects.filter(code=default_code, name=default_name).first()
        if not default_status:
            default_status = StatusCode.objects.create(code=default_code, name=default_name)
        return default_status.code

    def __str__(self):
        return f'{self.code} - {self.name}'


class StatusConfig(models.Model):
    LEAD = 'LEAD'
    PROSPECT = 'PROSPECT'
    TYPE_CHOICES = [
        (LEAD, 'Lead'),
        (PROSPECT, 'Prospect'),
    ]
    config = models.ForeignKey(MasterConfig, on_delete=models.CASCADE)
    status_type = models.CharField(verbose_name='Tipo Status', max_length=20, choices=TYPE_CHOICES)
    status_code = models.ForeignKey(StatusCode, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=7, blank=True, null=True)
    icon = models.ImageField(upload_to='status_icons', blank=True, null=True)
    tooltip = models.CharField(max_length=150, blank=True, null=True)
    notes = models.TextField(verbose_name='Notas', blank=True, null=True)

    def __str__(self):
        return f'{self.status_code}/{self.status_type} - Config: {self.config.short_desc}'


class WorkflowConfig(models.Model):
    LEAD_VENDA = 'LEAD-VENDA'
    LEAD_COMPRA = 'LEAD-COMPRA'
    PROSPECT_VENDA = 'PROSPECT-VENDA'
    PROSPECT_COMPRA = 'PROSPECT-COMPRA'
    TYPE_CHOICES = [
        (LEAD_VENDA, 'Lead - Venda'),
        (LEAD_COMPRA, 'Lead - Compra'),
        (PROSPECT_VENDA, 'Prospect - Venda'),
        (PROSPECT_COMPRA, 'Prospect - Compra'),
    ]
    config = models.ForeignKey(MasterConfig, on_delete=models.CASCADE)
    workflow_type = models.CharField(verbose_name='Tipo Workflow', max_length=20, choices=TYPE_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    start_status = models.ForeignKey(StatusCode, on_delete=models.CASCADE, related_name='start_status', verbose_name='Estado Inicial')
    end_status = models.ForeignKey(StatusCode, on_delete=models.CASCADE, related_name='end_status', verbose_name='Estado Final')
    available_if = models.ForeignKey(StatusCode, on_delete=models.CASCADE, related_name='available_if', verbose_name='Disponível se', blank=True, null=True)
