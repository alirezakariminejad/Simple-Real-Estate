from random import choice
from user import User

FIRST_NAME = ["alireza", "meysam", "ehsan", "mahdi", "amirhossein"]
LAST_NAME = ["karimi", "alavi", "moghaddam", "shahkandi", "bagheri"]
MOBILES = ["09123625456", "09125478963", "09135563256", "09135475214", "09145693253", "09158965413"]

if __name__ == "__main__":
    for mobile in MOBILES:
        User(first_name=choice(FIRST_NAME), last_name=choice(LAST_NAME), phone_number=choice(mobile))

    for user in User.object_list:
        print(f"{user.id}: \t {user.full_name}")
