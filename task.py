import datetime
from collections import OrderedDict 
import re

def getNextDate(date1):
    NextDay_Date = date1 + datetime.timedelta(days=1)
    return (NextDay_Date)

def convertStrToDate(s1):
    obj=datetime.datetime.strptime(s1,'%Y-%m-%d')
    return obj.date()

def convertDateToStr(date1):
    str1=date1.strftime("%Y-%m-%d")
    return str1

def checkDateValid(s1):
    if(re.search('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',s1)==None):
        print ("Input date is not valid..")
        return False
    year,month,day = s1.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    if(isValidDate) :
        return True
    else :
        print ("Input date is not valid..")
        return False

def solution(d):
    ans={}
    key=list(d)[0]
    ans[key]=d[key]
    i=1
    j=0
    while(i<len(d)):
        key1=list(d)[i]
        value1=d[key1]
        key2=list(ans)[j]
        value2=ans[key2]
        next_date=convertStrToDate(key1)
        prev_date=convertStrToDate(key2)
        prev_next_date=getNextDate(prev_date)
        if(prev_next_date != next_date):
            days_diff=(next_date-prev_date).days
            s1=convertDateToStr(prev_next_date)
            ans[s1]=value2 + int((value1-value2)/days_diff)
            j+=1
        else:
            ans[convertDateToStr(prev_next_date)]=value1
            i+=1
            j+=1

    return ans

def main():
    # d={"2019-01-01":100,"2019-01-04":115}
    # d={"2019-01-10":10,"2019-01-11":20,"2019-01-13":10}
    # d={"2019-01-31":10,"2019-02-02":20,"2019-02-05":20}
    n= int(input("Enter no. of elements to be inserted in dictionary: "))
    d=dict()
    i=0
    while i<n:
        key=input("Enter date key in 'YYYY-MM-DD' format: ")
        check=checkDateValid(key)
        if(check==False):
            continue
        value=int(input("Enter value: "))
        d[key]=value
        i+=1
    d=OrderedDict(sorted(d.items(),key = lambda x:x[0]))
    print("\nOriginal Dictionary:")
    print(d)
    d=solution(d)
    print("\nResult: ")
    print(d)

if __name__ == "__main__":
    main()