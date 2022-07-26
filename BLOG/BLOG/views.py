from xmlrpc.client import ResponseError
from rest_framework.decorators import api_view
from .models import Post
from rest_framework.response import Response

from .serializers import PostSerializer

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)



