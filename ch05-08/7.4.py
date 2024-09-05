class Fan():
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__( self , on = False , rad = 5 ,  spd = SLOW , clr = "blue" ):
        self.__speed = spd
        self.__radius = rad
        self.__color = clr
        self.__on = on

    def __str__(self):
        if self.__on == True:
            return "\n\t Fan is On"+"\n\t Fan Speed = " + self.get_Speed() + "\n\t Fan Radius = " + str(self.__radius) + "\n\t Fan Color = " + self.__color + "\n"
        else:
            return "\n\t Fan is Off"+"\n\t Fan Speed = "+self.get_Speed() + "\n\t Fan Radius = " + str(self.__radius) + "\n\t Fan Color = " + self.__color  + "\n"

    def get_Speed(self):
        if self.__speed == 1:
            return "SLOW"
        elif self.__speed == 2:
            return "MEDIUM"
        elif self.__speed == 3:
            return "FAST"

    def set_Speed(self,spd):
        self.__speed = spd

    def get_Radius(self):
        return self.__radius

    def set_Radius(self,rad):
        self.__radius = rad

    def get_Color(self):
        return self.__color

    def set_Color(self,clr):
        self.__color = clr

    def Set_ON(self):
        self.__on = True

    def Set_OFF(self):
        self.__on = False

    def get_ON(self):
        return self.__on

f = Fan()
f1 = Fan( True , 10 , 3 , "Yellow" )
f2 = Fan(False , 5 , 2 , "Blue")

print("\n Default Fan:")
print(f)
print("\n FAN 1 :")
print(f1)
print("\n FAN 2 :")
print(f2)
