import re
import getpass


def take_blacklist(blacklist_file_way='password_blacklist'):
    with open(blacklist_file_way) as blacklist_file:
        black_list_text = blacklist_file.read()
    return black_list_text


def check_in_blacklist(password):
    password_in_blacklist = False
    if password in take_blacklist().split('\n'):
        password_in_blacklist = True
    return password_in_blacklist


def get_password_strength(password):
    good_pass_len = 6
    not_only_low_reg = bool(password.lower() != password)
    not_only_upp_reg = bool(password.upper() != password)
    include_numbers = re.search("[1-9]", password) is not None
    has_no_phone_number = re.search(".?\d.?.?\d{3}.?.?\d{3}.?\d{2}.?\d{2}", password) is None
    has_no_date = re.search("[0-3]\d.?[0-1]\d.?(\d{4}|\d{2})", password) is None
    has_no_car_number = re.search("[а-я]\d{3}[а-я]{2}(\d{2,3})?", password) is None
    include_special_characters = re.search("\W", password) is not None
    good_len = len(password) > good_pass_len
    great_len = len(password) > (good_pass_len * 2)
    not_in_blacklist = check_in_blacklist(password) is False
    return sum(
        [not_only_low_reg, not_only_upp_reg, include_numbers, has_no_phone_number, has_no_date, has_no_car_number,
         include_special_characters, good_len, great_len, not_in_blacklist])


if __name__ == '__main__':
    my_password = getpass.getpass()
    print("Ваш пароль получает %d баллов из 10" % (get_password_strength(my_password)))
