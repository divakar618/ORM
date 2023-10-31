from django.db import models
from django.contrib import admin
class student (models.Model):
    eid=models.CharField(max_length=20, help_text="student ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class studentAdmin(admin.ModelAdmin):
    list_display=('eid', 'name', 'salary', 'age', 'email')