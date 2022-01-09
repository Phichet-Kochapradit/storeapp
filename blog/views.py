from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    ##return HttpResponse("Hello ICT STOU")ปิดไว้##
    posts = Post.objects.all()
    return render(request, 'index.html', {'test':posts})
