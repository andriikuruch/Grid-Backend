from django.shortcuts import render
from rest_framework import viewsets, mixins

from projects.models import Project, Style
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer, StyleSerializer


class ProjectListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ProjectDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class StyleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
