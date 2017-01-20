import re


def check_in_blacklist(password):
    blacklist_file_way = 'password_blacklist'
    password_in_blacklist = False
    with open(blacklist_file_way) as blacklist_file:
        if password in blacklist_file.read().split('\n'):
            password_in_blacklist = True
    return password_in_blacklist


def get_password_strength(password):
    good_pass_len = 8
    great_pass_len = 12
    pass_power = 0
    re_phone_number = re.search(".?\d.?.?\d{3}.?.?\d{3}.?\d{2}.?\d{2}", password)
    re_date = re.search("[0-3]\d.?[0-1]\d.?(\d{4}|\d{2})", password)
    re_car_number = re.search("[а-я]\d{3}[а-я]{2}(\d{2,3})?", password)
    if password.lower() != password:
        pass_power += 1
    if password.upper() != password:
        pass_power += 1
    if re.search("[1-9]", password).group(0):
        pass_power += 1
        if not re_phone_number.group(0):
            pass_power += 1
        if not re_date.group(0):
            pass_power += 1
        if not re_car_number.group(0):
            pass_power += 1
    if re.search("\W", password).group(0):
        pass_power += 1
    if len(password) > good_pass_len:
        pass_power += 1
        if len(password) > great_pass_len:
            pass_power += 1
    if not check_in_blacklist(password):
        pass_power += 1
    return pass_power


if __name__ == '__main__':
    my_password = input("Write password: ")
    print("Ваш пароль получает %d баллов из 10" % (get_password_strength(my_password)))
