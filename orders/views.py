from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer
from django.db.models import Sum


# Список всех заказов
def order_list(request):
    orders = Order.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        orders = orders.filter(table_number__icontains=search_query) | \
                 orders.filter(status__icontains=search_query)
    return render(request, 'orders_list.html', {'orders': orders})


# Создание заказа
def order_create(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        items = request.POST.getlist('items[]')
        prices = request.POST.getlist('prices[]')
        quantities = request.POST.getlist('quantities[]')

        if not table_number or not items:
            messages.error(request, 'Заполните все обязательные поля!')
            return render(request, 'order_create.html')

        try:
            order = Order.objects.create(table_number=table_number)
            for item_name, price, qty in zip(items, prices, quantities):
                if item_name and float(price) >= 0 and int(qty) > 0:
                    OrderItem.objects.create(
                        order=order,
                        item_name=item_name,
                        price=float(price),
                        quantity=int(qty)
                    )
            order.total_price = order.calculate_total()
            order.save()
            messages.success(request, 'Заказ успешно создан!')
            return redirect('order_list')
        except ValueError:
            messages.error(request, 'Некорректные данные!')
            return render(request, 'order_create.html')

    return render(request, 'order_create.html')


# Обновление заказа
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['pending', 'ready', 'paid']:
            order.status = status
            order.save()
            messages.success(request, 'Статус заказа обновлен!')
            return redirect('order_list')
        else:
            messages.error(request, 'Некорректный статус!')

    return render(request, 'order_update.html', {'order': order})


# Удаление заказа
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Заказ успешно удален!')
        return redirect('order_list')
    return render(request, 'order_list.html', {'orders': Order.objects.all()})


# Отчет по выручке
def revenue_report(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = paid_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
    return render(request, 'revenue.html', {
        'paid_orders': paid_orders,
        'total_revenue': total_revenue
    })


# REST API для списка заказов
class OrderListAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer