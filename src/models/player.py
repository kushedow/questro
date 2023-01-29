from dataclasses import dataclass

from src.models.game_session import GameSession
from src.models.question import Question


@dataclass
class Player:
    sid: str  # идентификатор сокета
    pk: int = 0
    score: int = 0
    game: GameSession = None
    questions: list | None = None

    def __post_init__(self):
        self.score = 0
        self.questions = []

    def add_answer(self, question: Question):
        """Добаввляет вопрос в список использованных"""
        if question is not None:
            self.questions.append(question)

    def get_game(self):
        return self.game

    def dict(self):

        result = {
            "sid": self.sid,
            "score": self.score,
            "pk": self.pk,
            "questions": [question.dict() for question in self.questions],
        }

        return result

