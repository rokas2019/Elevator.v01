from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path('screen/', views.ele_screen, name='screen'),
                path('levels/', views.levels_list, name='level_list'),
                path('levels/<int:pk>/', views.level_detail, name='level_detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

