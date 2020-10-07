# Инструкция к заданию
Здравствуйте!
Я подготовил небольшую инструкцию к выполненному заданию. Надеюсь, она сэкономит ваше время:

Как вы можете видеть: я решил воспользоваться Докером. Управляемый демон - apache.
Если что, само приложение работает при помощи nginx. 

Пока что приложение может работать только на локальном компьютере. 
Но оно готово к работе на VPS. Для этого просто нужно будет в файле .env.prod добавить ip адрес в DJANGO_ALLOWED_HOSTS.

Инструкция к запуску(Должен быть установлен Докер):
1. Нужно клонировать репозиторий себе на диск: git clone https://github.com/LpilinAlexandr/demon_control.git
2. В консоли зайти в репозиторий и ввести команду: docker-compose -f docker-compose.prod.yml up -d --build
3. После запуска контейнеров нужно ввести команду для сбора статики (хотя и без этого должно работать): docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input

4. В этот момент можно уже зайти на адрес: http://127.0.0.1/

Если хотите проверить работу демона изнутри:
(приложение работает из под root'a. Понимаю, что это дурной тон, но у меня получилось только так)
5.Чтобы зайти внутрь контейнера, введите: docker-compose -f docker-compose.prod.yml exec web bash
6.Чтобы проверить работу apache, введите service --status-all или service apache2 status
7.Чтобы выйти из контейнера, введите exit

8.Чтобы завершить работу контейнера, введите docker-compose -f docker-compose.prod.yml down -v
