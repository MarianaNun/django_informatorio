from django.contrib import admin

# Register your models here.

from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'disponible')



admin.site.register(Libro, LibroAdmin)

