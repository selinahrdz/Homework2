import cipher

database_file = open("database.txt","r")
for student in database_file:
    student_data = student.rstrip("\n")
    split_name = student_data.split(" ",1)
    userid = split_name[0]
    password = split_name[1]
    decrypt_userid = cipher.decrypt(userid, 3,+1)
    decrypt_password = cipher.decrypt(password,3,+1)
    print("Userid: " + decrypt_userid + "\n" + "Password: " + decrypt_password + "\n")


database_file.close()

# 1. Which of the userid and password combination(s) in the table above are present in the database?
# Userid: asamant Password: Temp123
# Userid: skharel Password: Life15$

# 2. Which userid(s) is/are present in the database, but the password does not match the password(s) in the table above?
# Userid: aissa
# Userid: bjha

# 3. Which userid(s) do/does not meet the requirements of a userid?
# Userid: Ally!
