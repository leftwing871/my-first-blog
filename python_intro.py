import random

#volume 값을 입력하세요.
if random.randrange(1, 10) > 5:
    print("true Hello, Django Girls.")
elif 10 > 5:
    print("10 > 5 Hello, Django Girls.")
else:
    print("false Hello, Django Girls.")