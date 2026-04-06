import random
my_random_number = random.randint(1000,9999)

user_password = int(input("Enter a 4_digit PIN code: "))


if len(str(user_password)) < 4 or len(str(user_password)) > 4:
    print("Enter 4 digite")
   
elif user_password == my_random_number:
    print("GUT")
elif user_password != my_random_number:
    print("Failure! PIN code did not match")
    print(f"the computer generated this PIN {my_random_number}")
