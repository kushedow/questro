## Серверная часть c сокетами для социального приложения Questro


Работает на порту 80, не забудь открыть порт на сервере!

Запускать:

```сd src```
```python run.py```

Запускать на сервере

```export PYTHONPATH=/root/questro```
```nohup python run.py > log.txt 2>&1 &```

---

### Запросы к серверу

Работа с игрой

```server/create_game  {"cat": 'default'}``` создать игру и сгенерить код

```server/join_game {"code": 1234}``` присоединиться к игре по коду

Работа с вопросами

```server/get_questions```  запрашивает 3 вопроса 

```server/pick_question {"pk": 1}```отправляет 1 вопрос партнеру

Работа с категорями

```server/get_categories``` запрашиваем категории

Всякое

```server/snapshot``` - снимок системы

### Слушатели для Postman

```client/welcome``` – при подключении

```client/game_created``` – после создания игры 

```client/game_updated``` – после получения данных игры

```client/get_questions``` – в ответ на просьбу прислать 3 вопроса

```client/receive_question``` – получение вопроса от парнера

```client/get_categories``` – получение всех категорий

```client/snapshot``` – снимок всех объектов

```client/exception``` – получение исключения


