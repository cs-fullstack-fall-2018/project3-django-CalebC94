from django.shortcuts import render
from .models import Expenses
from django.contrib.auth.decorators import login_required



def expense_list(request):
    expense_list = Expenses.objects.all()
    context = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html', context)

@login_required
def userexpense(request):
    expense_list = Expenses.objects.filter(user=request.user)
    context = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html', context)