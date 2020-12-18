from random import choice
from user import User
from region import Region
from estate import Apartment, House, Store
from advertisment import ApartmentSell

FIRST_NAME = ["alireza", "meysam", "ehsan", "mahdi", "amirhossein"]
LAST_NAME = ["karimi", "alavi", "moghaddam", "shahkandi", "bagheri"]
MOBILES = ["09123625456", "09125478963", "09135563256", "09135475214", "09145693253", "09158965413"]

if __name__ == "__main__":
    for mobile in MOBILES:
        User(first_name=choice(FIRST_NAME), last_name=choice(LAST_NAME), phone_number=choice(mobile))

    for user in User.object_list:
        print(f"{user.id}: \t {user.full_name}")

    r1 = Region(name='Andishe')

    apartment1 = Apartment(has_elevator=True, has_parking=True, floor=2, user=User.object_list[0], area=120,
                           rooms_count=2, built_year=1396, region=r1, address="Shahriyar")

    house1 = House(has_yard=True, floors_count=2, user=User.object_list[1], area=90,
                   rooms_count=1, built_year=1390, region=r1, address="Shahriyar")

    store1 = Store(user=User.object_list[2], area=50, rooms_count=1, built_year=1390, region=r1, address="Shahriyar")

    apartment_sell_1 = ApartmentSell(has_elevator=False, has_parking=False, floor=3, user=User.object_list[0], area=90,
                                     rooms_count=2, built_year=1399, region=r1, address="Shahriyar",
                                     price_per_meter=8000000, discountable=False, convertable=False)

    apartment1.show_description()
    house1.show_description()
    store1.show_description()

    apartment_sell_1.show_details()
