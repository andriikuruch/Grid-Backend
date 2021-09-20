from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from projects.models import Project, Style
from projects.paginations import RangedPagination
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer, StyleSerializer, ContactForm


class ProjectListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = RangedPagination


class ProjectDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class StyleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


@api_view(["POST", ])
@permission_classes([AllowAny, ])
def send_mail(request):
    if request.method == "POST":
        serializer = ContactForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message': 'email is sent'}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
