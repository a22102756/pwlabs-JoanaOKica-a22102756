from django.shortcuts import render
from models import Post

def home_page_view(request):


	return render(request, 'portfolio/home.html')