from django.urls import path
from tutorials import views

urlpatterns = [
    path('api/tutorials', views.tutorial_list),
    # path('api/tutorials/<int:id>', views.tutorial_detail),
    # path('api/tutorials/published', views.tutorial_list_published)
]