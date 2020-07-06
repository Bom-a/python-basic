import math
a = int(input("nhập a: ")) 
b = int(input("nhập b: "))
c = int(input("nhập c: "))
if a == 0:
    if b == 0:
        if c == 0:  # truong hop a = 0,b = 0,c = 0
            print("phương trình có vô số nghiệm")
        else:       # truong hop a = 0,b = 0,c = 0    
            print("phương trình vô nghiệm")
    else:
        if c == 0: # truong hop a = 0,b /= 0,c = 0
            print("phương trình có nghiệm là: x = 0")
        else:      # truong hop a = 0,b /= 0,c = 0
            print("phương trình có nghiệm là: ", -c/b)
else:
    delta = b * b - 4 * a * c # tính delta
    if delta < 0:             # trường hợp delta < 0
        print("Phương trình vô nghiệm!")
    elif delta == 0:          # trường hợp delta = 0
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:                     # trường hợp delta > 0
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - math.sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + math.sqrt(delta)) / (2 * a)))
