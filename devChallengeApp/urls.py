from django.contrib import admin
from django.urls import path
from .views import indexPageView
# , howPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPageView, name="index"),
    # path('how/', howPageView, name="how")
]
