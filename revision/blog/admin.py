from django.contrib import admin
from .models import m_ki_c_Admin

@admin.register(m_ki_c_Admin)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('name', 'age','age', )