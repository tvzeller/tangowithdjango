from django.contrib import admin
from rango.models import Category, Page

# add in this class to customise the admin interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
