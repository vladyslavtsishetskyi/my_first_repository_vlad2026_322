class Parfumy:
    """Клас "Парфуми"."""

    def __init__(self, volume, price, manufacturer):
        self.volume = volume              # об'єм (в мілілітрах)
        self.price = price                # ціна
        self.manufacturer = manufacturer  # назва виробника

    def __str__(self):
        return (f"Виробник: {self.manufacturer}, "
                f"об'єм: {self.volume} мл, ціна: {self.price}")


if __name__ == "__main__":
    p1 = Parfumy(50, 1200.0, "Chanel")
    p2 = Parfumy(100, 2500.0, "Dior")
    print(p1)
    print(p2)
