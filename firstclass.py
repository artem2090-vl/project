class Motorcycl:
    mark = None
    type = None
    cub = None
    __owner = None

    def __init__(self, mark_user, type_user, cub_user, owner_user):
        self.mark = mark_user
        self.type = type_user
        self.cub = cub_user
        self.__owner = owner_user
    def show_moto(self):
        print(f"Марка: {self.mark}")
    def show_type(self):
        print(f"Тип: {self.type}")
    def show_cub(self):
        print(f"Кубатура: {self.cub}")
    def show_owner(self):
        if len(self.__owner) <= 4:
           return f"Власник: {self.__owner[0:2]}*******"
        else:
           return f"Власник: {self.__owner[0:3]}*******"



mark_user = input("Введи марку мотоцикла: ")
type_user = input("Введи тип мотоциклу:")
cub_user = input("Введи кубатуру мотоцикла:")
owner_user = input("Введи імя власника:")

#cub_user = float(cub_user)

moto = Motorcycl(mark_user, type_user, cub_user, owner_user)

moto.show_moto()
moto.show_type()
moto.show_cub()
print(moto.show_owner())
#print(moto.owner)
