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
        if user_input.find("/"):
            user_input = user_input.split("/")
            month = user_input[0]
            day = user_input[1]
            year = user_input[2]
        elif user_input.find(","):
            user_input = user_input.split(", ")
            month = user_input[0].split(" ")[0]
            days = user_input[0].split(" ")[1]
            


main()

