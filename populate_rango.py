import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages=[
        {"title": "Official Python Tutorial",
        "url":"http://docs.python.org/3/tutorial/",
         "views":128,
         "likes":64},
    {"title": "How to Think like a Computer Scientist",
     "url": "http://www.greenteapress.com/thinkpython/",
     "views": 128,
     "likes": 64
     },
    {"title": "Learn Python in 10 Minutes",
    "url": "http://www.korokithakis.net/tutorials/python/",
     "views": 128,
     "likes": 64
     }
    ]


    django_pages = [
         {"title": "Official Django Tutorial",
            "url":"https://docs.djangoproject.com/en/2.1/intro/tutorial01/",
          "views": 64,
          "likes": 32
          },
    {"title": "Django Rocks",
    "url": "http://www.djangorocks.com/",
     "views": 64,
     "likes": 32
     },

    {"title": "How to Tango with Django",
      "url": "http://www.tangowithdjango.com/",
     "views": 64,
     "likes": 32
     }]

    other_pages = [
        {"title": "Bottle",
            "url":"http://bottlepy.org/docs/dev/",
         "views": 32,
         "likes": 16
         },
    {"title": "Flask",
      "url": "http://flask.pocoo.org",
     "views": 32,
     "likes": 16
     }]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
    "Other Frameworks": {"pages": other_pages}}
    for cat, cat_data in cats.items():
        c=add_cat(cat,cat_data["pages"][0]["views"],cat_data["pages"][0]["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} - {1}".format(str(c),str(p)))
def add_page(cat, title, url , views=10):
    p=Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
def add_cat (name,views,likes):
    c= Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes = likes
    c.save()
    return c
if __name__=="__main__":
    print("starting")
    populate()