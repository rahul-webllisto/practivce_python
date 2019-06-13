
print("Welcome to the birthday dictionary. We know the birthdays of:")
birthdays = {'john': '11/12/90', 'jane': '25/11/98'}
for birthday in birthdays.keys():
     print(birthday)

name = input("Who's birthday do you want to look up? ")
if name in birthdays:
    print(birthdays[name])
else:
    print("We don't have the birthday of {} ".format(name))
    