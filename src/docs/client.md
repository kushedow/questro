# Основные ручки от клиента к серверу

### Игровая сессия

```creategame``` отправляет заявку на создание game_session. 
В ответ возвращается экземпляр game_session

```json
{
   "pk": 112233344,
   "pass": 1239,
   "created_at": ...,
   "status": "ongoing"
   "players": [...]
   "questions_played": 
}
```

```joingame``` отправляет заявку на присоединение к игре по коду. В ответ возвращается экземпляр game_session

Формат запроса:

```json
{
  "pass": 1239,
}
```

В ответ возвращается экземпляр game_session. 
Теперь у обоих игроков есть game_session.

```json
{
   "pk": 112233344,
   "pass": 1239,
   "created_at": ...,
   "status": "ongoing"
   "players": [...]
   "questions_played": 
}
```

### Ответ

```answer``` Отправляет ответ на вопрос - объект типа answer

```json
{"player": ..., "game": ...}
```
В ответ возвращаются 
### Статистика


