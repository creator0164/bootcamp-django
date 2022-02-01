from django.shortcuts import render
from django.http import HttpResponse


def profile_detail_view(request, *args, **kwargs):
    return HttpResponse("Profile")
