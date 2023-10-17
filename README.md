Для запуска Docker образа небходимо выполнить следующие команды:

Сборка образов sudo docker-compose build

Запуск контейнеров sudo docker-compose up

Откройте второй терминал и примините маграции командой sudo docker-compose exec app python manage.py migrate


После успешного запуска проекта убедитесь что все зависимости установлены, премините миграции командой:

docker-compose exec app python manage.py migrate:

Чтобы запустить celery примените команду:

docker-compose exec celery -A config worker -l INFO

После запуска celery запутсите celery-beat командой:

docker-compose exec celery -A config beat -l INFO