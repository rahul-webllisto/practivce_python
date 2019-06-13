import datetime


def cal_year100(name,age):
    current_year=datetime.datetime.now().year
    yr_100 = current_year + 100-age
    print("hello {} you wil be 100 in {} ".format(name,yr_100))    


if __name__ == '__main__':

    name = input("enter ur name: ")
    age = int(input("enter ur age: "))
    cal_year100(name,age)
