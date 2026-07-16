# use @dataclass when you are constructing a class primarily engineered to store data, state, or configuration parameters, and you want to eliminate verbose boilerplate code by automatically generating underlying methods like __init__, __repr__, and __eq__.

# Using frozen=True makes the dataclass immutable, meaning once an instance is created, its fields cannot be modified. This is useful for creating hashable objects that can be used as dictionary keys or stored in sets, and for ensuring the integrity of data throughout the lifecycle of the object.


from dataclasses import dataclass


@dataclass(frozen=True)
class Contractor:
    id: int
    name: str
    score: float
