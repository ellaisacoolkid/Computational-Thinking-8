import turtle, time, random
from utils import *

# Section 1 - setup
set_background("Bakery")
money = 0
cookies = 0
cost = 2
# everything start at 0 except for cost because the cost for each cookie is 2 



# Section 2 - controls
def get_money() :
    global money
    money += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("money",x,y)
window.onkeypress(get_money, "space")
# if you want cookies you need at least 2 dollars. each cookie is 2 dollars so you gotta press the space bar to get money to get cookies.



def get_cookies() :
    global money, cookies, cost
    if money >= cost :
        cost = cost * 2
        cookies+= 1
        x = -400 + 120*cookies
        y = -200
        create_sprite("cookies",x,y)
window.onkeypress(get_cookies, "a")
#  you can only get cookies if you have enough money so you have to click "a" to get cookies