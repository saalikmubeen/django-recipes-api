from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagsViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('tags', TagsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)), # /api/recipes/tags/
]


# urlpatterns = [
#     path('tags/', TagsViewSet.as_view({'get': 'list', 'post': 'create'}), name='tags'),
# ]