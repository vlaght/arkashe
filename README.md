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

Вуаля, база с фейковыми данными