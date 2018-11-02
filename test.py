def triangle(angle1, angle2):
    return 180 - angle1 - angle2

user_angle1 = input("What is angle one of the triangle?")
user_angle2 = input("What is angle two of the triangle?")

print("The third angle of the triangle is: ", triangle(user_angle1, user_angle2))

input("Press any key to continue...")
