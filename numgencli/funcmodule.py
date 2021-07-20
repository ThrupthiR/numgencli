#actual login to print numbers randomly
import random
def my_function(a,b):
    numbers_range = list(range(a,b))
    random.shuffle(numbers_range)
    print(numbers_range)