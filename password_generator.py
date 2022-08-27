from string import digits, ascii_uppercase, ascii_lowercase, punctuation
from random import choice

n = input("Введите количество паролей для генерации: ")
def num(n):
    while True:
        if n.isdigit() == True:
            n = int(n)
            return n
        else:
            n = input("Пожалуйста, введите число, а не текст: ")
num = num(n)

l = input("Введите длину каждого пароля: ")
def length(l):
    while True:
        if l.isdigit() == True:
            l = int(l)
            return l
        else:
            l = input("Пожалуйста, введите число, а не текст: ")
length = length(l)

is_include_digits = input("Включать ли цифры? ").lower()
is_include_uppercase_letters = input("Включать ли прописные буквы? ").lower()
is_include_lowercase_letters = input("Включать ли строчные буквы? ").lower()
is_include_punctuation_chars = input("Включать ли символы пунктуации? ").lower()
is_include_ambiguous_chars = input("Включать ли неоднозначные символы \"il1Lo0O\"? ").lower()

chars = ""
def generator_of_safe_passwords(chars):       # Создаём строку из допустимых символов для генерации паролей
    if is_include_digits == "да":
        chars += digits
    if is_include_uppercase_letters == "да":
        chars += ascii_uppercase
    if is_include_lowercase_letters == "да":
        chars += ascii_lowercase
    if is_include_punctuation_chars == "да":
        chars += punctuation
    if is_include_ambiguous_chars == "да":
        chars += "il1Lo0O"
    return chars
chars = generator_of_safe_passwords(chars)

def generate_password(length, chars):         # Генерируем пароль на основе допустимых символов
    password = [choice(chars) for c in range(length)]
    return "".join(password)

for _ in range(num):                          # Цикл генерирует необходимое количество паролей
    print(generate_password(length, chars))