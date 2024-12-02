def check_vowel():
    for vowel in ["a", "e", "i", "o", "u"]:
        if vowel in password:
            return True
    return False


def check_triple():
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(password[:-2])):
        if password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels:
            return False
        if password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels:
            return False
    return True


def check_double():
    for i in range(len(password[:-1])):
        if password[i] == password[i+1]:
            if password[i] != "e" and password[i] != "o":
                return False
    return True


while True:
    password = input()
    if password == "end":
        break

    if not check_vowel():
        print(f"<{password}> is not acceptable.")
        continue

    if not check_triple():
        print(f"<{password}> is not acceptable.")
        continue

    if not check_double():
        print(f"<{password}> is not acceptable.")
        continue

    print(f"<{password}> is acceptable.")






