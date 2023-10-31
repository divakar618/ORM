# Ex02 Django ORM Web Application
## Date: 07/10/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```python
Admin.py

from django.contrib import admin
from .models import student,studentAdmin
admin.site.register(student,studentAdmin)

model.py

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

```

## OUTPUT

![Alt text](<Screenshot 2023-10-31 140011.png>)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
