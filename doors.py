# Problem: We have 100 doors are closed
# In the first iteration will open all doors
# from the second iteration we need to close doors from the second door like: 2, 4, 6, etc.
# in the third iteration we need to change the door state from the third door like 3, 6, 9, etc.
# at the final iteration we need to count how many door remains open


def count_open_doors():
    doors = [False] * 101
    for i in range(1, 101):
        for j in range(i, 101, i):
            doors[j] = not doors[j]
        if doors[i] is True:
            print("Door number", i, "is open")
    print("Total number of open doors:", doors.count(doors[True]))


count_open_doors()
