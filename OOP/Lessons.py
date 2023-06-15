# Lesson 1
# Classes and objects.
# Attributes of classes and objects.

class Point:
    """
    Class to define points coordinates on coordinate plane
    """
    # Attributes (or properties)
    color = 'Red'
    circle = 2


Point.color = 'Black'
Point.circle = 1

a = Point()
b = Point()
# print(a.__dict__)
# print(b.color)

a.color = 'Green'
# print(a.__dict__)

# Class and its instance have their own namespaces!!!

# Adding and deleting attributes

Point.type_pt = 'disc'
# print(Point.__dict__)

setattr(Point, 'prop', 1)
# print(Point.__dict__)

setattr(Point, 'type_pt', 'square')
# print(Point.__dict__)

# print(getattr(Point, 'type_pt'))

del Point.prop
# print(getattr(Point, 'prop', False))

delattr(Point, 'type_pt')
# print(getattr(Point, 'type_pt', False))

# Attribute deleting available only in current namespace (example: now
# we cant do something like
# del b.color, cause b doesn't has 'color' attribute.
# But we can:
# del a.color

a.x = 1
a.y = 2
b.x = 10
b.y = 20

print(Point.__doc__)
# __________________________________________________________________

