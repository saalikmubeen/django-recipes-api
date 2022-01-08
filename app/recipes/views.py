from rest_framework import viewsets, mixins, permissions, authentication
from .serializers import TagSerializer, IngredientSerializer
from shared.models import Tag, Ingredient

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
    

class IngredientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    Viewset for creating and retrieving ingredients
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        """Return ingredients for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name').distinct()
    
    def perform_create(self, serializer):
        """Create a new ingredient and assign the current user to it"""
        serializer.save(user=self.request.user)