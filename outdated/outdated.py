def main():
    convert_date()
def convert_date():
    months_a = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    months_ab = [

    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
    ]
    month_n = range(12)
    days_m = range(31)
    while True:
        user_input = input("Date: ") #taking user's date input
        if user_input.find("/"):#handling dates in the format 8/9/1996
            user_input = user_input.split("/")
            month = user_input[0]
            day = user_input[1]
            year = user_input[2]
        elif user_input.find(","):#handling dates with month spellings and comma
            user_input = user_input.split(", ")
            u1 = user_input[0].split(" ")[0]
            u2 = user_input[0].split(" ")[1]
            year = user_input[2]
            if u1.isnumeric():
                day = u1
                month = u2
            else:
                month = u1
                day = u2

        else:#handling dates with months spelling without comma
            user_input = user_input.split(" ")
            day = user_input[0]
            month = user_input[1]
            year = user_input[2]
        if month in months_a:#checking if month was sully spelt
            try:
                d = days_m.index(day)
                m = months_a.index(month)
            except ValueError:
                pass
            else:#printin out date
                print(f"{year}-{m:02}-{d:02}")
        if month in month_ab:
            try:
                d = days_m.index(day)
                m = months_a.index(month)
            except ValueError:
                pass
            else:#printin out date
                print(f"{year}-{m:02}-{d:02}")






main()

