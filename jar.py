class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Емкость должна быть неотрицательным целым числом.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Нельзя добавлять отрицательное количество печений.")
        if self._cookies + n > self._capacity:
            raise ValueError("Превышена емкость банки.")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Нельзя убирать отрицательное количество печений.")
        if self._cookies < n:
            raise ValueError("Недостаточно печений в банке.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


if __name__ == "__main__":
    jar = Jar(0)
    print(jar)
    jar.deposit(12)
    print(jar)
    print(jar.size)
    print(jar.capacity)
    jar.withdraw(0)
    print(jar)
