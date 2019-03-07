 #!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("DIME UN ANO Y TE DIGO SI ES BISIESTO")
    n = int(input("introduce un número: "))
    if n%400==0:
        print("El ano {} es un ano bisiesto porque es múltiplo de 400.".format(n))
    elif n%100==0:
        print("El ano {} NO es un ano bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.".format(n))

    elif n%4 == 0:
        print("El ano {} es un ano bisiesto porque es múltiplo de 4.".format(n))
    else:
        print("El ano {} NO es un ano bisiesto.".format(n))
      
if __name__ == "__main__":
    main()

