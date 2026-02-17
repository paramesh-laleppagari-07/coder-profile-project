from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

projectList = [
    {'id':1, 'title':'E-commerce Website', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':2, 'title':'Social Media App', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':3, 'title':'Blog Platform', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':4, 'title':'Portfolio Website', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':5, 'title':'Task Management Tool', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':6, 'title':'Online Learning Platform', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':7, 'title':'Fitness Tracker App', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':8, 'title':'Recipe Sharing Website', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':9, 'title':'Event Management System', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    {'id':10, 'title':'Travel Booking Platform', 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit auctor dui, sed efficitur ipsum.'},
    ]
def projects(request):
    msg="Hello, This is the projects page"
    page="Projects"
    number = 11
    context={'page':page,'number':number,'msg':msg,'projects':projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
        
    return render(request, 'projects/single-project.html', {'project':projectObj})