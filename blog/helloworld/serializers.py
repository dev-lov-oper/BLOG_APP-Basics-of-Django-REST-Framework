from rest_framework   import serializers
from helloworld.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username',read_only=True) 
    class Meta:
        model  = Post
        fields = '__all__'
        read_only_fields = [ 'created_by']

    def create(self, validated_data):
        validated_data.pop('created_by', None)
        return Post.objects.create(created_by=self.context['request'].user, **validated_data)