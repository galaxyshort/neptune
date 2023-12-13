from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField(max_length=10)
    age = models.CharField(max_length=5)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=15, choices=gender_choices)
    phone_Number = models.CharField(max_length=15)
    mail_id = models.EmailField(max_length=50)
    address = models.TextField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose_choices = [
        ('enquiry', 'Enquiry'),
        ('return', 'Return'),
        ('place_order', 'Place_order'),
        ('FAQ', 'FAQ'),
        ('other', 'Other'),
    ]

    purpose = models.CharField(max_length=20, choices=purpose_choices)

    def __str__(self):
        return self.first_name
