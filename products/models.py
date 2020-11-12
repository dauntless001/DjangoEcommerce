from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

condition = (
	('New', 'New'),
	('Hot', 'Used')
	)

class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)
	class Meta:
		verbose_name_plural ='Categories'


	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=50, unique=True)
	condition = models.CharField(max_length=20, choices=condition)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	brand = models.CharField(max_length=20)
	details = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	tags = TaggableManager()
	image = models.ImageField(upload_to='images/')
	image_one = models.ImageField(upload_to='images/', null=True, blank=True)
	image_two = models.ImageField(upload_to='images/', null=True, blank=True)
	image_three = models.ImageField(upload_to='images/', null=True,blank=True)
	slug = models.SlugField(null=True, blank=True)

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products:products_details', kwargs={'slug':self.slug})


	def save(self, *args, **kwargs):
		if self.slug is None and self.name:
			self.slug = slugify(self.name[:15] + str(timezone.now())[11:])[:50]
		return super(Product, self).save(args, kwargs)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.amount

    # def get_total(self):
    # 	total = 0
    # 	for a in self.item.all():
    # 		total += a.get_total_item_price()


class Review(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	review = models.TextField()
	time_created = models.TimeField(auto_now_add=True)
	date_created = models.DateField(auto_now_add=True)
	

	def __str__(self):
		return self.reviewer


class Wishlist(models.Model):
	wisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)


	def __str__(self):
		return str(self.wisher.username.capitalize())



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    postal_code = models.IntegerField()
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    ship_to_billing = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
    	return self.user.username

    def get_absolute_url(self):
    	return reverse('products:order', kwargs={'slug', self.slug})

    def save(self, *args, **kwargs):
    	if self.slug is None and self.user.username:
    		self.slug = slugify(str(self.user.username)+str(self.ordered_date))
    	return super(Order, self).save(args, kwargs)




