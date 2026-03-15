from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ('name','email','phone','city')

    search_fields = ('name','email')

    list_filter = ('city',)

    list_per_page = 5   # Pagination

admin.site.register(User, UserAdmin)