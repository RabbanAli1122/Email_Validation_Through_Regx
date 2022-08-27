#wscube@gmail.com
import re
def Wrong_Email_Errors(error_number):
    print("Email incorrect!\nError number:", error_number)
    int(input("Enter 1 for error detail and enter 0 to exit the email checking:"))
    if error_number == 1:
        print("Error number:1\n"
              "Which means that your email is shorter than the minimum email length\n"
              "Which is not valid.")
        return ""
    elif error_number == 2:
        print("Error number:2\n"
              "Which means that email length is more than 6 letters but it is not \n"
              "fulfilling some other valid email conditions\n"
              "Which is not valid.")
        return ""
    else:
        print("An unexpected error occurred")
        return ""
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email:\n")
if len(user_email) >=6:
    if re.search(email_condition,user_email):
        print("Right Email")
    else:
        print(Wrong_Email_Errors(error_number=2))
else:
    print(Wrong_Email_Errors(error_number=1))
