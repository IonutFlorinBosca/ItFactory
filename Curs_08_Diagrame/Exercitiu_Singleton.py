# Varianta 1

# class SingletonClass(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print("Class is creating...")
#             cls._instance = super().__new__(cls)
#
#         return cls._instance
#
# a1 = SingletonClass()
# a2 = SingletonClass()
#
# print(a1)
# a1._instance = {"word", 2, True}
# print(a2)
#
# print(a1 is a2)

# Varianta 2
class Singleton(object):
    # creating the instance of this class
    def __new__(cls, *args, **kwargs):
        # checking if this class has an "_instance" atribute, else create one
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


a1 = Singleton()
a2 = Singleton()
print(a1)
a1._instance = "New"
print(a2._instance)
