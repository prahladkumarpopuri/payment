from django.shortcuts import render

'''from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('hello, world!')'''

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
