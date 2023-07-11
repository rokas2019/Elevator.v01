from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('screen/', views.ele_screen, name='screen'),
    path('levels/', views.levels_list, name='levels_list'),
    path('levels/create/', views.level_create, name='level_create'),
    path('levels/<int:pk>/', views.level_detail, name='level_detail'),
    path('levels/<int:pk>/update/', views.level_update, name='level_update'),
    path('levels/<int:pk>/delete/', views.level_delete, name='level_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)