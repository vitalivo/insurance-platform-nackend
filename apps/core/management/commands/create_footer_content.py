from django.core.management.base import BaseCommand
from apps.core.models import PageContent
from apps.applications.models import ApplicationStatus

class Command(BaseCommand):
    help = 'Создает базовый контент для футера, хедера и страниц'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Принудительно обновить существующие записи',
        )

    def handle(self, *args, **options):
        force_update = options['force']
        
        # КОНТЕНТ ДЛЯ ХЕДЕРА (НОВОЕ!)
        header_content = [
            # Логотип и компания
            ('header', 'logo', 'company_name', 'СтрахПлатформа', 'text'),
            ('header', 'logo', 'tagline', 'Надежная защита', 'text'),
            
            # Контакты в хедере
            ('header', 'contacts', 'phone', '8 (800) 123-45-67', 'text'),
            ('header', 'contacts', 'phone_link', '+78001234567', 'text'),
            ('header', 'contacts', 'phone_description', 'Бесплатно по России', 'text'),
            
            # Админка
            ('header', 'admin', 'admin_url', 'https://insurance-platform-nackend.onrender.com/admin/', 'text'),
            ('header', 'admin', 'admin_text', 'Личный кабинет', 'text'),
        ]
        
        # Контент для футера
        footer_content = [
            # Контакты
            ('footer', 'contacts', 'phone', '8 (800) 123-45-67', 'text'),
            ('footer', 'contacts', 'phone_link', '+78001234567', 'text'),
            ('footer', 'contacts', 'phone_description', 'Бесплатно по России', 'text'),
            ('footer', 'contacts', 'email', 'info@strah-platform.ru', 'text'),
            ('footer', 'contacts', 'email_link', 'info@strah-platform.ru', 'text'),
            ('footer', 'contacts', 'email_description', 'Техподдержка', 'text'),
            ('footer', 'contacts', 'address', 'Москва, ул. Тверская, 15', 'text'),
            ('footer', 'contacts', 'address_description', 'Офис продаж', 'text'),
            
            # Ссылки информации
            ('footer', 'info_links', 'about_company_text', 'О компании', 'text'),
            ('footer', 'info_links', 'about_company_link', '/pages/about', 'text'),
            ('footer', 'info_links', 'licenses_text', 'Лицензии', 'text'),
            ('footer', 'info_links', 'licenses_link', '/pages/licenses', 'text'),
            ('footer', 'info_links', 'partners_text', 'Партнеры', 'text'),
            ('footer', 'info_links', 'partners_link', '/pages/partners', 'text'),
            ('footer', 'info_links', 'vacancies_text', 'Вакансии', 'text'),
            ('footer', 'info_links', 'vacancies_link', '/pages/vacancies', 'text'),
            ('footer', 'info_links', 'privacy_policy_text', 'Политика конфиденциальности', 'text'),
            ('footer', 'info_links', 'privacy_policy_link', '/pages/privacy', 'text'),
            
            # Социальные сети (ПУСТЫЕ - чтобы не показывались по умолчанию)
            ('footer', 'social', 'vk_link', '', 'text'),
            ('footer', 'social', 'telegram_link', '', 'text'),
            ('footer', 'social', 'youtube_link', '', 'text'),
            
            # Копирайт
            ('footer', 'copyright', 'text', '© 2025 СтрахПлатформа. Все права защищены.', 'text'),
            ('footer', 'copyright', 'license_text', 'Лицензия ЦБ РФ № 12345', 'text'),
            ('footer', 'copyright', 'rsa_text', 'Член РСА', 'text'),
        ]

        # Контент для страниц (весь контент из вашего файла)
        pages_content = [
            # О компании
            ('about', 'main', 'content', '''
                <h2>О нашей компании</h2>
                <p>СтрахПлатформа — современная страховая компания, которая предоставляет широкий спектр страховых услуг для физических и юридических лиц.</p>
                
                <h3>Наша миссия</h3>
                <p>Обеспечить надежную страховую защиту для каждого клиента, используя современные технологии и индивидуальный подход.</p>
                
                <h3>Наши преимущества</h3>
                <ul>
                    <li>Быстрое оформление полисов онлайн</li>
                    <li>Конкурентные тарифы</li>
                    <li>Круглосуточная поддержка клиентов</li>
                    <li>Широкая сеть партнеров</li>
                </ul>
                
                <h3>История компании</h3>
                <p>Основанная в 2020 году, наша компания быстро завоевала доверие клиентов благодаря надежности и качеству предоставляемых услуг.</p>
            ''', 'html'),
            
            # Лицензии
            ('licenses', 'main', 'content', '''
                <h2>Лицензии и разрешения</h2>
                <p>Наша компания имеет все необходимые лицензии для осуществления страховой деятельности.</p>
                
                <h3>Основные лицензии</h3>
                <ul>
                    <li><strong>Лицензия ЦБ РФ № 12345</strong> от 01.01.2020 - основная лицензия на страховую деятельность</li>
                    <li><strong>Лицензия на ОСАГО № 67890</strong> от 15.03.2020 - обязательное страхование автогражданской ответственности</li>
                    <li><strong>Лицензия на страхование имущества № 11111</strong> от 20.05.2020 - страхование недвижимости и имущества</li>
                    <li><strong>Лицензия на личное страхование № 22222</strong> от 10.07.2020 - страхование жизни и здоровья</li>
                </ul>
                
                <h3>Членство в организациях</h3>
                <ul>
                    <li>Российский союз автостраховщиков (РСА)</li>
                    <li>Всероссийский союз страховщиков (ВСС)</li>
                    <li>Национальный союз страховщиков ответственности (НССО)</li>
                </ul>
                
                <p><strong>Все лицензии действительны и регулярно продлеваются в соответствии с требованиями законодательства.</strong></p>
            ''', 'html'),
            
            # Партнеры
            ('partners', 'main', 'content', '''
                <h2>Наши партнеры</h2>
                <p>Мы сотрудничаем с ведущими компаниями в различных сферах для обеспечения качественного сервиса.</p>
                
                <h3>Банки-партнеры</h3>
                <ul>
                    <li><strong>Сбербанк</strong> - кредитование и банковские услуги</li>
                    <li><strong>ВТБ</strong> - корпоративное обслуживание</li>
                    <li><strong>Альфа-Банк</strong> - премиальные услуги</li>
                    <li><strong>Газпромбанк</strong> - специальные программы</li>
                </ul>
                
                <h3>Автосалоны</h3>
                <ul>
                    <li><strong>Автомир</strong> - официальный дилер</li>
                    <li><strong>Рольф</strong> - премиум автомобили</li>
                    <li><strong>Авилон</strong> - широкая сеть салонов</li>
                    <li><strong>Инком-Авто</strong> - специальные условия</li>
                </ul>
                
                <h3>Медицинские центры</h3>
                <ul>
                    <li><strong>Медси</strong> - премиальная медицина</li>
                    <li><strong>СМ-Клиника</strong> - широкая сеть клиник</li>
                    <li><strong>Европейский медицинский центр</strong> - международные стандарты</li>
                </ul>
                
                <p>Партнерство с ведущими компаниями позволяет нам предоставлять клиентам лучшие условия и качественный сервис.</p>
            ''', 'html'),
            
            # Вакансии
            ('vacancies', 'main', 'content', '''
                <h2>Работа в СтрахПлатформе</h2>
                <p>Мы всегда ищем талантливых специалистов для развития нашей команды.</p>
                
                <h3>Почему стоит работать у нас?</h3>
                <ul>
                    <li>Конкурентная заработная плата</li>
                    <li>Полный социальный пакет</li>
                    <li>Возможности карьерного роста</li>
                    <li>Обучение и развитие</li>
                    <li>Дружный коллектив</li>
                    <li>Современный офис в центре Москвы</li>
                </ul>
                
                <h3>Открытые вакансии</h3>
                
                <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 20px; margin: 20px 0;">
                    <h4>Страховой агент</h4>
                    <p><strong>Требования:</strong> опыт работы в страховании от 1 года, коммуникабельность, ответственность, знание ПК.</p>
                    <p><strong>Обязанности:</strong> консультирование клиентов, оформление полисов, ведение клиентской базы.</p>
                    <p><strong>Условия:</strong> официальное трудоустройство, оклад + проценты, бонусы за выполнение плана.</p>
                </div>
                
                <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 20px; margin: 20px 0;">
                    <h4>Менеджер по работе с клиентами</h4>
                    <p><strong>Требования:</strong> высшее образование, опыт работы с клиентами от 2 лет, знание CRM-систем.</p>
                    <p><strong>Обязанности:</strong> обработка заявок, консультирование, сопровождение сделок.</p>
                    <p><strong>Условия:</strong> полный рабочий день, социальный пакет, обучение за счет компании.</p>
                </div>
                
                <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 20px; margin: 20px 0;">
                    <h4>Андеррайтер</h4>
                    <p><strong>Требования:</strong> высшее образование (экономическое/юридическое), опыт в страховании от 3 лет.</p>
                    <p><strong>Обязанности:</strong> оценка рисков, принятие решений по страхованию, анализ заявок.</p>
                    <p><strong>Условия:</strong> высокая заработная плата, премии, возможность удаленной работы.</p>
                </div>
                
                <h3>Как откликнуться?</h3>
                <p>Для отправки резюме пишите на: <a href="mailto:hr@strah-platform.ru" style="color: #2563eb;">hr@strah-platform.ru</a></p>
                <p>Или звоните по телефону: <a href="tel:+74951234567" style="color: #2563eb;">+7 (495) 123-45-67</a></p>
                
                <p><em>Мы рассматриваем все резюме и обязательно отвечаем каждому кандидату!</em></p>
            ''', 'html'),
            
            # Политика конфиденциальности
            ('privacy', 'main', 'content', '''
                <h2>Политика конфиденциальности</h2>
                <p><em>Дата последнего обновления: 17 августа 2025 года</em></p>
                
                <p>Настоящая Политика конфиденциальности определяет порядок обработки персональных данных пользователей сайта СтрахПлатформа.</p>
                
                <h3>1. Общие положения</h3>
                <p>Мы обязуемся защищать конфиденциальность персональных данных наших клиентов в соответствии с требованиями Федерального закона № 152-ФЗ "О персональных данных".</p>
                
                <h3>2. Какие данные мы собираем</h3>
                <ul>
                    <li><strong>Личные данные:</strong> ФИО, дата рождения, паспортные данные</li>
                    <li><strong>Контактная информация:</strong> телефон, email, адрес</li>
                    <li><strong>Данные для страхования:</strong> информация об объекте страхования</li>
                    <li><strong>Технические данные:</strong> IP-адрес, cookies, данные браузера</li>
                </ul>
                
                <h3>3. Как мы используем данные</h3>
                <ul>
                    <li>Оформление и обслуживание страховых полисов</li>
                    <li>Связь с клиентами по вопросам страхования</li>
                    <li>Выполнение обязательств по договорам</li>
                    <li>Улучшение качества услуг</li>
                    <li>Соблюдение требований законодательства</li>
                </ul>
                
                <h3>4. Передача данных третьим лицам</h3>
                <p>Мы можем передавать ваши данные:</p>
                <ul>
                    <li>Страховым компаниям-партнерам для оформления полисов</li>
                    <li>Государственным органам по их законным требованиям</li>
                    <li>Сервисным компаниям для технической поддержки</li>
                </ul>
                
                <h3>5. Защита данных</h3>
                <p>Мы применяем современные технические и организационные меры для защиты персональных данных:</p>
                <ul>
                    <li>Шифрование данных при передаче (SSL/TLS)</li>
                    <li>Ограничение доступа к данным</li>
                    <li>Регулярное обновление систем безопасности</li>
                    <li>Обучение сотрудников правилам обработки данных</li>
                </ul>
                
                <h3>6. Ваши права</h3>
                <p>Вы имеете право:</p>
                <ul>
                    <li>Получать информацию об обработке ваших данных</li>
                    <li>Требовать уточнения, блокирования или уничтожения данных</li>
                    <li>Отзывать согласие на обработку данных</li>
                    <li>Обращаться в надзорные органы</li>
                </ul>
                
                <h3>7. Cookies и аналитика</h3>
                <p>Наш сайт использует cookies для улучшения пользовательского опыта и аналитики. Вы можете отключить cookies в настройках браузера.</p>
                
                <h3>8. Изменения в политике</h3>
                <p>Мы можем обновлять данную политику. О существенных изменениях мы уведомим вас по email или через уведомления на сайте.</p>
                
                <h3>9. Контакты</h3>
                <p>По вопросам обработки персональных данных обращайтесь:</p>
                <ul>
                    <li><strong>Email:</strong> <a href="mailto:privacy@strah-platform.ru" style="color: #2563eb;">privacy@strah-platform.ru</a></li>
                    <li><strong>Телефон:</strong> <a href="tel:+78001234567" style="color: #2563eb;">8 (800) 123-45-67</a></li>
                    <li><strong>Адрес:</strong> 125009, г. Москва, ул. Тверская, д. 15</li>
                </ul>
            ''', 'html'),
        ]

        # Создаем весь контент
        created_count = 0
        updated_count = 0
        
        all_content = header_content + footer_content + pages_content
        
        for page_name, section_name, content_key, content_value, content_type in all_content:
            obj, created = PageContent.objects.get_or_create(
                page_name=page_name,
                section_name=section_name,
                content_key=content_key,
                defaults={
                    'content_value': content_value,
                    'content_type': content_type
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f"✅ Создано: {page_name}.{section_name}.{content_key}")
            elif force_update:
                # Обновляем существующие записи ТОЛЬКО с флагом --force
                obj.content_value = content_value
                obj.content_type = content_type
                obj.save()
                updated_count += 1
                self.stdout.write(f"🔄 Обновлено: {page_name}.{section_name}.{content_key}")
            else:
                self.stdout.write(f"ℹ️  Уже существует: {page_name}.{section_name}.{content_key}")

        # Создаем статусы заявок
        self.stdout.write("\n📋 Создание статусов заявок...")
        statuses = [
            ('Новая', '#3B82F6', 'Новая заявка, ожидает обработки', False, 1),
            ('В обработке', '#F59E0B', 'Заявка принята в работу', False, 2),
            ('Требует уточнения', '#EF4444', 'Необходимы дополнительные документы', False, 3),
            ('Одобрена', '#10B981', 'Заявка одобрена, готовится полис', False, 4),
            ('Полис выдан', '#059669', 'Полис оформлен и выдан клиенту', True, 5),
            ('Отклонена', '#DC2626', 'Заявка отклонена', True, 6),
        ]
        
        status_created_count = 0
        for name, color, description, is_final, sort_order in statuses:
            obj, created = ApplicationStatus.objects.get_or_create(
                name=name,
                defaults={
                    'color': color,
                    'description': description,
                    'is_final': is_final,
                    'sort_order': sort_order
                }
            )
            if created:
                status_created_count += 1
                self.stdout.write(f"✅ Создан статус: {name}")
            else:
                self.stdout.write(f"ℹ️  Статус уже существует: {name}")

        # Итоговая статистика
        self.stdout.write(
            self.style.SUCCESS(f'\n🎉 Готово!')
        )
        self.stdout.write(f"📄 Создано записей контента: {created_count}")
        if updated_count > 0:
            self.stdout.write(f"🔄 Обновлено записей: {updated_count}")
        self.stdout.write(f"📋 Создано статусов: {status_created_count}")
        self.stdout.write(
            self.style.SUCCESS('✅ Все данные успешно загружены!')
        )
