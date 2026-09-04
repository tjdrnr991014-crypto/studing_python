MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost":1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for ingredients in order_ingredients:
        if order_ingredients[ingredients] >= resources[ingredients]:
            print(f"죄송합니다 {ingredients}가 충분하지 않습니다")
            return False
        
    return True

def process_coins():
    print("동전을 넣어주세요")
    quarters = int(input("쿼터 개수:"))
    dimes = int(input("다임 개수:"))
    nickels = int(input("니켈 개수:"))
    pennies = int(input("페니 개수:"))

    total = (quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01)

    return total

def is_transaction_successful(money_received, drink_cost):
    global profit

    cost = money_received-drink_cost

    if money_received < drink_cost:
        print("죄송합니다 금액이 부족합니다")
        return False
        
    elif money_received >drink_cost:
        print(f'거스름돈{cost:.2f}를 돌려드립니다' )
    
    profit = profit + drink_cost

    return True

def make_coffee(drink_name, order_ingredients):

    for ingredients in order_ingredients:
        resources[ingredients] = resources[ingredients]- order_ingredients[ingredients]

    print(f'여기 {drink_name}나왔습니다')

def report():
    print(f"물:{resources['water']}ml")
    print(f"우유:{resources['milk']}ml")
    print(f"커피:{resources['coffee']}ml")
    print(f"돈: ${profit:.2f}")

while True:
    choice = input("어떤 음료를 원하시나요?(espresso/latte/cappuccino):")

    if choice == "off":
        print("종료합니다")
        break

    if choice == "report":
        report()
        continue

    if choice not in MENU:
        print("메뉴를 올바르게 적어주세요")
        continue

    
    drink = MENU[choice]

    ingredients = drink["ingredients"]
    cost = drink["cost"]
        
    if not is_resource_sufficient(ingredients):
        continue

    money_received = process_coins()

    if not is_transaction_successful(money_received, cost):
        continue
    make_coffee(choice, ingredients)

    


