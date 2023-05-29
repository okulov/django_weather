from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import weather

urlpatterns = {
    path('', weather, name="items"),
    path('<slug:key>', weather, name="specific_city")
}
urlpatterns = format_suffix_patterns(urlpatterns)
