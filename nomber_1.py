import ru_local

Taken = 0
date_tr = int(input(ru_local.NAME))

while Taken < 3:
    date_no = (input(ru_local.NAME_ONE))
    date_no = int(date_no)
    Taken = Taken+1
    if date_tr == date_no:
        print(ru_local.MEY,ru_local.SAVE)
    if date_tr != date_no:
        print(ru_local.NAME_THREE)
    if date_tr == date_no:
        break
if date_tr != date_no:
    Taken = str(Taken)
    date_tr = str(date_tr)
    print(ru_local.NAME_TWO)
if date_tr == date_no:
    Taken = str(Taken)
    date_tr = str(date_tr)
    print(ru_local.NAMEYER)


    pys_str = str(input(ru_local.ONEWORD))

one = 'love'


one_str = pys_str.replace('а','а' + one)
two_str = one_str.replace('о','о' + one)
three_str = two_str.replace('э','э' + one)
fore_str = three_str.replace('и','и' + one)
five_str = fore_str.replace('ы','ы' + one)
six_str = five_str.replace('е','е' + one)
seven_str = six_str.replace('ё','ё' + one)
eight_str = seven_str.replace('ю','ю' + one)
nine_str = eight_str.replace('у','у' + one)
ten_str = nine_str.replace('я','я' + one)

One_str = ten_str.replace('А','А' + one)
Two_str = One_str.replace('О','О' + one)
Three_str = Two_str.replace('Э','Э' + one)
Fore_str = Three_str.replace('И','И' + one)
Five_str = Fore_str.replace('Ы','Ы' + one)
Six_str = Five_str.replace('Е','Е' + one)
Seven_str = Six_str.replace('Ё','Ё' + one)
Eight_str = Seven_str.replace('Ю','Ю' + one)
Nine_str = Eight_str.replace('У','У' + one)
Ten_str = Nine_str.replace('Я','Я' + one)

print('')
print(Ten_str)


