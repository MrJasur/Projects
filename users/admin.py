from pyexpat import model
from django.contrib import admin
from .models import CustomUserModel

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')

admin.site.register(CustomUserModel, UserAdmin)