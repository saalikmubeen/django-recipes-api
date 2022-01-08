from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagsViewSet, IngredientsViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('tags', TagsViewSet) # /api/recipes/tags/
router.register("ingredients", IngredientsViewSet) # /api/recipes/ingredients/

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)), # The API URLs are now determined automatically by the router.
]


# urlpatterns = [
#     path('tags/', TagsViewSet.as_view({'get': 'list', 'post': 'create'}), name='tags'),
# ]