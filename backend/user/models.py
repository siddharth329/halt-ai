from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.admin import ModelAdmin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
FULL_USER_PROFILE = [
    'name',
    'email',
    'slug',
    'profile_image',
    'user_type'
]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('user_type', 2)

        self.create_user(email=email, name=name, password=password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = [
        (0, 'REGULAR_USER'),
        (1, 'ADMIN'),
        (2, 'SUPER_ADMIN')
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.IntegerField(default=0, choices=USER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class UserAdmin(ModelAdmin):
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('is_staff', '-created_at')
    list_display = ('email', 'name', 'user_type', 'is_active', 'is_staff')
    fieldsets = (
        ('Required', {'fields': ('email', 'name', 'password')}),
        ('About', {'fields': [
            'slug',
            'profile_image',
        ]}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_permissions', 'groups')}),
        ('App Level Critical', {'fields': ('user_type', 'is_superuser')}),
        ('Metrics', {'fields': ('last_login', 'created_at', 'updated_at')})
    )
    readonly_fields = ('last_login', 'created_at', 'updated_at')
