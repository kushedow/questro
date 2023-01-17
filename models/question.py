from dataclasses import dataclass


@dataclass
class Question:
    """
    Класс для хранения вопросов
    """
    pk: int
    text: str
    score: int
    used: bool = False

    def mark_used(self):
        self.used = True

    def dict(self):
        result = {
            "pk": self.pk,
            "text": self.text,
            "score": self.score,
            "used": self.used,
        }

        return result

