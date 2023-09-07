from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealClient(Subject):

    def request(self):
        print("Real Client: Access Grented!")

class Proxy(Subject):

    #the constructor takes a real client as a parameter
    def __init__(self, the_real_client):
        self.the_real_client = the_real_client

    #do something before granting access to the real client
    def requireAccess(self):
        print("After doing x I will grant access!!")
        return True

    def request(self):
        if self.requireAccess():
            self.the_real_client.request()

real = RealClient()
prox = Proxy(real)
prox.request()