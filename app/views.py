from django.shortcuts import render, redirect
from .models import Supplier, Product, Customer
from django.contrib.auth import authenticate, login, logout

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
        return render(request,'loginpage.html')
    else:
        a = request.POST['customerfname']
        b = request.POST['customerlname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Customer(customerfname = a, customerlname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])
    
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