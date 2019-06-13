import random

def pickword():
    with open('dictionary.txt','r') as f:
        contents = f.readlines()       
    word = random.choice(contents)          
    letters={}
    while True:
        guess = input("Guess ur letter: ").strip().upper()
        if guess in word:
            for i in range(len(word)-1):
                if guess == word[i]:                 
                    letters[i] = guess 
                    continue            
            items = sorted([x for x in letters.keys()])                                                
            for k in range(len(word)-1):                                 
                if k in items:
                    print(letters[k],end=" ")                                                                    
                else:
                    print("_",end=" ")             
            
            if len(items) == len(word)-1:
                print("\nU WON") 
                break
            print()
        else:
            print("Incorrect!")


if __name__ == "__main__":
    pickword()

