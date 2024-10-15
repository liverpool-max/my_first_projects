import json
import re
import string
def bank_application():
    while True:
        lower=list(string.ascii_lowercase)
        upper=list(string.ascii_uppercase)
        special_character=["@","!","?","_","#"]
        numbers=[x for x in range(10)]
        try:
            response = int(input("daxil olmaq üçün 1\nqeydiyyat üçün 2\nproqramı başa çatdırmaq üçün 3\n1/2/3: "))
        except:
            print("Zəhmət olmasa yuxarıda qeyd olunanlardan birini seçin ")
        else:
            if response == 2:
                username = input("enter the username: ")
                password = input("enter the password: ")
                k = " "
                try:
                    balance = int(input("enter the balance:"))
                except:
                    print("Yalnız ədəd daxil edin...")
                else:
                    with open("data.json",mode="r",encoding="utf-8") as f:
                        try:
                            ls_persons=json.load(f) 
                        except:
                            ls_persons=[]
                    ls1=[]       
                    for j in ls_persons:
                        if j["username"]==username:
                            ls1.append(True)
                        else:
                            ls1.append(False)
                    if True in ls1:
                        print("Bu ad istifade olunub")
                    else:
                        if balance < 0:
                            print ("Balans müsbət olmalıdır...")
                        elif len(username) <= 4:
                            print ("İstifadəçi adı minimum 4 hərf olmalıdır... ")
                        elif len(password) <= 4:
                            print("Şifrə 4 hərfdən çox olmalıdır... ")
                        elif k in password:
                            print("Şifrədə boşluq ola bilməz...")
                        elif k in username:
                            print("İstifadəçi adında boşluq olmamalıdır...")
                        elif username==password:
                            print("İstifadəçi adı ilə parol eyni ola bilməz...")
                        elif re.search(str(lower),password) is None:
                            print("Şifrədə minimum 1 ədəd balaca hərf istifadə olunmalıdır...")
                        elif re.search(str(upper),password) is None:
                            print("Şifrədə minimum 1 ədəd böyük hərf istifadə olunmalılır...")
                        elif re.search(str(numbers),password) is None:
                            print("Şifrədə minimum 1 ədəd rəqəm istifadə olunmalıdır")
                        elif re.search(str(special_character),password) is None:
                            print(f"Şifrədə minimum 1 ədəd xüsusi simvol istifadə etməlisiniz \nYalnız bu simvolları istifadə edə bilərsiniz {special_character}")
                        else:
                            data={"username": username, "password":password, "balance": balance} 
                            ls_persons.append(data)
                            with open("data.json",mode="w",encoding="utf-8") as f:
                                json.dump(ls_persons,f,indent=4)
                            print( "Siz qeydiyyatdan uğurla keçmisiniz...")
                            print(f"Hörmətli {username}, Orxan MMC-yə xoş gəlmisiniz...")
                            
            elif response == 1:
                login()
            elif response == 3:
                return  "Hörmətli müştəri\nProqram başa çatdı\nXidmətimizdən istifadə etdiyiniz üçün təşəkkürlər:)\n012-211-00-00 əlaqə nömrəsi ilə bizimlə əlaqə saxlaya bilərsiniz..."
            else:
                print("Zəhmət olmasa yuxarıda qeyd olunanlardan birini seçin ")
            

def login():
    login_username = input("enter the login_username: ")
    login_password = input("enter the login_password: ")
    with open("data.json","r",encoding="utf-8") as file:
        try:
            ls_persons=json.load(file) 
        except:
            ls_persons=[]
        for line in ls_persons:
            if line['username']==login_username and line['password']==login_password:
                while True:
                    try:
                        question = int(input("balansı görmək üçün 2\nbalansı artırmaq üçün 3\nbalansdan pul çıxarmaq üçün 4\n2/3/4: "))
                    except:
                        print("Yuxarıda qeyd olunan rəqəmlərdən birini seçməklə əməliyyatları icra edə bilərsiniz:)")
                    else:
                        if question == 2:
                            with open("data.json","r",encoding="utf-8") as file:
                                try:
                                    ls_persons=json.load(file) 
                                except:
                                    ls_persons=[]
                            for line in ls_persons:
                                if line['username']==login_username and line['password']==login_password:
                                    print("Sizin balansınız: ", line["balance"])
                        elif question == 3:
                            increase_the_balance = int(input("Artırmaq istədiiyiniz balansı qeyd edin: "))
                            if increase_the_balance > 0:
                                for line in ls_persons:
                                    if line['username']==login_username and line['password']==login_password:
                                        new_balance = line['balance'] + increase_the_balance
                                        ls_persons.remove(line)
                                        ls_persons.insert(0, {'username': login_username, 'password': login_password, 'balance': new_balance})
                                        with open('data.json', 'w', encoding='utf-8') as file:
                                            json.dump(ls_persons, file, indent=4)
                                        print("Yeni balans:",new_balance)
                                        break
                            else:
                                print("Mənfi balans daxil edilə bilməz...")
                        elif question == 4:
                            decrease_the_balance = int(input("Çıxarmaq istədiyiniz balansı qeyd edin: ")) 
                            if decrease_the_balance>0:
                                while True:
                                    if line["balance"] > decrease_the_balance :
                                        for line in ls_persons:
                                            if line['username']==login_username and line['password']==login_password:
                                                new_balance1 = line['balance'] - decrease_the_balance
                                                ls_persons.remove(line)
                                                ls_persons.insert(0, {'username': login_username, 'password': login_password, 'balance': new_balance1})
                                                with open('data.json', 'w', encoding='utf-8') as file:
                                                    json.dump(ls_persons, file, indent=4)
                                                print("Yeni balans:",new_balance1)
                                        break
                                    else:
                                        print("Balansınızda kifayət qədər məbləğ yoxdur...")
                                        break   
                            else:
                                print("Mənfi balans çıxara bilmərsiniz...")
                        else:
                            print("Zəhmət olmasa yuxarda qeyd olunan rəqəmlərdən birini seçin")
                            continue
                        check = input("davam etmək istəyirsizinsə 'hə', proqramı başa çatdırmaq istəyirsinizsə 'yox'\nhə/yox: ")
                        if check == "hə":
                            continue
                        elif check != "hə" and check != "yox":
                            print("Yalnız yuxarıda olan hə və yaxud yoxu qeyd edin...")
                        elif check == "yox":
                            return "Başa çatdı"
                                 
        else:
            print( "İstifadəçi adı və ya parolunuz səhvdir...")   
print(bank_application())                                                                                                                                                                                                                                                                                                                                                                           


