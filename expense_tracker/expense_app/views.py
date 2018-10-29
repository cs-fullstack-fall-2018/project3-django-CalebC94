from django.shortcuts import render
from .forms import Transaction
from .models import Expenses
from django.contrib.auth.decorators import login_required

def create_expense(request):
    print("create expense")
    form = Transaction(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'expense_app/index.html', context)

def expense_list(request):
    expense_list = Expenses.objects.all()
    context = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html', context)

@login_required
def userexpense(request):
    expense_list = Expenses.objects.filter(user=request.user)
    context = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html', context)