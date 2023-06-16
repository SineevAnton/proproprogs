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

    # def set_coords(self, x, y):
    #     print('set_coords method call')
    #     self.x = x
    #     self.y = y

    # Initializer
    def __init__(self, x=0, y=0):
        print('__init__ callback')
        self.x = x
        self.y = y

    # Finalizer
    def __del__(self):
        print('Deleting instance: ' + str(self))

    def get_coords(self):
        return (self.x, self.y)


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

# print(Point.__doc__)
# __________________________________________________________________

# Lesson 2
# Class methods.
# Parameter "self"

# Adding "set_coords" into Point class in Lesson 1

pt = Point()
print(type(pt)) # <class '__main__.Point'>
# print(type(pt.set_coords)) # <class 'method'>, but it isn't method call

# pt.set_coords() # Don't work if there is no 'self' parameter in set_coords() method
# Point.set_coords() # Work if there is no 'self' parameter in set_coords() method

# pt.set_coords() # Work if there is 'self' parameter in set_coords() method

# pt.set_coords(1, 2)
# print(pt.__dict__)

# pt2 = Point()
# pt2.set_coords(10, 20)
# print(pt2.__dict__)

# !!! 'self' parameter allows us to work with a specific instance of class

# Adding "get_coords" into Point class in Lesson 1
print(pt.get_coords())

# So... As method name is a class attribute we can do something like:
res = getattr(pt, 'get_coords')
print(res) # link to object-function: >>> <bound method Point.get_coords of <__main__.Point object at 0x1286ddf10>>
print(res())
# but this way is uncommon, so usually we should use point-call (.get_coords())

# __________________________________________________________________
# Lesson 3
# Initializer __init__ and finalizer __del__

# Rewrite class method set_coords() with '__init__' magic method in the begining of this file.

pt = Point(1, 2)
print(pt.__dict__)