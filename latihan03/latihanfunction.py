# function

def helloWorld (name):
    print ("Hello, %s" % name)
# call method
helloWorld("luke skywalker")

def helloWorld (name):
    print(f"Hello,{name}")
# call method
helloWorld("luke skywalker")



def helloWorld (name):
    print(f"Hello,{name}")

def secondFunc():
    name = 'Luke Skywalker'
    return helloWorld(name)
helloWorld('Jhon Doe')


# print bilangan negative
def printNegative(index, lengt):
    if index == "" and length == "":
        return
    
    while index < lengt:
        if index % 2 == 1:
            print(index)
        index +=1

# call method
helloWorld('Jhon Doe')

secondFunc()

printNegative(0, 100)