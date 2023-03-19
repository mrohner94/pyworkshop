try:
    int("a")
except ValueError as e:
    print("oops, you can't do that")
    print(e)

print("this is the end of my program")