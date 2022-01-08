from rest_framework import viewsets, mixins, permissions, authentication
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer
from shared.models import Tag, Ingredient, Recipe

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


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating, reading and updating recipes
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        """Return recipes for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new recipe and assign the current user to it"""
        serializer.save(user=self.request.user)
    
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return RecipeDetailSerializer

        return self.serializer_class