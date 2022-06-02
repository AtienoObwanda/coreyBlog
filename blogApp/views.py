from django.shortcuts import render
from .models import *

# posts = [
#     {
#         'author': 'Atieno',
#         'content': 'First dummy post',
#         'date_posted': 'May 27 2018'
#     },
#      {
#         'author': 'Kikie',
#         'content': 'Second dummy post',
#         'date_posted': 'June 27 2019'
#     },
#      {
#         'author': 'Treasure',
#         'content': 'Third dummy post',
#         'date_posted': 'May 27 2020'
#     },
#      {
#         'author': 'Atieno',
#         'content': 'Fourth dummy post',
#         'date_posted': 'May 27 2021'
#     }
# ]

# Create your views here.
def home(request):
    posts = posts.objects.all()
    return render(request, 'blog/index.html', {"posts": posts})

def about(request):
    return render(request, 'blog/about.html')