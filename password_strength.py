import re
import getpass


def take_blacklist(blacklist_file_path):
    with open(blacklist_file_path) as blacklist_file:
        black_list_text = blacklist_file.read()
    return black_list_text


def prepare_blacklist(blacklist_file_path=r'C:\password_blacklist'):
    black_list_text = take_blacklist(blacklist_file_path)
    blacklist = black_list_text.split('\n')
    return blacklist


def get_password_strength(password):
    good_pass_len = 6
    password_not_only_low_register = bool(password.lower() != password)
    password_not_only_upp_register = bool(password.upper() != password)
    password_include_numbers = re.search("[1-9]", password) is not None
    password_has_no_phone_number = re.search(".?\d.?.?\d{3}.?.?\d{3}.?\d{2}.?\d{2}", password) is None
    password_has_no_date = re.search("[0-3]\d.?[0-1]\d.?(\d{4}|\d{2})", password) is None
    password_has_no_car_number = re.search("[а-я]\d{3}[а-я]{2}(\d{2,3})?", password) is None
    password_include_special_characters = re.search("\W", password) is not None
    password_have_good_len = len(password) > good_pass_len
    password_have_great_len = len(password) > (good_pass_len * 2)
    password_not_in_blacklist = password not in prepare_blacklist()
    return sum(
        [password_not_only_low_register, password_not_only_upp_register, password_include_numbers,
         password_has_no_phone_number, password_has_no_date, password_has_no_car_number,
         password_include_special_characters, password_have_good_len, password_have_great_len,
         password_not_in_blacklist])


if __name__ == '__main__':
    password_for_assessment = getpass.getpass()
    print("Ваш пароль получает %d баллов из 10" % (get_password_strength(password_for_assessment)))
