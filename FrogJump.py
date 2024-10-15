def frog_jump():
    position_x = int(input("Type in position X "))
    position_y = int(input("Type in position Y "))
    jump_force = int(input("Type jump force "))

    if position_y > position_x:
        num_of_jump = int((position_y - position_x)/jump_force) + 1
        print(f"The minimal number of jump from {position_x} to {position_y} is {num_of_jump}")
    else:
        print("Invalid input")


frog_jump()
