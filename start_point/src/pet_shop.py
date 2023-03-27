# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"]) 

def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# alt. method:
# def remove_pet_by_name(pet_shop, name):
#   pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))
     
def add_pet_to_stock(pet_shop, new_pet):
    if bool(new_pet):
        pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    if bool(new_pet):
        customers["pets"].append(new_pet)


# Below code is incorrect:
# def customer_can_afford_pet(customers, new_pet):
#     for customer in customers:
#         if customer["cash"] >= new_pet["price"]:
#             return True
#         print("You have sufficient funds")
#     else: 
#             return False
# print("you have insufficient funds")


def customers_can_afford_pet(customers, new_pet):
    if customers["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# alt method:
# def customers_can_afford_pet(customers, new_pet):
#     return customers["cash"] >= new_pet["price"]
    

# RECAP THIS!!:   
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customers_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
