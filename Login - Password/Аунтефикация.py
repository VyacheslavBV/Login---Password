print('1 - Регистрация'+'\n'+'2 - Вход')
i=int(input())
if i == 1:
    o=open('data.txt')
    ind=len(list(o))+1
    print('Вам присвоен индивидуальный номер:',str(ind))
    print("Создайте пароль")
    f=str(input())
    print("Ваши данные")
    h = str(input())
    o.close()
    o=open('data.txt','a')
    o.write(str(ind)+' '+ str(f)+' '+str(h)+'\n' )
elif i==2:
    print('Введите индивидуальный номер')
    n=str(input())
    o=open('data.txt')
    d=0
    while d==0:
        s=str(o.readline())
        s=list(s.split())
        try:
            if s[0]==n:
                d=1
                print('Введите пароль от учетной записи')
                p=str(input())
                if s[1]==p:
                    print('Вход завершен успешно')
                    print(s[2])
                else:
                    print('Неверный пароль')
        except IndexError:
            d=1
            print('Учетная запись не найдена')

o.close()