from rest_framework import serializers

from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fiedls = "__all__"
