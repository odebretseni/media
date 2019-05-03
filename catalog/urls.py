from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/$', views.ItemListView.as_view(), name='item_list'),
    url(r'^items/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item_detail'),
    url(r'^photos/(?P<pk>\d+)$', views.PhotoDetailView.as_view(), name='photo_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#handler404 = views.error404
