# Короче, меченый
В благородство играть не буду - пару зависимостей поставишь и мы в расчете.

- python3
- pipenv
- mysql-client

Заходишь в папку с проектом, делаешь
```
pipenv install --three
docker-compose up -d db
python main.py
```

После чего
```
mysql -u root -h0 db
```

Вуаля, база с фейковыми данными.

Если что-то из зависимостей не встало, вот тебе выхлоп ```pip freeze```

```
Faker==4.1.2
PyMySQL==0.10.0
python-dateutil==2.8.1
six==1.15.0
SQLAlchemy==1.3.19
text-unidecode==1.3
```