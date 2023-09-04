from random import randint


if __name__ == "__main__":
    # # task one
    # while True:
    #     try:
    #         num_one = int(input("введіть перше число "))
    #         num_two = int(input("введіть друге число "))
    #         break
    #     except ValueError:
    #         print("ввдити можна лише цифри!")
    #
    # operation = input("виберіть доступну дію:  +, -,*,/")
    #
    # if operation == "+":
    #     print(f"отож {num_one} + {num_two} = {num_two+num_one}")
    # elif operation == "-":
    #     print(f"отож {num_one} - {num_two} = {num_one-num_two}")
    # elif operation == "*":
    #     print(f"отож {num_one} * {num_two} = {num_one*num_two}")
    # elif operation == "/":
    #     if num_two != 0:
    #         print(f"отож {num_one} / {num_two} = {num_two / num_one}")
    #     else:
    #         print("ділити на нуль не можна!")

    # task two
    while True:
        try:
            min_arr = int(input("введіть початкове значення списку"))
            max_arr = int(input("введіть кінцеве значення списку"))
            arr_length = int(input("введіть довжину списку"))
            break
        except ValueError:
            print("вводити можна лише цілі цифри")

    if min_arr > max_arr:
        print("ви ввели мінімальне значення більшим, ніж максимальне. Значення були автоматично замінені!")
        temp_min_arr = max_arr
        max_arr = min_arr
        min_arr = temp_min_arr

    num_arr = []
    zero_arr = []
    negative_nums_arr = []
    positive_nums_arr = []

    for i in range(arr_length):
        randint_num = randint(min_arr, max_arr+1)
        num_arr.append(randint_num)
        if i > 0:
            positive_nums_arr.append(i)
        elif i < 0:
            negative_nums_arr.append(i)
        else:
            zero_arr.append(i)

    print(f"Отож в цьому списку є:\n {len(positive_nums_arr)} елементів більших від нуля ось їх список: "
          f"{positive_nums_arr}\n"
          f"{len(negative_nums_arr)} елементів менших від нуля ось їх список: {negative_nums_arr}\n"
          f"{len(zero_arr)} елементів  рівних нулю ось їх список: {zero_arr}")






