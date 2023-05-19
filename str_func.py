def upper_str(string):
    """ Функция возвращает строку в верхнем регистре """
    upper_string = string.upper()
    return upper_string


def up_first_letter(string):
    """ Функция возвращает заглавными первые буквы каждого слова в строке """
    str_list = string.split(" ")
    upper_letter_str = []
    for word in str_list:
        up_letter_world = word.capitalize()
        upper_letter_str.append(up_letter_world)
    return ' '.join(upper_letter_str)
