class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        #raise error if a negative capacity
        if capacity < 0:
            raise ValueError("Invalid cookie capacity entered.")

    def __str__(self):
        return "🍪" * self.size if self.size > 0 else ""


    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.add_cookies(n)
        else:
            raise ValueError("deposit exceeds the capacity amount")

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("not enough cookies to withdraw")
        else:
            self.remove_cookies(n)


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    def add_cookies(self, n):
        self._size = self._size + n

    def remove_cookies(self, n):
        self._size = self._size - n


def main():
    try:
        jar = Jar()
        jar.deposit(3)
        jar.withdraw(1)
    except Exception as err:
        print(err)


main()

if __name__ == "main":
    main()
