from dataclasses import dataclass


@dataclass
class Category:
    pk: int
    code: str
    title: str

    def dict(self):
        """ Сериализуем в словарь """
        result = {
            "pk": self.pk,
            "code": self.code,
            "title": self.title,
        }

        return result
