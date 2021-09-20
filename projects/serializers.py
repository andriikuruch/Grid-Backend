from rest_framework import serializers

from projects.models import Project, Style


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):
    style = serializers.StringRelatedField(source='style_id')
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Project
        fields = ['url', 'name', 'style', 'aria', 'preview']


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    style = serializers.StringRelatedField(source='style_id')
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Project
        exclude = ['style_id']


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Style
        fields = '__all__'
