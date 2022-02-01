from django import forms
from django.db.models import query
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from products.models import Product
from .forms import ProductForm


def bad_view(request, *args, **kwargs):
    # print(dict(request.GET))
    my_request_data = dict(request.GET)
    new_product = my_request_data.get('new_product')
    print(my_request_data, new_product)
    if new_product[0].lower() == 'true':
        print(new_product)
        Product.objects.create(title=my_request_data.get(
            'title')[0], content=my_request_data.get('content')[0])
    return HttpResponse('Dont do this')


def home_view(request, *args, **kwargs):
    context = {"name": "kean", "age": 21}
    return render(request, 'home.html', context)


def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "abc", "query": query}
    return render(request, 'home.html', context)


# def product_create_view(request, *args, **kwargs):
    # print(request.POST)
    # print(request.GET)
#    if request.method == 'POST':
#        post_data = request.POST or None
#        if post_data is not None:
#            my_form = ProductForm(request.POST)
#            if my_form.is_valid():
#                print(my_form.cleaned_data.get('title'))
#                title_from_input = my_form.cleaned_data.get('title')
#                Product.objects.create(title=title_from_input)
#           # print(post_data)
#    return render(request, 'forms.html', {})

def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        # Do some Stuff
        obj.save()
        # print(request.POST)
        # print(form.cleaned_data)
        #data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductForm()
        # return HttpResponseRedirect("/success")
        # return redirect("/success")

    return render(request, 'forms.html', {"form": form})


def product_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(f'Not Found')
    return render(request, 'products/detail.html', {"object": obj})


def product_json_detail_view(request, pk, *arg, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'messages': 'Not Found'})
    return JsonResponse({'ID :': obj.pk})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {'object_list': qs}
    return render(request, 'products/list.html', context)
