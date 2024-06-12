from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'skin_care_hair_care', 'brand', 'teens', "twenties", "thirties", "forties", "fifties", "sixties",
        'skin_type_normal', 'oily', 'dry', 'sensitive', 'combination', 'skin_concerns_acne', 'aging',
        'dull_skin', 'elasticity', 'hydration', 'pigmentation', 'pores', 'redness', 'scarring',
        'sensitive_skin', 'sun_protection', 'texture', 'uneven_skin_tone', 'body_care',
        'eye_cream', 'cleanser', 'exfoliant', 'microneedling', 'moisturizer', 'peels', 'serums',
        'sun_screen', 'spot_treatment', 'toner', 'use_sunscreen_daily', 'react_to_sun_exposure', 'hair_loss'
    )
    list_filter = (
        'skin_care_hair_care', 'brand', 'teens', "twenties", "thirties", "forties", "fifties", "sixties",
        'skin_type_normal', 'oily', 'dry', 'sensitive', 'combination', 'skin_concerns_acne', 'aging',
        'dull_skin', 'elasticity', 'hydration', 'pigmentation', 'pores', 'redness', 'scarring',
        'sensitive_skin', 'sun_protection', 'texture', 'uneven_skin_tone', 'body_care',
        'eye_cream', 'cleanser', 'exfoliant', 'microneedling', 'moisturizer', 'peels', 'serums',
        'sun_screen', 'spot_treatment', 'toner', 'use_sunscreen_daily', 'react_to_sun_exposure', 'hair_loss'
    )
    search_fields = ('product_name', 'brand')

# Optionally, you can customize how the form looks by using fieldsets
# fieldsets = (
#     (None, {
#         'fields': ('product_name', 'skin_care_hair_care', 'brand')
#     }),
#     ('Age Groups', {
#         'fields': ('teens', "twenties", "thirties", "forties", "fifties", "sixties")
#     }),
#     # Add more fieldsets as necessary
# )