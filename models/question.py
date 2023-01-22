from dataclasses import dataclass


@dataclass
class Question:
    """
    Класс для хранения вопросов
    """
    pk: int
    text: str
    points: int
    used: bool = False

    def mark_used(self):
        self.used = True

    def dict(self):
        result = {
            "pk": self.pk,
            "text": self.text,
            "points": self.points,
            "used": self.used,
        }

        return result

