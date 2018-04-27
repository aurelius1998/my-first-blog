from django.shortcuts import render

def index(request):
	return render(request, 'blog/index.html', {})

def post_index(request):
	return render(request, 'myfirstgame.html', {})

# Create your views here.
