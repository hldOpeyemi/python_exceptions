# def greet(name):
#     print('Hello, I am', name)

# greet('John')

x = 3
y = "hello"
try:
    print('I am trying something bad!')
    print (x + y)
except TypeError:
    print("Sorry! You cannot add integer to string")
except:
    print('Something bad has happened, get help')
finally:
    print('I will always happen, error or no error')
