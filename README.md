# Пульт охраны банка
Сайт, который можно подключить к удалённой базе данных, для организации пульта охраны предприятия. В базе должна быть информация с карточками посетителей и карточками их визитов.

## Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```commandline
pip install -r requirements.txt
```
### Enviroments
В проекте используются переменные окружения. Создайте файл `.env` и укажите переменные:
- DATABASE_URL - URL со всеми настройками подключения к СУБД ```postgres://USER:PASSWORD@HOST:PORT/NAME```
- ALLOWED_HOSTS - Разрешенные хосты сайта ```['*']```
- SECRET_KEY - Секретный ключ, с помощью которого шифруют пароли пользователей сайта
- DEBUG - Отладочный режим сайта ```True or False```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.