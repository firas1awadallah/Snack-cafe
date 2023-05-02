
Appetizers = ["Wings", "Cookies", "Spring Rolls"]
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream", "Cake", "Pie"]
Drinks = ["Coffee", "Tea", "Unicorn Tears"]

order_counts = {}  

def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

''')

def user_insertion():
    user_input = input("> ")  
    return user_input        

def main():
    user_input = user_insertion()
    while user_input.lower() != "quit":
   
        if user_input in Appetizers or user_input in Entrees or user_input in Desserts or user_input in Drinks:
            order_counts[user_input] = order_counts.get(user_input, 0) + 1
            count = order_counts[user_input]
            print(f"** {count} order{'s' if count > 1 else ''} of {user_input} has been added to your meal **")
        else:
            print("Sorry, we don't have this item!")
        user_input = user_insertion()    

    end_application()

def end_application():
    print("Thanks for using Snakes Cafe application!")
    print("Here is a summary of your order:")
    for item, count in order_counts.items():
        print(f"{count} order{'s' if count > 1 else ''} of {item}") 
    
intro()
main()

                 

 








