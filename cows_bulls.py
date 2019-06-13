import random
count=0
num = random.randint(999,10001)
print(num)
num_list=[int(x) for x in str(num)]
while True:
    count+=1
    cows, bulls = 0,0
    guess = int(input("guess a 4 digit number: "))
    guess_list=[int(x) for x in str(guess)]
    if guess == num:
        print("ur guess is correct!!")  
        print("u took {} chances: ".format(count))  
        break
    else:
        for i in range(4):
            if guess_list[i] == num_list[i]:
                cows+=1
            elif guess_list[i] in num_list:
                bulls+=1
        print("you have {} cows and {} bulls in {} chances ".format(cows,bulls,count))


