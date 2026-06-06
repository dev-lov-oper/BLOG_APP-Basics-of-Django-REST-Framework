from rest_framework   import serializers
from helloworld.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=True) 
    class Meta:
        model  = Post
        fields = '__all__'
        read_only_fields = ['created_by', 'created_on', 'updated_on']

    def create(self, validated_data):
        validated_data.pop('created_by', None)
        user = self.context['request'].user if self.context['request'].user.is_authenticated else None
        return Post.objects.create(created_by=user, **validated_data)