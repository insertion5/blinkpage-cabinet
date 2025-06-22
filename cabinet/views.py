from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Service, Comment
from .forms import OrderForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def dashboard(request):
    return redirect('order_list')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cabinet/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    comments = Comment.objects.filter(order=order).order_by('created_at')
    return render(request, 'cabinet/order_detail.html', {'order': order, 'comments': comments})

@login_required
def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'cabinet/new_order.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'cabinet/profile.html')

@login_required
def support(request):
    return render(request, 'cabinet/support.html')

@csrf_exempt
def tilda_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        site_type = data.get('site_type')
        services = data.get('services', [])
        total_price = data.get('price', 0)

        from django.contrib.auth import get_user_model
        User = get_user_model()
        user, created = User.objects.get_or_create(email=email)
        order = Order.objects.create(user=user, site_type=site_type, total_price=total_price)
        for service_name in services:
            service = Service.objects.filter(name=service_name).first()
            if service:
                order.services.add(service)

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
