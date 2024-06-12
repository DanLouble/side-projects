import datetime

current = datetime.datetime.today()
print(current)

birthday = datetime.datetime.strptime(input("enter your date of birthday in the form yyyy/mm/dd "),'%Y/%m/%d')


diff = current - birthday
print("you've lived for",diff.days,"months")