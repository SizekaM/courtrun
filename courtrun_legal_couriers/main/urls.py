from django.urls import path
from . import views
from django.views.static import serve
from django.conf import settings

app_name = "main"

urlpatterns = [
	
	path('', views.home, name="home"),
    path('selection/', views.selection, name="selection"), 
	path('route/', views.route, name="route"),
    path('route-serve/', views.route_serve, name="route_serve"),
    path('route-file/', views.route_file, name="route_file"),
    path('route-summon/', views.route_summon, name="route_summon"),
    path('route-notice/', views.route_notice, name="route_notice"),
    path('route-correspondence/', views.route_correspondence, name="route_correspondence"),
	path('order-details', views.map, name="map"),
    path('serve-order-details', views.map_serve, name="map_serve"),
    path('file-order-details', views.map_file, name="map_file"),
    path('summon-order-details', views.map_summon, name="map_summon"),
    path('notice-order-details', views.map_notice, name="map_notice"),
    path('correspondence-order-details', views.map_correspondence, name="map_correspondence"),
    path('pricing/', views.pricing, name="pricing"),
	path('page-not-found/', views.page_not_found, name="page_not_found"), 
	path('popia/', views.popia, name="popia"),    
	path('faq/', views.faq, name="faq"),  
    path('contact/', views.contact, name="contact"),      
    path('confirmation/', views.confirmation, name="confirmation"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
	path('terms-and-conditions', views.terms_and_conditions, name="terms_and_conditions"),       
    path('googlee7ff021fb9cd9b73.html', serve, {'document_root': settings.STATIC_ROOT}),
	]

