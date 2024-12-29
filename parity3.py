# Demonstrates returning the value of a Boolean expression

def main():
    x = int(input("what is x? "))
    if x_even(x):
        print("Evan")
    else:
        print("odd")

def x_even(n):
    return n % 2 == 0

main()