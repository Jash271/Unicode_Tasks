from django.urls import path
from . import views
from . views import LaunchesListView,LaunchesDetailView


urlpatterns=[
    path('',views.home,name='home'),
    path('list_view',LaunchesListView.as_view(),name='list-view'),
    path('detail_view/<int:pk>',LaunchesDetailView.as_view(),name='detail_view'),
    path('API-view',views.call,name='Call_API_SPACEX')
]