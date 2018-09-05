from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponse

# Create your views here.
def post_list(request):
    template = get_template('post_list.html')
    context = {
        'text1': 'Python'
    }

    return HttpResponse(template.render(context))