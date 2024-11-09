from django.contrib import admin

from django.contrib import admin
from .models import Profile, Couple


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fecha_nacimiento', 'foto']

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ['novio', 'novia', 'aniversario', 'foto']

