from django.urls import path
from .views import CreateUserView, AuthTokenView, ManageUserView


urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create-user"),
    path('token/', AuthTokenView.as_view(), name="create-token"),
    path('me/', ManageUserView.as_view(), name="me"),
]