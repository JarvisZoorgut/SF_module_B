f = open('test.txt', 'a', encoding='utf8')

# Запишем в файл строку
f.write("This is a test string\n")
f.write("This is a new string\n")

f = open('test.txt', 'r', encoding ="utf8")
print(f.read(10))
print(f.read())
f.close()

print()

f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись

sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берет строки из sequence и записывает в файл (без переносов)

f.close()

print()

f = open('test.txt', 'r', encoding='utf8')

print(f.readlines())  # считывает все строки в список и возвращает список

f.close()

print()

f = open('test.txt', 'r', encoding='utf8')

print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline(10))  # is a new string
print(f.readline())  # This is a test string

print(f.read())
print(f.tell())

f.close()