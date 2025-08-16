from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
# Импортируем PageContentListView напрямую из apps.core.views
from apps.core.views import PageContentListView 
# Импортируем site_settings_view напрямую из apps.core.views
from apps.core.views import site_settings_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.applications.urls')),
    path('api/', include('apps.accounts.urls')),
    
    # Напрямую указываем путь к PageContentListView
    path('api/page-content/', PageContentListView.as_view(), name='page-content'),
    
    # Напрямую указываем путь к site_settings_view
    path('api/site-settings/', site_settings_view, name='site-settings'),
    
    path('', RedirectView.as_view(url=settings.SITE_URL, permanent=False)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "Страховая платформа - Администрирование"
admin.site.site_title = "Админ панель"
admin.site.index_title = "Управление системой"
