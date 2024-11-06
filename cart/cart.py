class Cart():
    def __init__(self,req):
        self.session = req.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in req.session:
            cart = self.session['session_key'] = {}
            
            
        self.cart = cart
        
    def add(self, product):
        product_id = str(product.id)
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        self.session.modified = True
    def __len__(self):
        return len(self.cart)