from rest_framework import viewsets, mixins, permissions, authentication
from .serializers import TagSerializer
from shared.models import Tag

# Create your views here.


class TagsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    Viewset for creating and retrieving tags
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """Return tags for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name').distinct()
    
    def perform_create(self, serializer):
        """Create a new tag and assign the current user to it"""
        serializer.save(user=self.request.user)
    
    