# Python
from typing import Any
import uuid

# Django
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import (
    HttpResponse, 
    HttpResponseRedirect
)
from django.shortcuts import render
from django.core.mail import send_mail

# Local
from .models import (
    Product,
    Genre,
    Discounts
)
from .forms import ReservationForm


class ProductView(View):
    
    template_name: str = 'main/index.html'

    def get(self, request: WSGIRequest) -> HttpResponse:
        form = ReservationForm()
        #----------ALL PRODUCTS----------
        products: QuerySet[Product] = Product.objects.all().order_by('id')
        #----------ALL PRODUCTS BY GENRE----------
        breakfast: QuerySet[Product] = Product.objects.filter(genres=1)
        pizza: QuerySet[Product] = Product.objects.filter(genres=2)
        burger: QuerySet[Product] = Product.objects.filter(genres=3)
        first_dish: QuerySet[Product] = Product.objects.filter(genres=4)
        pasts: QuerySet[Product] = Product.objects.filter(genres=5)
        salad: QuerySet[Product] = Product.objects.filter(genres=7)
        waffles: QuerySet[Product] = Product.objects.filter(genres=8)
        snacks: QuerySet[Product] = Product.objects.filter(genres=9)
        desserts: QuerySet[Product] = Product.objects.filter(genres=10)
        cold_drinks: QuerySet[Product] = Product.objects.filter(genres=11)
        coffee: QuerySet[Product] = Product.objects.filter(genres=12)
        #----------COUNT PRODUCTS----------
        breakfast_count: QuerySet[Product] = Product.objects.filter(genres=1).count()
        snacks_count: QuerySet[Product] = Product.objects.filter(genres=9).count()
        coffee_count: QuerySet[Product] = Product.objects.filter(genres=12).count()
        all_products_count: QuerySet[Product] = Product.objects.count()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'products': products,
                
                'breakfast': breakfast,
                'pizza': pizza,
                'burger': burger,
                'first_dish': first_dish,
                'pasts': pasts,
                'salad': salad,
                'waffles': waffles,
                'snacks': snacks,
                'desserts': desserts,
                'cold_drinks': cold_drinks,
                'coffee': coffee,

                'breakfast_count': breakfast_count,
                'snacks_count': snacks_count,
                'coffee_count': coffee_count,
                'all_products_count': all_products_count,

                'form':form
            }
        )
    
    def post(self, request: WSGIRequest) -> HttpResponse:
        form = ReservationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            sender = form.cleaned_data['sender']
            phone_number = form.cleaned_data['phone_number']
            how_many_person = form.cleaned_data['how_many_person']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']

            recipients = ["venums46@gmail.com"]
            subject = "New Reservation"
            email_message = f'''
                Имя: {full_name}\n
                Номер телефона: {phone_number}\n
                {how_many_person} человек\n
                Дата резерва: {date} | в {time}
                Сообщение:\n 
                {message}
            '''
            try:
                send_mail(subject, email_message, sender, recipients)
                return HttpResponseRedirect('')
            
            except Exception as e:
                return HttpResponse("Произошла ошибка при отправке письма.")

        return render(request, self.template_name, {'form': form})
    
