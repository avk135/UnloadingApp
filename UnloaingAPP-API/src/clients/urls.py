from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from clients import views as clients_views

urlpatterns = [
    # lists
    path('all1/', clients_views.CliensList.as_view()),
    path('unloading/all/', clients_views.UnloadingList.as_view()),
    path('unloading/list/<int:client_id>/', clients_views.UnloadingClientList.as_view()),
    # adds
    path('add/', clients_views.ClientCreate.as_view()),
    path('unloading/add/', clients_views.UnLoadingCreate.as_view()),
    # updates
    path('unloading/update/', clients_views.UpdatePaid.as_view()),
    # deletes
    path('unloading/<int:id>/delete/', clients_views.DeleteUnloading.as_view()),
    path('client/<int:id>/delete/', clients_views.DeleteClient.as_view())
]