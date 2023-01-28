import logging


def create_loggers():

    # Создаем логгер сокетов настраиваем его на максимальную чувствительность
    socket_logger = logging.getLogger("socket")
    socket_logger.setLevel("DEBUG")

    # Добавляем обработчик – ошибки будут падать в файл
    file_handler = logging.FileHandler("logs/socket.log")
    socket_logger.addHandler(file_handler)

    # Создаем форматтер и настраиваем вывод для обработчиков
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")
    file_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)

    print("SOCKET    LOGGER CREATED")

    # Создаем логгер хранилища и настраиваем его тоже
    storage_logger = logging.getLogger("storage")
    storage_logger.setLevel("DEBUG")

    # Добавляем обработчик
    storage_handler = logging.FileHandler("logs/storage.log")
    storage_logger.addHandler(storage_handler)

    # Добавляем форматтер
    storage_handler.setFormatter(formatter_one)

    print("STORAGE   LOGGER CREATED")


create_loggers()
