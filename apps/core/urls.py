from django.urls import path
# Импортируем оригинальный PageContentListView
from .views import PageContentListView, site_settings_view

app_name = 'core'

urlpatterns = [
    # Используем оригинальный PageContentListView
    path('page-content/', PageContentListView.as_view(), name='page-content'),
    path('site-settings/', site_settings_view, name='site-settings'),
]
