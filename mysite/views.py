
from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee # Import your Employee model


def home(request):
    employees = Employee.objects.all()  # Assuming you have an Employee model
    # print(employees)
    context = {
        'employees' : employees,
    }
    return render(request, "home.html", context) # Render the home.html template with the context