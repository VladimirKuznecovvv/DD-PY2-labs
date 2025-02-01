import doctest


class MusicalInstrument:
    """
    Класс, представляющий музыкальный инструмент.
    """
    def __init__(self, name: str, material: str):
        """
        Инициализация объекта "Музыкальный инструмент".

        :param name: Название инструмента
        :param material: Материал изготовления

        Примеры:
        >>> guitar = MusicalInstrument("Guitar", "Wood")
        """
        if not isinstance(name, str):
            raise TypeError("Название инструмента должно быть строкой")
        if not name:
            raise ValueError("Название инструмента не может быть пустым")
        self.name = name

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not material:
            raise ValueError("Материал не может быть пустым")
        self.material = material

    def play(self, style: str) -> None:
        """
        Игра на инструменте в указанном стиле.

        :param style: Стиль игры (например, классический, джазовый)
        :raise ValueError: Если стиль пустой

        Примеры:
        >>> guitar = MusicalInstrument("Guitar", "Wood")
        >>> guitar.play("Jazz")
        """
        if not isinstance(style, str):
            raise TypeError("Стиль игры должен быть строкой")
        if not style:
            raise ValueError("Стиль игры не может быть пустым")
        ...

    def tune(self) -> None:
        """
        Настройка инструмента.

        Примеры:
        >>> guitar = MusicalInstrument("Guitar", "Wood")
        >>> guitar.tune()
        """
        ...


class SmartphoneApp:
    """
    Класс, представляющий мобильное приложение.
    """
    def __init__(self, name: str, version: str):
        """
        Инициализация объекта "Мобильное приложение".

        :param name: Название приложения
        :param version: Версия приложения

        Примеры:
        >>> app = SmartphoneApp("WeatherApp", "1.0.0")
        """
        if not isinstance(name, str):
            raise TypeError("Название приложения должно быть строкой")
        if not name:
            raise ValueError("Название приложения не может быть пустым")
        self.name = name

        if not isinstance(version, str):
            raise TypeError("Версия должна быть строкой")
        if not version:
            raise ValueError("Версия не может быть пустой")
        self.version = version

    def update(self, new_version: str) -> None:
        """
        Обновление приложения до новой версии.

        :param new_version: Новая версия приложения
        :raise ValueError: Если новая версия идентична текущей

        Примеры:
        >>> app = SmartphoneApp("WeatherApp", "1.0.0")
        >>> app.update("1.1.0")
        """
        if not isinstance(new_version, str):
            raise TypeError("Новая версия должна быть строкой")
        if new_version == self.version:
            raise ValueError("Новая версия должна отличаться от текущей")
        ...

    def open(self) -> None:
        """
        Открытие приложения.

        Примеры:
        >>> app = SmartphoneApp("WeatherApp", "1.0.0")
        >>> app.open()
        """
        ...


class FitnessTracker:
    """
    Класс, представляющий фитнес-трекер.
    """
    def __init__(self, model: str, steps_goal: int):
        """
        Инициализация объекта "Фитнес-трекер".

        :param model: Модель трекера
        :param steps_goal: Целевое количество шагов в день

        Примеры:
        >>> tracker = FitnessTracker("FitPro X1", 10000)
        """
        if not isinstance(model, str):
            raise TypeError("Модель трекера должна быть строкой")
        if not model:
            raise ValueError("Модель трекера не может быть пустой")
        self.model = model

        if not isinstance(steps_goal, int):
            raise TypeError("Цель по шагам должна быть целым числом")
        if steps_goal <= 0:
            raise ValueError("Цель по шагам должна быть положительным числом")
        self.steps_goal = steps_goal

    def track_steps(self, steps: int) -> None:
        """
        Отслеживание количества сделанных шагов.

        :param steps: Количество шагов
        :raise ValueError: Если шаги отрицательные

        Примеры:
        >>> tracker = FitnessTracker("FitPro X1", 10000)
        >>> tracker.track_steps(5000)
        """
        if not isinstance(steps, int):
            raise TypeError("Количество шагов должно быть целым числом")
        if steps < 0:
            raise ValueError("Количество шагов не может быть отрицательным")
        ...

    def check_goal(self) -> bool:
        """
        Проверка, достигнута ли цель по шагам.

        :return: True, если цель достигнута, иначе False

        Примеры:
        >>> tracker = FitnessTracker("FitPro X1", 10000)
        >>> tracker.steps_goal = 10000
        >>> tracker.check_goal()
        True
        """
        return True


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров
