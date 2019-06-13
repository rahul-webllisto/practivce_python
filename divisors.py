
def divisor(n):
    print("Divisors of {} ".format(n))
    for i in range(1,n):
        if n%i==0:            
            print(i)

if __name__ == '__main__':

    num=int(input("enter a number: "))
    divisor(num)
