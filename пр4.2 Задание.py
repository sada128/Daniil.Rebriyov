text = input('')
x = text.replace(':', '%')
if x != text :
    print(("Код работает\n"),x.count("%"), ("Замен\t"), x)
else: 
    print("Тут нет ""':'"" :-( ")
