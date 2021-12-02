def log(func):
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} was called")
        result = func(*args, **kwargs)
        print(f"function {func.__name__} ended its execution")
        return result
    return wrapper

class Flameable:
    @log
    def store(self):
        print("Keep this away from the open flame")


class Product:
    @log
    def __init__(self, name):
        self.name = name
    @log
    def add_to_cart(self, ammount):
        past = "was"
        if ammount > 1:
            past = "were"
        print(f"{ammount} {self.name} {past} added to cart")

class Book(Product, Flameable):
    @log
    def __init__(self, author, name, pages):
        super().__init__(f"Book of {author}: {name}")
        self.author = author
        self.name = name
        self.pages = pages
    @log
    def add_to_cart(self, ammount):
        super().add_to_cart(ammount)
        print("Enjoy your reading!")
