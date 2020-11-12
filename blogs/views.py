from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Blog, Reply
from .forms import ReplyForm
# Create your views here.

def blog_list(request):
	qs = Blog.objects.all()
	paginator = Paginator(qs, 4)
	page_number = request.GET.get('page')
	qs = paginator.get_page(page_number)
	name = 'blog.html'
	context = {
	'blogs' : qs
	}
	return render(request, name, context)

def blog_detail(request, slug):
	qs = Blog.objects.get(slug=slug)
	query = Reply.objects.filter(blog=qs)
	form = ReplyForm(request.POST or None)
	if form.is_valid():
		reply = form.save(commit=False)
		reply.commenter = request.user
		reply.blog = qs
		reply.save()
		return redirect('blogs:blog_detail', slug=qs.slug)
	name = 'blog-single.html'
	context = {
	'blog' : qs,
	'replies' : query,
	'form':form
	}
	return render(request, name, context)