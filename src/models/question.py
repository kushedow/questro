from dataclasses import dataclass


@dataclass
class Question:
    """
    Класс для хранения вопросов
    """
    pk: int

    text: str
    points: int = 0  # баллы DEPRECATED
    used: bool = False

    cat: str = "default"  # категория

    def mark_used(self):
        self.used = True

    def dict(self):
        result = {
            "pk": self.pk,
            "text": self.text,
            "points": self.points,
            "used": self.used,
            "cat": self.cat,
        }

        return result

