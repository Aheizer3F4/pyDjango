from django.shortcuts import render

def home(request):
    return render(request, 'expense/home.html')

def expense_list(request):
    # Example data for expenses (you could replace this with a database query later)
    expenses = [
        {'name': 'Groceries', 'amount': 150},
        {'name': 'Utilities', 'amount': 80},
        {'name': 'Internet', 'amount': 60},
        {'name': 'Rent', 'amount': 1000},
    ]

    # Calculate total expenses
    total_expenses = sum(expense['amount'] for expense in expenses)

    # Pass the expenses and total to the template
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses
    }

    return render(request, 'expense/expense_list.html', context)

def about(request):
    return render(request, 'expense/about.html')
