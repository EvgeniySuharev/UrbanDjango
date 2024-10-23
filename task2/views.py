from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Index1(TemplateView):
    template_name = 'class_template.html'


def index2(request):
    return render(request, 'func_template.html')
