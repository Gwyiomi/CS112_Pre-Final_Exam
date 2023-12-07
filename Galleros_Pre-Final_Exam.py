print("{:>60}".format("* " * 25))
print("{:>11}{:^58}*".format("*", "\033[1;95mP R I M E  N U M B E R S\033[0m"))
print("{:>60}\n{:>36}\n".format("* " * 25, "By: Gwynette Galleros CS1D"))


prime_number = []

while True:
    num_start = int(input("Enter a number [start]: "))
    if num_start < 0:
        print("Enter a non-negative number\n")
        continue
    elif num_start == 0:
        print("\033[91mPROGRAM TERMINATED\033[0M")
        break
    num_end = int(input("Enter a number [end]: "))
    if num_start >= num_end:
        print(f"Invalid Input. Enter a number greater than {num_start}\n")
    for num in range(num_start, num_end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_number.append(num)
    if num_start < num_end:
        print(f"Prime numbers between {num_start} and {num_end} are: \033[93m " + " ".join(map(str, prime_number)), "\033[0m")
        prime_number.clear()
        print()
