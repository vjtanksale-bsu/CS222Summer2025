def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print(maximum(15, 20, 15))
def main():
    average = float(input("Enter average score: "))
    if average >= 60:
        print("Pass")
    else:
        print("Fail")
    
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")
    elif average >= 70:
        print("C")
    elif average >= 60:
        print("D")
    else:
        print("F")
# main()