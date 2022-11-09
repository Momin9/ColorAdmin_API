from rest_framework.routers import DefaultRouter
from django.urls import path, include

from Related_Links.views import Privacy_and_PolicyViewSet, Contact_UsViewSet, Terms_of_UseViewSet, Shopping_HelpViewSet

router = DefaultRouter()
router.register(r'privacy_policy', Privacy_and_PolicyViewSet, basename="Privacy_and_PolicyViewSet")
router.register(r'contact_us', Contact_UsViewSet, basename="Contact_UsViewSet")
router.register(r'term_use', Terms_of_UseViewSet, basename="Terms_of_UseViewSet")
router.register(r'shopping_help', Shopping_HelpViewSet, basename="Shopping_HelpViewSet")



urlpatterns = [
    path("", include(router.urls)),

]