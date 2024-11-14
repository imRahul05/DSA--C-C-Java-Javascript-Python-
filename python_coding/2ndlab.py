import math


def si():
 p = float(input("Enter the Pricipal Amount : "))
 r = float(input("Enter the Rate of interst : "))
 t = float(input("Enter the time : "))
 simp = p*r*t/100
 print(f"Simple Interet : {simp:.4f}")


def ci():
 p = float(input("Enter the Pricipal Amount : "))
 r = float(input("Enter the Rate of interst : "))
 t = float(input("Enter the time : "))
 comp =  (p*(1 + r/100)**t) - p
 print("Compound Intersest : " , int(comp))


def main():
 print("Choose an option: \n 1.Calclute the Simple interest \n 2.calculateb the Compound interest")
 choice = int(input("Enter the option :"))


 if choice==1:
  si()
 elif choice ==2:
  ci()
 else:
  print("Invalid choice. Please choose 1 or 2.")




main()




