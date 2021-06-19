import datetime
corrent_time_and_date=datetime.datetime.now()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
print(corrent_time_and_date)
# hour = int(input("enter your hour:- "))
# if hour > 0 and hour < 12 :
#     print("good morning")
# elif hour >= 12 and hour <=18:
#     print("good afternoon")
# else:
#     print("good evening")


if __name__ == "__main__" :          #this is nothing this is true condition
    print('jai mata di')
else:
    print("not equal")