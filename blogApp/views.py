from django.shortcuts import render
from .models import posts

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
    allposts = posts.objects.all()

    return render(request, 'blog/index.html', {"allposts": allposts})

def about(request):
    return render(request, 'blog/about.html')