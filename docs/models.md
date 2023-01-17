# Модели для клиента и сервера

### GameSession – Игра (игровая сессия)

```python
@dataclass
class GameSession:
    pk: int,
    started_at: datetime:datetime,
    finished_at: datetitme.datetime,
    code: int,
    status: str,
    players: list
    questions: list
```

### Answer – Ответ (получается от пользователя)

```python
@dataclass
class Answer:
  question: int,
  score: int,
  player: int,
  
```
### Question Вопрос (загружается из базф)

```python
@dataclass
class Question:
    text: str,
    score: int,
```
