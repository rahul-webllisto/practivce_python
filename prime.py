
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:            
            return "NOT PRIME"
    return "PRIME"

if __name__ == '__main__':
    num = int(input("enter a number to check if it is prime: "))
    print(is_prime(num))
