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

    def __new__(cls, *args, **kwargs): # cls is a link to current class
        print('Callback __new__ method for ' + str(cls))
        return super().__new__(cls)

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

# a.color = 'Green'
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

# a.x = 1
# a.y = 2
# b.x = 10
# b.y = 20

# print(Point.__doc__)
# __________________________________________________________________

# Lesson 2
# Class methods.
# Parameter "self"

# Adding "set_coords" into Point class in Lesson 1

# pt = Point()
# print(type(pt)) # <class '__main__.Point'>
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
# print(pt.get_coords())

# So... As method name is a class attribute we can do something like:
# res = getattr(pt, 'get_coords')
# print(res) # link to object-function: >>> <bound method Point.get_coords of <__main__.Point object at 0x1286ddf10>>
# print(res())
# but this way is uncommon, so usually we should use point-call (.get_coords())


# __________________________________________________________________
# Lesson 3
# Initializer __init__ and finalizer __del__

# Rewrite class method set_coords() with '__init__' magic method in the begining of this file.

# pt = Point(1, 2)
# print(pt.__dict__)

# Add finalizer __del__ to class.
# Garbage collector delete instances, cause there aren't any external links on them.


# __________________________________________________________________
# Lesson 4
# Magic method __new__.
# Singleton pattern example.

# Adding __new__ magic method to our class

pt = Point(1, 2)
print(pt)

# About Singleton


class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        print('deleting instance ' + str(self))

    def connect(self):
        print(f'Connecting to DataBase: {self.user}, {self.psw}, {self.port}.')

    def close(self):
        print('Closing DB connection.')

    def read(self):
        return "DB data"

    def write(self, data):
        print(f"Writing to DB: {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))

db.connect()
db2.connect()

# __________________________________________________________________
# Lesson 5
# Classmethod and staticmethos


class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
        # if self.validate(x) and self.validate(y): # almost possible
            self.x = x
            self.y = y
        print(Vector.norm2(self.x, self.y)) # This doesn't print anything...
        print(self.norm2(self.x, self.y)) # This doesn't print anything...

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x*x + y*y

    def get_coords(self):
        return self.x, self.y


v = Vector(10, 20)
coords = v.get_coords()
print(coords)

coord2 = Vector.get_coords(v)
print(coord2)

res = Vector.validate(995)
print(res)

res = Vector.norm2(5, 6)
print(res)