from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PageContent, SiteSettings
from .serializers import PageContentSerializer, SiteSettingsSerializer
import logging

logger = logging.getLogger(__name__)

class PageContentListView(generics.ListAPIView):
    """Получение контента страниц"""
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
    lookup_field = None
    lookup_url_kwarg = None

    # ВОЗВРАЩАЕМ ЭТОТ МЕТОД get
    def get(self, request, *args, **kwargs):
        print("--- DEBUG: get метод вызван ---")
        queryset = self.get_queryset() # Вызываем наш get_queryset
        print(f"--- DEBUG: get_queryset вернул {queryset.count()} объектов ---")

        if not queryset.exists():
            print("--- DEBUG: Queryset пуст, но возвращаем 200 OK с пустым списком ---")
            return Response([], status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        print(f"--- DEBUG: Сериализовано {len(serializer.data)} объектов. Возвращаем 200 OK ---")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        # Эти print-операторы можно оставить для финальной проверки, затем удалить.
        print("--- DEBUG: get_queryset вызван ---")
        queryset = super().get_queryset()
        page_name = self.request.query_params.get('page', None)
        print(f"--- DEBUG: Получен параметр 'page': '{page_name}' ---")

        logger.info(f"DEBUG: PageContentListView - Начало get_queryset. Получен параметр 'page': '{page_name}'")

        all_page_contents = PageContent.objects.all()
        logger.info(f"DEBUG: PageContentListView - Все объекты PageContent в базе данных (до фильтрации): {[pc.page_name for pc in all_page_contents]}")

        if page_name:
            try:
                filtered_queryset = queryset.filter(page_name=page_name)
                logger.info(f"DEBUG: PageContentListView - Объектов найдено после фильтрации по '{page_name}': {filtered_queryset.count()}")
                if not filtered_queryset.exists():
                    logger.warning(f"DEBUG: PageContentListView - После фильтрации по '{page_name}' не найдено ни одного объекта. Проверьте регистр и наличие данных в админке.")
                print(f"--- DEBUG: Возвращаем отфильтрованный queryset (count: {filtered_queryset.count()}) ---")
                return filtered_queryset
            except Exception as e:
                logger.error(f"DEBUG: Ошибка при фильтрации queryset по page_name='{page_name}': {e}")
                print(f"--- DEBUG: Ошибка при фильтрации: {e} ---")
                return PageContent.objects.none()
        
        logger.info(f"DEBUG: PageContentListView - Параметр 'page' не предоставлен. Возвращаем все объекты: {queryset.count()}")
        print(f"--- DEBUG: Возвращаем весь queryset (count: {queryset.count()}) ---")
        return queryset

@api_view(['GET'])
def site_settings_view(request):
    """Получение настроек сайта"""
    settings, created = SiteSettings.objects.get_or_create()
    serializer = SiteSettingsSerializer(settings)
    return Response(serializer.data)
