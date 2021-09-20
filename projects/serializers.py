from django.core.mail import send_mail
from rest_framework import serializers

from projects.models import Project, Style


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    style = serializers.StringRelatedField(source='style_id')
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Project
        fields = ['url', 'id', 'name', 'style', 'aria', 'preview']


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    style = serializers.StringRelatedField(source='style_id')
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Project
        exclude = ['style_id']


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    preview = serializers.StringRelatedField(source='preview.url')

    class Meta:
        model = Style
        fields = '__all__'


class ContactForm(serializers.Serializer):
    email = serializers.EmailField()

    def save(self, **kwargs):
        email = self.validated_data['email']
        send_mail(subject="Gritting",
                  from_email="gir-pro@gmail.com",
                  recipient_list=[email, ],
                  message='Hello')

