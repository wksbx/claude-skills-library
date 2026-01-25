# SOLID Principles Reference

## Single Responsibility Principle (SRP)

A class should have one, and only one, reason to change.

**Violation:**
```python
class User:
    def __init__(self, name): self.name = name
    def save_to_database(self): ...  # persistence
    def send_email(self): ...         # notification
    def generate_report(self): ...    # reporting
```

**Fixed:**
```python
class User:
    def __init__(self, name): self.name = name

class UserRepository:
    def save(self, user): ...

class EmailService:
    def send(self, user, message): ...
```

## Open/Closed Principle (OCP)

Open for extension, closed for modification.

**Violation:**
```python
def calculate_area(shape):
    if shape.type == "circle":
        return 3.14 * shape.radius ** 2
    elif shape.type == "rectangle":
        return shape.width * shape.height
    # Adding new shape requires modifying this function
```

**Fixed:**
```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h): self.width, self.height = w, h
    def area(self): return self.width * self.height
```

## Liskov Substitution Principle (LSP)

Subclasses must be substitutable for their parent classes.

**Violation:**
```python
class Bird:
    def fly(self): return "flying"

class Penguin(Bird):
    def fly(self): raise Exception("Can't fly!")  # Breaks substitution
```

**Fixed:**
```python
class Bird:
    def move(self): pass

class FlyingBird(Bird):
    def move(self): return "flying"

class Penguin(Bird):
    def move(self): return "swimming"
```

## Interface Segregation Principle (ISP)

Many specific interfaces beat one general-purpose one.

**Violation:**
```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass  # Robots don't eat

class Robot(Worker):
    def work(self): return "working"
    def eat(self): pass  # Forced to implement unused method
```

**Fixed:**
```python
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): return "working"
    def eat(self): return "eating"

class Robot(Workable):
    def work(self): return "working"
```

## Dependency Inversion Principle (DIP)

Depend on abstractions, not concrete implementations.

**Violation:**
```python
class MySQLDatabase:
    def query(self, sql): ...

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Concrete dependency
```

**Fixed:**
```python
class Database(ABC):
    @abstractmethod
    def query(self, sql): pass

class UserService:
    def __init__(self, db: Database):  # Depends on abstraction
        self.db = db

# Can inject any implementation
service = UserService(MySQLDatabase())
service = UserService(PostgresDatabase())
```

## Quick SOLID Checklist

- [ ] **S**: Does each class have only one responsibility?
- [ ] **O**: Can I add features without modifying existing code?
- [ ] **L**: Can subclasses replace parents without breaking behavior?
- [ ] **I**: Are interfaces focused and minimal?
- [ ] **D**: Do high-level modules depend on abstractions?
