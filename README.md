# employees_django
Написать апи, которой можно отправить пару команд на взаимодействие с таблицей о сотрудниках в БД:
/insert
Добавляет информацию о сотруднике
/update
Обновляет информацию о сотруднике
/select
Возвращает информацию о сотруднике
Примеры полей:
ФИО, Дата рождения, Стаж работы
Пример обращения к апи:
http://localhost:8000/insert
Все аргументы должны быть в json формате, и апи их должна провалидировать. При обращении к БД должна быть исключена возможность sql инъекций.
В случае наличия ошибок в параметрах, либо обращении к апи отправить соответствующий ответ в формате json.

requirements:
- pip install -r requirements.txt

postgesql:
- docker-compose -f docker-compose.dev.yaml up

tests:
- python manage.py test
