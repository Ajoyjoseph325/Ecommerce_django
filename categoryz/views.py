
from unicodedata import category, name
from django.shortcuts import render,get_object_or_404
from django.db . models import Q
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        print("c_page value ===>",c_page)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
    cat_list=categ.objects.all()
    paginator=Paginator(prodt,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'products':prodt,'category':cat_list,'pg':pro,'catname':c_page})
def proddetails(request,c_slug,product_slug):
    try:
        prod_d=products.objects.filter(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'details2.html',{'pr':prod_d})    
def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
         
    
    return render(request,"search.html",{'qr':query,'prod':prod})
# Create your views here.
