#Calls myfunction
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    #print('in main')
    my_function(1,11)

if __name__ == '__main__':
    main()