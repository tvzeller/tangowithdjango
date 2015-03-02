import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category, Page


# Delete Categories
print "Categories: {} instances were detected".format(Category.objects.all().count())
Category.objects.all().delete()
print "Categories: {} instances remain".format(Category.objects.all().count())

# Delete Sessions
print "Pages: {} instances were detected".format(Page.objects.all().count())
Page.objects.all().delete()
print "Sessions: {} instances remain".format(Page.objects.all().count())

