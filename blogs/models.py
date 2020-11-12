from django.db import models
from django.conf import settings
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, unique=True)
	image = models.ImageField(upload_to='images/')
	content = models.TextField()
	tags = TaggableManager()
	date_created = models.DateField(auto_now_add=True)
	time_created = models.TimeField(auto_now_add=True)
	slug = models.SlugField(null=True, blank=True)

	class Meta:
		ordering = ['-time_created']

	def __str__(self):
		return self.title.title()

	def get_absolute_url(self):
		from django.shortcuts import reverse
		return reverse('blogs:blog_detail', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		if self.slug is None and self.title:
			self.slug = slugify(self.title)
		return super(Blog, self).save(args, kwargs)


class Reply(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_created = models.DateField(auto_now_add=True)
	time_created = models.TimeField(auto_now_add=True)
	comment = models.TextField()

	class Meta:
		verbose_name_plural = 'Replies'

	def __str__(self):
		return str(self.commenter.username.capitalize())
