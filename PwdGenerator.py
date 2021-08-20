import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()!@#$%^&*?"

all = lower+upper+numbers+symbols
Length: int = 16
password = "".join(random.sample(all, Length))
print(password)

