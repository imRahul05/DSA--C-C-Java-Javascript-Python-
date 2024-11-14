import math

def area():
 r = float(input("Enter the Radius of circle : "))
 ar = math.pi*r**2
 print(f"Area of the circle : {ar:.4f}")


def cylin():
 ra = float(input("Enter the radius : "))
 h = float(input("Enter the height: "))
 area = (2*math.pi*r*r) * 2*math.pi*r*h
 print(f"Area of cylinder is : {area:.2f}")

def main():
 print("Choose an option: \n 1.Calclute the area of circle \n 2.calculateb the area of cylinder")
 choice = int(input("Enter the option :"))


 if choice==1:
  area()
 elif choice ==2:
  cylin()
 else:
  print("Invalid choice. Please choose 1 or 2.")




main()