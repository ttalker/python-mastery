# day 9 MRO, super(), mixins
class Shape:
    """Base class for all shapes"""

    def __init__(self, color: str = "black"):
        # color is a shared attribute all shapes have
        self.color = color

    def area(self) -> float:
        # subclasses MUST override this
        raise NotImplementedError(f"{self.__class__.__name__} must implement area()")

    def describe(self) -> str:
        # uses area() — works because subclasses override it
        return f"{self.__class__.__name__}: color={self.color}, area={self.area():.2f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color={self.color!r})"


class Circle(Shape):
    def __init__(self, radius: float, color: str = "black"):
        # super().__init__(color) calls Shape.__init__ with the color arg
        # without this, self.color would never be set
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2  # π * r²


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str = "black"):
        super().__init__(color)   # pass color up to Shape
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height   # width × height


class Triangle(Shape):
    def __init__(self, base: float, height: float, color: str = "black"):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height   # ½ × base × height


c = Circle(5, color="red")
r = Rectangle(4, 6, color="blue")
t = Triangle(3, 8)

print("\n=== Shape Hierarchy ===")
print(c.describe())   # Circle: color=red, area=78.54
print(r.describe())   # Rectangle: color=blue, area=24.00
print(t.describe())   # Triangle: color=black, area=12.00


# ── PART 4: Mixin — add functionality without deep inheritance ─

class SerializableMixin:
    """
    Mixin: a class that adds a specific ability (serialization here)
    It does NOT have __init__ — it is not a standalone class
    It is designed to be mixed into other classes via multiple inheritance
    """

    def to_dict(self) -> dict:
        # vars(self) returns the instance __dict__ — all attributes
        # this works because Circle/Rectangle etc set self.radius, self.color etc
        return vars(self)

    def to_string(self) -> str:
        import json
        # json.dumps converts the dict to a JSON string
        # default=str handles non-serializable types
        return json.dumps(self.to_dict(), default=str)


class LoggableMixin:
    """Another mixin — adds logging ability"""

    def log(self, message: str) -> None:
        # self.__class__.__name__ gets the actual class name, not LoggableMixin
        print(f"[{self.__class__.__name__}] {message}")


# ColoredCircle inherits from BOTH mixins AND Circle
# MRO: ColoredCircle → SerializableMixin → LoggableMixin → Circle → Shape → object
class ColoredCircle(SerializableMixin, LoggableMixin, Circle):
    def __init__(self, radius: float, color: str):
        # super().__init__ follows MRO
        # eventually reaches Circle.__init__ which calls Shape.__init__
        super().__init__(radius, color)


print("\n=== Mixin Demonstration ===")
cc = ColoredCircle(3, "purple")
print(cc.to_dict())       # {'color': 'purple', 'radius': 3}
print(cc.to_string())     # {"color": "purple", "radius": 3}
cc.log("created")         # [ColoredCircle] created
print(f"MRO: {[cls.__name__ for cls in ColoredCircle.__mro__]}")
# ColoredCircle → SerializableMixin → LoggableMixin → Circle → Shape → object


# ── PART 5: Composition vs inheritance ───────────────────────

# Inheritance: "is-a" relationship. ColoredCircle IS-A Circle.
# Composition: "has-a" relationship. ShapeCollection HAS shapes.
# Rule: prefer composition when the relationship is not truly "is-a"

class ShapeCollection:
    """
    Does NOT inherit from Shape
    It HAS shapes — it contains them
    This is composition
    """

    def __init__(self):
        # stores shapes internally — not exposed directly
        self._shapes: list[Shape] = []

    def add(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def total_area(self) -> float:
        # sum calls shape.area() for each shape
        # works for ANY Shape subclass — polymorphism
        return sum(shape.area() for shape in self._shapes)

    def __len__(self) -> int:
        return len(self._shapes)

    def __iter__(self):
        # delegates iteration to the internal list
        return iter(self._shapes)

    def __repr__(self) -> str:
        return f"ShapeCollection({len(self)} shapes)"


print("\n=== Composition ===")
collection = ShapeCollection()
collection.add(Circle(5))
collection.add(Rectangle(4, 6))
collection.add(Triangle(3, 8))

print(collection)                          # ShapeCollection(3 shapes)
print(f"Total area: {collection.total_area():.2f}")  # sum of all areas
for shape in collection:                   # __iter__ makes this work
    print(f"  {shape.describe()}")