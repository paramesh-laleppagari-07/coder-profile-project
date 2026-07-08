from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes

from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
       {'GET': '/api/projects'},
       {'GET': '/api/projects/id'}, 
       {'POST': '/api/projects/id/vote'},
       
       {'POST': '/api/users/token'},
       {'POST': '/api/users/token/refresh'},
       
        
    ]
    return JsonResponse(routes, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    print("USER:", request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    # print(request.data) 
    data = request.data
    
    review, created = Review.objects.get_or_create(
        owner=user, 
        project=project
        )
    review.value = data['value']
    review.save()
    project.getVoteCount()
   
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)



from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def removeTag(request):
    print("REQUEST DATA:", request.data)

    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    print("REMAINING:", project.tags.all())

    return Response({'message': 'Tag deleted'})

