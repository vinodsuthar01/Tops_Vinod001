from datetime import datetime
records = []

def calc_days(d1,d2):
    try:
        date1 = datetime.strptime(d1,"%Y-%m-%d")
        date2 = datetime.strptime(d2,"%Y-%m-%d")
    except:
        date1 = datetime.strptime(d1,"%d-%m-%Y")
        date2 = datetime.strptime(d2,"%d-%m-%Y")
    finally:
        total_days = date1 - date2
    return total_days.days

def rent_book():
    data = {
        "cust_name" : "",
        "book_title" : "",
        "date_of_rent" : "",
        "expected_return" : "",
        "price_day" : 5
    }
    
    for i in data:
        if i == "price_day":
            change_p = input("are you want to change rent price of a day enter(y/n) : ")
            if change_p == "y":
                data.update({i:int(input(f"{i} : "))})
            continue
        data.update({i:input(f"{i} : ")})
        
        if i == "expected_return":
            k = (calc_days(data.get(i),data.get("date_of_rent")))
            while k <= 0:
                data.update({i:input("date must not less than from date of rent...")})
                k = (calc_days(data.get(i),data.get("date_of_rent")))
    records.append(data)

def return_book():
    search = input("Enter Cust Name : ")
    for i in records:
        if search in i.get("cust_name"):
            return_date = input("enter return date : ")
            d1 = i.get("expected_return")
            d2 = i.get("date_of_rent")
            price = i.get("price_day")
            d = calc_days(return_date,d1)
            dayss = calc_days(d1,d2)
            if d==0:
                rent = calc_rent(dayss,price)
                i.update({"rent" : rent})
            elif d > 0:
                rent = calc_rent(dayss,price)
                d*= price*2
                rent+=d
                i.update({"book_returned" : return_date})
                i.update({"rent" : rent})
            elif d < 0:
                dayss = calc_days(return_date,d2)
                rent = calc_rent(dayss,price)
                i.update({"book_returned" : return_date})
                i.update({"rent" : rent})
            
            title = "_____custmor bill_____"
            print(title)
            for items in i:
                print(items," : ",i.get(items))
            print("----------------------")


def calc_rent(dayss,price):
    rent = dayss*price
    return rent

while True:
    option = input("""1. rent a book
2. return a book
3. exit program
enter op: """)
    if option == "1":
        rent_book()
    elif option == "2":
        return_book()
    elif option == "3":
        print("exit program")
        break
    else:
        print("invalid choice")

