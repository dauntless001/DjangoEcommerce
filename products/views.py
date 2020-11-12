from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Review, Wishlist, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ReviewForm, OrderForm
# Create your views here.
def home_view(request):
	qs = Product.objects.all()[:12]
	wishlists = []
	try:
		wishlist = Wishlist.objects.filter(wisher=request.user)
		for wish in wishlist:
			product_name = wish.product.name
			wishlists.append(product_name)
	except:
		pass
	name = 'index.html'
	context = {
	'products' : qs,
	'wishlists':wishlists
	}
	return render(request, name, context)


def search_view(request):
	search = request.GET.get('q')
	print(search)
	qs = Product.objects.filter(
		Q(name__icontains=search)| Q(name__iexact=search)|
		Q(details__icontains=search)
		)
	wishlists = []
	try:
		wishlist = Wishlist.objects.filter(wisher=request.user)
		for wish in wishlist:
			product_name = wish.product.name
			wishlists.append(product_name)
	except:
		pass
	paginator = Paginator(qs, 12)
	page_number = request.GET.get('page')
	qs = paginator.get_page(page_number)
	name = 'shop.html'
	context = {
	'products' : qs,
	'wishlists':wishlists,
	'search' : search
	}
	return render(request, name, context)


def product_list(request):
	qs = Product.objects.all()
	wishlists = []
	try:
		wishlist = Wishlist.objects.filter(wisher=request.user)
		for wish in wishlist:
			product_name = wish.product.name
			wishlists.append(product_name)
	except:
		pass
	paginator = Paginator(qs, 12)
	page_number = request.GET.get('page')
	qs = paginator.get_page(page_number)
	name = 'shop.html'
	context = {
	'products' : qs,
	'wishlists':wishlists
	}
	return render(request, name, context)


def product_detail(request, slug):
	qs = Product.objects.get(slug=slug)
	cart = OrderItem.objects.filter(user=request.user)
	cart_added = False
	for a in cart:
		if a.item.name == qs.name:
			cart_added = True
	review = Review.objects.filter(product=qs)
	form = ReviewForm(request.POST or None)
	if form.is_valid():
		review = form.save(commit=False)
		review.product = qs
		review.reviewer = request.user
		review.save()
		return redirect('products:products_details', slug=qs.slug)
	name = 'product-details.html'
	context = {
	'product':qs,
	'review' : review,
	'form' : form,
	'cart_added':cart_added
	}
	return render(request, name, context)



@login_required(login_url='/accounts/login')
def add_to_wishlist(request, slug):
	qs = Product.objects.get(slug=slug)
	Wishlist.objects.create(
		wisher=request.user,
		product=qs)
	print('Added')
	messages.success(request, 'Product Added to Wishlist Successfully')
	return redirect('products:products_list')


@login_required(login_url='/accounts/login')
def remove_from_wishlist(request, slug):
	qs = Product.objects.get(slug=slug)
	wish = Wishlist.objects.get(product=qs)
	wish.delete()
	print('Deleted')
	messages.success(request, 'Product Deleted from Wishlist Successfully')
	return redirect('products:products_list')


@login_required(login_url='/accounts/login')
def wishlist_view(request):
	qs = Wishlist.objects.filter(wisher=request.user)
	name = 'wishlist.html'
	context = {
	'wishes' : qs
	}
	return render(request, name, context)


def contact_view(request):
	name = 'contact-us.html'
	return render(request, name)


@login_required(login_url='/accounts/login')
def add_to_cart_view(request, slug):
	if request.method == 'POST':
		quantity = request.POST['quantity']
		product = request.POST['product']
		item = Product.objects.get(name=product)
		orderitem = OrderItem.objects.create(
			user = request.user,
			item = item,
			quantity = quantity
			)
		messages.success(request, 'Item Addded Successfully')
		return redirect('products:products_details', item.slug)


@login_required(login_url='/accounts/login')
def remove_from_cart_view(request, id):
	qs = OrderItem.objects.get(id=id)
	if qs:
		qs.delete()
		messages.success(request, 'Item Removed Successfully')
		return redirect('products:cart')


@login_required(login_url='/accounts/login')
def cart(request):
	qs = OrderItem.objects.filter(user=request.user)
	total_amount = 0
	for item in qs:
		total_amount +=(item.item.amount*item.quantity)
	name = 'cart.html'
	context = {
	'cart':qs,
	'total_amount':total_amount
	}
	return render(request, name, context)

@login_required(login_url='/accounts/login')
def checkout(request):
	qs = OrderItem.objects.filter(user=request.user)
	total_amount = 0
	for item in qs:
		total_amount +=(item.item.amount*item.quantity)
	form = OrderForm(request.POST or None)
	if form.is_valid():
		print(form, 'jghhjghghjghjghjg')
		# order = form.save(commit=False)
		# order.user = request.user
		# order.items = OrderItem.objects.filter(user=request.user)
		# order.save()
		# return redirect('products:checkout_final', order.slug)
	name = 'checkout.html'
	context = {
	'form' : form,
	'cart':qs,
	'total_amount':total_amount
	}
	return render(request, name, context)




