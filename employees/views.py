from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render 
from employees.models import Employee

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_details.html')

    # return HttpResponse(employee)
    
    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404