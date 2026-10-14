from dataclasses import dataclass

# decorator
@dataclass
class Point:
    x: int
    y: int

# __init__
# __rep__    (print out or view content of an object)
# __eq__     (compare two instances of the same object)

p = Point(1, 2)
p2 = Point(1, 2)
print(p == p2)