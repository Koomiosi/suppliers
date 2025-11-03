from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Supplier, Product, Customer
from django.contrib.auth import authenticate, login, logout
import json, random, string
from django.db.models import F



#Landing after login

def landingview(request):
    return render(request, 'landingpage.html')

# Login and logout

def loginview(request):
    return render(request, 'loginpage.html')

def loginaction(request):
    user = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=user, password=password)
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')
    
def logoutaction(request):
    logout(request)
    return render(request, 'loginpage.html')

# Product views

def productslistview(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
        
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render(request, 'productslist.html', context)
        

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
        Product(productname=a, packagesize=b, unitprice=c, unitsinstock=d, supplier=Supplier.objects.get(id=e)).save()
        return redirect(request.META['HTTP_REFERER'])
        

def deleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:  
        Product.objects.get(id=id).delete()
        return redirect('productslistview')

def confirmdeleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'confirmdelprod.html', context)

def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'edit_product.html', context)

def edit_product_post(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        item = Product.objects.get(id=id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect('productslistview')

def products_filtered(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        productlist = Product.objects.all()
        filteredproducts = productlist.filter(supplier=id)
        context = {'products': filteredproducts}
        return render(request, 'productslist.html', context)

# Suppliers views

def supplierslistview(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render(request, 'supplierslist.html', context)

def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def searchsupplier(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Supplier.objects.filter(companyname__icontains=search)
        context = {'suppliers': filtered}
        return render(request, 'supplierslist.html', context)
    
# Customers views

def customerslistview(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        customerlist = Customer.objects.all()
        context = {'customers': customerlist}
        return render(request, 'customers.html', context)

def addcustomer(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')

    if request.method == 'POST':
        a = request.POST.get('customerfname', '').strip()
        b = request.POST.get('customerlname', '').strip()
        c = request.POST.get('address', '').strip()
        d = request.POST.get('phone', '').strip()
        e = request.POST.get('email', '').strip()
        f = request.POST.get('country', '').strip()

        # Varmistetaan että etunimi ja sukunimi on annettu
        if a and b:
            Customer.objects.create(
                customerfname=a,
                customerlname=b,
                address=c,
                phone=d,
                email=e,
                country=f
            )

        # Palautetaan aina takaisin samaan sivuun
        return redirect(request.META.get('HTTP_REFERER', 'customerslistview'))

    # Jos joku menee suoraan /add-customer/ osoitteeseen ilman POST:ia
    return redirect('customerslistview')
    
def searchcustomer(request):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Customer.objects.filter(companyname__icontains=search)
        context = {'customers': filtered}
        return render(request, 'customers.html', context)
    
def deletecustomer(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:  
        Customer.objects.get(id=id).delete()
        return redirect('customerslistview')

def confirmdeletecustomer(request, id):
    if not request.user.is_authenticated:
        return render(request,'loginpage.html')
    else:
        customer = Customer.objects.get(id=id)
        context = {'customer': customer}
        return render(request, 'confirmdelcust.html', context)
    
# Orders views
def order_list(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')

    # Superuser näkee kaikki tilaukset, muut vain omansa
    if request.user.is_superuser:
        orders = Order.objects.select_related('product__supplier', 'customer', 'user').all()
    else:
        orders = Order.objects.select_related('product__supplier', 'customer', 'user').filter(user=request.user)

    suppliers = Supplier.objects.all()
    products = Product.objects.all()

    # Muutetaan tuotteet JSONiksi (Decimal -> float)
    products_json = json.dumps([
        {
            'id': p.id,
            'productname': p.productname,
            'packagesize': p.packagesize,
            'unitprice': float(p.unitprice),
            'unitsinstock': p.unitsinstock,
            'supplier_id': p.supplier_id
        } for p in products
    ])

    context = {
        'orders': orders,
        'suppliers': suppliers,
        'products_json': products_json,
    }

    return render(request, 'orders.html', context)

def addorder(request, customer_id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')

    customer = get_object_or_404(Customer, id=customer_id)
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id)
        ordernumber = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        # Varmistetaan, että varastossa on tarpeeksi
        if product.unitsinstock < quantity:
            messages.error(request, "Not enough units in stock!")
            return redirect('addorder', customer_id=customer.id)

        Order.objects.create(
            ordernumber=ordernumber,
            customer=customer,
            product=product,
            quantity=quantity,
            unitprice=product.unitprice,
            user=request.user
        )

        # Päivitetään varastosaldo
        product.unitsinstock -= quantity
        product.save()

        return redirect('customer_orders', customer_id=customer.id)

    return render(request, 'add-order.html', {
        'customer': customer,
        'products': products,
    })


def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('customer_orders', customer_id=order.customer.id)

    if request.method == 'POST':
        order.delete()
        return redirect('customer_orders', customer_id=order.customer.id)

    return render(request, 'confirmdeleteorder.html', {'order': order})

def customer_orders(request, customer_id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')

    customer = get_object_or_404(Customer, id=customer_id)
    orders = Order.objects.filter(customer=customer)

    return render(request, 'customer_orders.html', {
        'customer': customer,
        'orders': orders
    })