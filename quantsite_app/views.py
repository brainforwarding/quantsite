from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def index(request):
    template = loader.get_template("quantsite_app/index.html")
    return HttpResponse(template.render())
