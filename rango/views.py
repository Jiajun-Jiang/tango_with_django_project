from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
def index(request):
    category_list= Category.objects.order_by('-likes')[:5]
    context_dict={}
    context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']=category_list
    return render(request,'rango/index.html',context=context_dict)
    #return HttpResponse("Rango says hey there partner!(<a href='/rango/about/'>About</a>)")
def about(request):
    your_name={'your_name':'Jiajun'}
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a> .")
    return render(request,'rango/about.html',your_name)

def show_category(request, category_name_slug):
    context_dict={}

    try:
        category= Category.objects.get(slug=category_name_slug)
        pages=Page.objects.filter(category=category)
        context_dict['pages']= pages
        context_dict['category']=category
    except:
        context_dict['pages']= None
        context_dict['category']=None
    return render(request,'rango/category.html', context=context_dict)