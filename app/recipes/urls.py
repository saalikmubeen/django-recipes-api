from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagsViewSet, IngredientsViewSet, RecipeViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('tags', TagsViewSet) # /api/recipes/tags/
router.register("ingredients", IngredientsViewSet) # /api/recipes/ingredients/
router.register("recipes", RecipeViewSet) # /api/recipes/recipes/, /api/recipes/recipes/id/, /api/recipes/recipes/id/upload-image/

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)), # The API URLs are now determined automatically by the router.
]


# urlpatterns = [
#     path('tags/', TagsViewSet.as_view({'get': 'list', 'post': 'create'}), name='tags'),
# ]