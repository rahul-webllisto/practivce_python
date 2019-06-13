
def less5(l1):
    print([x for x in l1 if x<5])

if __name__ == '__main__':

    l1=list(map(int, input("create list of numbers with space: ").split()))
    less5(l1)
