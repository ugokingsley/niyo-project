from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our Book ViewSets with it.
router = DefaultRouter()
router.register(r'books', views.SnippetViewSet, basename='books')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]