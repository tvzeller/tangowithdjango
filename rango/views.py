from django.shortcuts import render
from django.http import HttpResponse
#import the Category model
from rango.models import Category
from rango.models import Page

def index(request):
	# query the database for a list of all categories currently stored
	# order the categories by number of likes in descending order
	# retrieve the top 5 only - or all if less than 5
	# place the list in our context_dict dictionary which will be passed to the template engine
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	#render the response and send it back
	return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
	#create a context dictionary which we can pass to the template rendering engine
	context_dict = {}

	try:
		#can we find a category name slug with the given name?
		# if we can't, the .get() method raises a doesnotexist exception
		# so the .get() method returns one model instance or raises an exception
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		#retrieve all of the associated pages
		# note that filter returns >= 1 model instance
		pages = Page.objects.filter(category=category)

		#add our results list to the template context under name pages
		context_dict['pages'] = pages
		#we also add the category object from the database to the context dictionary
		#we'll use this in the template to verify that the category exists
		context_dict['category'] = category
	except Category.DoesNotExist:
		#we get here if we didn't find the specified category
		#don't do anything - the template displays the "no category" message for us
		pass

	#render response and return to client
	return render(request, 'rango/category.html', context_dict)

#def about(request):
#	return HttpResponse("Rango says here is the about page <br/> <a href = '/rango'>Main Page</a>")

def about(request):
	context_dict = {'testmessage': "new insect overlords"}
	return render(request, 'rango/about.html', context_dict)