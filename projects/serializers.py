from rest_framework import serializers

from projects.models import Project, Style


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):
    style = serializers.StringRelatedField(source='style_id')

    class Meta:
        model = Project
        fields = ['url', 'name', 'style', 'aria']


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    style = serializers.StringRelatedField(source='style_id')

    class Meta:
        model = Project
        exclude = ['style_id']


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
