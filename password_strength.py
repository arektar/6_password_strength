import re
import getpass


def take_blacklist(blacklist_file_path):
    with open(blacklist_file_path) as blacklist_file:
        black_list_text = blacklist_file.read()
    return black_list_text


def prepare_blacklist(blacklist_file_path):
    black_list_text = take_blacklist(blacklist_file_path)
    blacklist = black_list_text.split('\n')
    return blacklist


def get_password_strength(password, blacklist_file_path):
    good_pass_len = 6
    not_only_low_register = password.lower() != password
    not_only_upp_register = password.upper() != password
    include_numbers = re.search("[1-9]", password) is not None
    no_phone_number_found = re.search(".?\d.?.?\d{3}.?.?\d{3}.?\d{2}.?\d{2}", password) is None
    no_date_found = re.search("[0-3]\d.?[0-1]\d.?(\d{4}|\d{2})", password) is None
    no_car_number_found = re.search("[а-я]\d{3}[а-я]{2}(\d{2,3})?", password) is None
    include_special_characters = re.search("\W", password) is not None
    good_len = len(password) > good_pass_len
    great_len = len(password) > (good_pass_len * 2)
    no_stop_words = password not in prepare_blacklist(blacklist_file_path)
    return sum(
        [not_only_low_register, not_only_upp_register, include_numbers,
         no_phone_number_found, no_date_found, no_car_number_found,
         include_special_characters, good_len, great_len,
         no_stop_words])


if __name__ == '__main__':
    blacklist_path = input("Введите путь к файлу исключений: ")
    password_for_assessment = getpass.getpass()
    print("Ваш пароль получает %d баллов из 10" % (get_password_strength(password_for_assessment, blacklist_path)))
