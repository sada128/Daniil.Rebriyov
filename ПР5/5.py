#Задание 1
words = "яблоко строка егерь еще"
count = 0
for word in words.split(" "):
    if word.strip()[0] == 'е':
        count +=1
print(count)
#Задание 2
text = input('')
if text.replace(':', ('%')):
    print(text)
else:
    print('Тут нет запятых!')
#Задание 6
string="aaaBaaaHE"
counti = len(string) - len(string.replace("a", ""))
print(string)
print(str(counti))

    