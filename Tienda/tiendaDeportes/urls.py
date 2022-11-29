from django.urls import path
from tiendaDeportes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="Index"),
    path('\popular',views.indexPopular, name="IndexPopular"),
    path('\promocion',views.indexPromocion, name="IndexPromocion"),

]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)