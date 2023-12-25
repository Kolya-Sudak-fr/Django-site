from django.contrib import admin
from .models import YogaClass, User, Student, Teacher

admin.site.register(YogaClass)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)