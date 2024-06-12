from django.shortcuts import render
# app/views.py
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Product

def product_list(request):
    products = Product.objects.all()
    product_count = Product.objects.count()
    print(products)
    print(product_count)
    return HttpResponse("Hello, World!")

# app/views.py

from django.shortcuts import render
from .models import Product

def filter_products(request):
    if request.method == 'POST':
        filter_criteria = {}
        # Add filter criteria based on form data
        if request.POST.get('teens'):
            filter_criteria['teens'] = True
        if request.POST.get('twenties'):
            filter_criteria['twenties'] = True
           
        if request.POST.get('thirties'):
            filter_criteria['thirties'] = True
        if request.POST.get('forties'):
            filter_criteria['forties'] = True
        if request.POST.get('fifties'):
            filter_criteria['fifties'] = True
        if request.POST.get('sixties'):
            filter_criteria['sixties'] = True
        if request.POST.get('skin_type_normal'):
            filter_criteria['skin_type_normal'] = True
        if request.POST.get('oily'):
            filter_criteria['oily'] = True
        if request.POST.get('dry'):
            filter_criteria['dry'] = True
        if request.POST.get('sensitive'):
            filter_criteria['sensitive'] = True
        if request.POST.get('combination'):
            filter_criteria['combination'] = True
        if request.POST.get('skin_concerns_acne'):
            filter_criteria['skin_concerns_acne'] = True
        if request.POST.get('aging'):
            filter_criteria['aging'] = True
        if request.POST.get('dull_skin'):
            filter_criteria['dull_skin'] = True
        if request.POST.get('elasticity'):
            filter_criteria['elasticity'] = True
        if request.POST.get('hydration'):
            filter_criteria['hydration'] = True
        if request.POST.get('pigmentation'):
            filter_criteria['pigmentation'] = True
        if request.POST.get('pores'):
            filter_criteria['pores'] = True
        if request.POST.get('redness'):
            filter_criteria['redness'] = True
        if request.POST.get('scarring'):
            filter_criteria['scarring'] = True
        if request.POST.get('sensitive_skin'):
            filter_criteria['sensitive_skin'] = True
        if request.POST.get('sun_protection'):
            filter_criteria['sun_protection'] = True
        if request.POST.get('texture'):
            filter_criteria['texture'] = True
        if request.POST.get('uneven_skin_tone'):
            filter_criteria['uneven_skin_tone'] = True
        if request.POST.get('body_care'):
            filter_criteria['body_care'] = True
        if request.POST.get('eye_cream'):
            filter_criteria['eye_cream'] = True
        if request.POST.get('cleanser'):
            filter_criteria['cleanser'] = True
        if request.POST.get('exfoliant'):
            filter_criteria['exfoliant'] = True
        if request.POST.get('microneedling'):
            filter_criteria['microneedling'] = True
        if request.POST.get('moisturizer'):
            filter_criteria['moisturizer'] = True
        if request.POST.get('peels'):
            filter_criteria['peels'] = True
        if request.POST.get('serums'):
            filter_criteria['serums'] = True
        if request.POST.get('sun_screen'):
            filter_criteria['sun_screen'] = True
        if request.POST.get('spot_treatment'):
            filter_criteria['spot_treatment'] = True
        if request.POST.get('toner'):
            filter_criteria['toner'] = True
        if request.POST.get('use_sunscreen_daily'):
            filter_criteria['use_sunscreen_daily'] = True
        if request.POST.get('react_to_sun_exposure'):
            filter_criteria['react_to_sun_exposure'] = True
        if request.POST.get('hair_loss'):
            filter_criteria['hair_loss'] = True

        # Filter products based on the criteria
        products = Product.objects.filter(**filter_criteria)
    else:
        products = Product.objects.all()
        print('none')

    # Counting the number of products that match the criteria
    product_count = products.count()

    # Returning the filtered products and the count to the template
    return render(request, 'product_list.html', {'products': products, 'product_count': product_count})



