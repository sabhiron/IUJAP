from django.contrib import admin

# Register your models here.

from .models import Student, Section, Year, Branch , Subject

admin.site.register(Student)
admin.site.register(Section)
admin.site.register(Year)
admin.site.register(Branch)
admin.site.register(Subject)
