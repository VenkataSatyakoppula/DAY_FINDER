from time import sleep
def leap(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True 
            else:  
                return False  
        else:  
            return True 
    else:  
        return False
def checker(my_list):
    if(int(my_list[1])>12 or int(my_list[0])>31 or int(my_list[0])<=0):
        return False
    else:
        if(int(my_list[1])==2):
            if(leap(int(my_list[2]))):
                return int(my_list[0])<=29
            else:
                return int(my_list[0])<29   
        elif((int(my_list[1])%2==0 and int(my_list[1])<8) or (int(my_list[1])>8 and int(my_list[1])%2!=0)):
                return int(my_list[0])<31 
        else:
            return True
def no_of_days(my_list,month):
    i=0
    days=0    
    while(i<int(my_list[1])-1):
        if(i==1 and leap(int(my_list[2]))!=True):
            days = days + month[i] + 28
        else:
            days = days + month[i] + 29    
        i = i + 1    
    return (days + int(my_list[0]))%7       
        
if __name__ == "__main__":
    print("""
        *********************************
        ********DAY FINDER CODE**********
        *********************************
                        -by Venkata satya
        """
    )
    print()
    sleep(2)
    date = input("Enter the date (dd/mm/yyyy) = ")
    my_list = list(map(str.strip, date.split('/')))
    odd_in_month = [2,0,2,1,2,1,2,2,1,2,1,2]
    year=int(my_list[2])-1
    i=1
    j=0
    odd=0
    if(checker(my_list)):
        if(year<=400):
            rem=year
        else:
            rem=year%400  
        while(i<=rem):
            if(leap(year-rem+i)):
                odd = odd +2
            else:
                odd = odd +1
            i = i+1 
    else:
        print("""
        **********************
        **Enter a valid date**
        **********************
        """)
        exit()        
    odd_days = (no_of_days(my_list,odd_in_month) + odd)%7
    month = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    
    print(f"""
        *************************
        {date} is {month[odd_days]}
        *************************

        THANKYOU FOR USING :)
        """
        )








