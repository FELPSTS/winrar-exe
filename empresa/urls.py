from django.urls import path
from .views import EMPRECreateView, EMPREListView, EMPREDetailView, EMPREUpdateView, EMPREDeleteView

urlpatterns = [
    path('create/', EMPRECreateView.as_view(), name='empre-create'),
    path('list/', EMPREListView.as_view(), name='empre-list'), # nada definido abaixo dessa aqui
    path('<int:pk>/', EMPREDetailView.as_view(), name='empre-detail'),
    path('<int:pk>/update/', EMPREUpdateView.as_view(), name='empre-update'),
    path('<int:pk>/delete/', EMPREDeleteView.as_view(), name='empre-delete'),
]
