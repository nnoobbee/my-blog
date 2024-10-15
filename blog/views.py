from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def qwe(request):
    return HttpResponse('qwe')
# Create your views here.
