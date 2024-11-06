from django.shortcuts import render , get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(req):
    return render(req, "cart/cart_summary.html",{})

def cart_add(req):
    cart = Cart(req)
    # test for post
    if req.POST.get('action') == 'post':
        #Get the product id
        product_id = int(req.POST.get('productid'))
        # lookup product in db
        product = get_object_or_404(Product, id=product_id)
        # add product to cart
        cart.add(product=product)
        # Get Cart quantity
        cart_quantity = cart.__len__()
        # return response
        # response = JsonResponse({'Product added':product.name})
        response = JsonResponse({'qty':cart_quantity})
        return response    

def cart_delete(req):
    pass

def cart_update(req):
    pass

