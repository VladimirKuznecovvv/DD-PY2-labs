class Vehicle:
    """
    Базовый класс для транспортного средства.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства
        :param model: Модель транспортного средства
        :param year: Год выпуска
        """
        self._brand = brand  # Приватный атрибут для предотвращения изменения напрямую
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запуск двигателя.

        :return: Сообщение о запуске двигателя
        """
        return "Двигатель запущен."

    def stop_engine(self) -> str:
        """
        Остановка двигателя.

        :return: Сообщение о выключении двигателя
        """
        return "Двигатель выключен."

    def __str__(self) -> str:
        return f"{self.year} {self._brand} {self.model}"

    def __repr__(self) -> str:
        return f"Vehicle('{self._brand}', '{self.model}', {self.year})"


class Car(Vehicle):
    """
    Дочерний класс для автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str):
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_type: Тип топлива
        """
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def honk(self) -> str:
        """
        Использование звукового сигнала.

        :return: Сообщение о звуке сигнала
        """
        return "Бип-бип!"

    def start_engine(self) -> str:
        """
        Переопределение метода запуска двигателя.
        У автомобиля может быть другая логика запуска.

        :return: Сообщение о запуске двигателя автомобиля
        """
        return f"Автомобиль {self._brand} {self.model} заведен."

    def __str__(self) -> str:
        return f"{self.year} {self._brand} {self.model} ({self.fuel_type})"

    def __repr__(self) -> str:
        return f"Car('{self._brand}', '{self.model}', {self.year}, '{self.fuel_type}')"


if __name__ == "__main__":
    # Тестовые примеры
    vehicle1 = Vehicle("Yamaha", "R1", 2022)
    car1 = Car("Toyota", "Camry", 2021, "Бензин")

    print(vehicle1)
    print(vehicle1.start_engine())
    print(vehicle1.stop_engine())

    print(car1)
    print(car1.start_engine())
    print(car1.honk())
