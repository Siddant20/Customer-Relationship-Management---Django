from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
    orders= Order.objects.all()
    customers= Customer.objects.all()
    total_customers= customers.count()
    total_orders = orders.count()
    delivered= orders.filter(status = 'Delivered').count()
    pending=orders.filter(status = "Pending").count()
    context = {'orders': orders, 'customers':customers, 'total_customers' : total_customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, "accounts/dashboard.html", context)

def products(request):
    products=Product.objects.all()
    return render(request, "accounts/products.html",{'products': products})

def customer(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    orders = customer.order_set.all()
    context = {'customer':customer, 'orders': orders}
    return render(request,"accounts/customer.html", context)

def createOrder(request, cust_id):
    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product','status'), extra=3)
    customer=Customer.objects.get(id=cust_id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, order_id):
    order= Order.objects.get(id=order_id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, order_id):
    order= Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context )