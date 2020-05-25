import random


def random_password(length):
    base_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'h', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                 '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*']
    password = ''
    for j in range(length):
        m = random.randint(0, len(base_char) - 1)
        password = password + base_char[m]
    return password
