#wap to input userid from user check whether the id follows the given pattern
#all char are uppercase the id starts with USER followed  by 3 digits followed by one special char followed by any number of char

import re #even if we are importing its not a lib or package but a module
user_id=input("enter user id: ")
pattern=r"^user\d{3}[^A-Za-z0-9][A-Za-z]+$"
if re.fullmatch(pattern,user_id):
    print("valid")
else:
    print("not valid")