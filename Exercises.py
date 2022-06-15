"""
In the Athlete class given below,

a. make all the attributes private and

b. add the necessary accessor and mutator methods

Represent Maria, the runner and make her run.

class Athlete:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def running(self):
        if(self.gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
"""
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_name(self):
        return self.__name


    def running(self):
        if self.__gender == "girl":
            return "running 150mtr"
        else:
            return "running 200mtr"

ma = Athlete("Maria","girl")
print(ma.get_name(), " is ", ma.running())

ma = Athlete("Priya","girl")
print(ma.get_name(), " is ", ma.running())


