
def even_list(l):
    print([x for x in l if x%2==0])

if __name__ == '__main__':
    l1 = list(map(int, input("create list of numbers with spaces: ").split()))
    even_list(l1)