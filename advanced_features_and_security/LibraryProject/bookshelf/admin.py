from .models import Book, CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show in list view
    list_filter = ('publication_year',)                     # Filter by year
    search_fields = ('title', 'author')                     # Search by title or author

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'date_of_birth', 'is_staff']  # Removed 'username'
    ordering = ['email']                                   # Set to 'email' instead of 'username'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)
