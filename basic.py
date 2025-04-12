
# ? dökümasyon https://docs.python.org/3/library/

#! temel adımlar

class basicsVerbs():
    #! bu da bir fonksiyon(def) ikiyle_carp = lambda sayı: sayı*2
    def variablesVerb():
        print("hello world!")
        sayi = 10  # integer
        tc = "10101010108"  # string
        isim = "Fahri"
        soyisim = "aydın"
        telefonNumarasi = "5354444444"
        floatSayi = 10.0
        lenght = "Fahri AYDIN"
        print(len(lenght))
        print(float(tc) + 10)
        print(type(floatSayi))
        print(type(sayi))
        print(type(tc))
        print(*"Fahri{} ADYIN".format(1), sep=".")
        print("alt\n satıra geçme kodu")
        # bireden fazla satıra string yazmak için üç tırnak kullanılmalıdır [""" """]
        print("""
        fazla satır
        yazı
        yazma
        """)

    def evalVerb():
        # eval bizim verdiğimiz paremetreyi python kodu gibi davranır ve o şekilde kodu işler
        hesapla = input("""
        Yapmak istediğiniz işlmei giriniz
        toplama(+)
        çıkarma(-)
        bölme(/)
        çarpma(*)
        işlem :
        """)
        print(eval(hesapla))

    def stringsVerb():
        # substring
        mesaj = "Merhaba dünya"
        print(mesaj[2:5])
        yeniMesaj = mesaj[12:13]
        print(yeniMesaj)

        # len
        print(len(mesaj))
        yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
        print(yeniMesaj2)

        # lower upper
        print(mesaj.upper())
        print(mesaj.lower())

        # replace
        # mesaj = mesaj.replace("ü","u")
        print(mesaj.replace("ü", "u"))
        print(mesaj)
        print(mesaj.replace("a", "e"))

        # split ve strip
        bilgi = "     Fahri;aydın;33;Ankara ".strip()
        print(bilgi.split())
        print("Adı = " + bilgi.split(";")[0])

        # input
        ad = input("Adınız?")
        sayi1 = input("Sayı 1 =? ")
        sayi2 = input("Sayı 2 =? ")
        print(int(sayi1) + int(sayi2))

        # ends with
        sehir = "Ankara"
        sonuc = sehir.upper()
        print(sonuc)
        print(sehir.endswith("e"))

    def listStarts():
        #!list []
        #! set {}
        #!tuple () fonksiyonları .index(x),.count()
        #!dict {"1":"bir", "2":"iki", "3":"üç"}
        # ogrenci1 = "Fahri"
        # ogrenci2 = "ayşe"
        # ogrenci3 = "selin"
        #
        # print(ogrenci1)
        # print(ogrenci2)
        # print(ogrenci3)

        students = ["Fahri", "ayşe", "selin"]

        students.append("Ahmet")
        # students[4] = "Veli"
        print(students[3])
        students.remove("selin")
        print(students)

        # list constructor
        sehirler = list(("Ankara", "İstanbul", "Ankara"))
        print(sehirler)
        print(len(sehirler))

        # diğer fonksiyonlar
        # print(sehirler.clear())
        print("Ankara sayısı = " + str(sehirler.count("Ankara")))
        print("Ankara indexi = " + str(sehirler.index("Ankara")))
        sehirler.pop(1)
        sehirler.insert(0, "İstanbul")
        sehirler.reverse()
        print(sehirler)

        sehirler3 = sehirler.copy()

        sehirler2 = sehirler
        sehirler2[0] = "İzmir"

        print(sehirler2)
        print(sehirler)
        print(sehirler3)

        sehirler.extend(sehirler3)
        sehirler.sort()
        sehirler.reverse()
        print(sehirler)

    def listsVerb():
        #!list []
        #! methotları .append("x"),.pop(),.sort(),.sort(reverse = True)
        #! kopyalama liste_kopya = list(liste1) ,liste_kopya = liste1.copy()
        def listMigrate():
            liste1 = [7, 8, 9]
            liste2 = [4, 5, 6]
            liste_toplam = liste1 + liste2
            print(liste_toplam)
        listMigrate()
        liste = [[1, 2], [2, 3], [4, 5]]
        liste[1][0]
        studentsSet = {"Fahri", "Selin", "Salih", "Ahmet"}
        studentsSet2 = set("Mehmet", "Veli", "Ayşe")
        print(studentsSet)

        for student in studentsSet:
            print(student)

        print("Selin" in studentsSet)

        if "Selin" in studentsSet:
            print("Listede var")

        studentsSet.add("Ali")
        print(studentsSet)

        studentsSet.update(["Merve", "Mert", "Selin"])
        print(studentsSet)

        print(len(studentsSet))
        # ! istenilen kısma verilen elemanı ekler
        studentsSet.insert(3, "fatma")

        studentsSet.remove("Selin")
        print(len(studentsSet))

        studentsSet.discard("Selin")
        print(len(studentsSet))

        x = studentsSet.clear()
        print(len(studentsSet))
        del studentsSet
        print(studentsSet)

    def dictionaries():
        #!dict {"1":"bir", "2":"iki", "3":"üç"}
        #! methotları .keys() ,.values(),.items(),.pop()
        sozluk = {
            "book": "kitap",
            "table": "masa"
        }
        sozluk2 = dict(kitap="book", masa="table")

        sozluk["book"] = "kitap 1"
        sozluk2["pencil"] = "kalem"
        del (sozluk["book"])
        print(len(sozluk))

    def tuplesVerb():
        #!tuple () fonksiyonları .index(x),.count()
        tupleListe = (2, 4, 6, "Ankara", (2, 3, 4), [])
        liste = [2, 4, 6, "Ankara", [3, 4, 5], ()]
        liste[0] = 6
        # tupleListe[0]=6

        tupleDeger = ("Fahri",)
        print(type(tupleDeger))

        print(tupleListe[1:2])
        print(liste[1:2])

        print(tupleListe[-2])
        print(liste[-2])

        print(type(tupleListe))
        print(type(liste))
        print(tupleListe)
        print(liste)
        print(len(tupleListe))
        print(len(liste))

        tuple_indeks = ("Apple", "Facebook", "Google", "Amazon")
        tuple_indeks.index("Facebook")
        tuple2 = (9, 9, 9, 5, 5, 5, 1)
        tuple2.count(9)

    def setsVerb():
        # değişken = {data} veya değişken = set([data])
        # frozen = frozenset([data]) sadece okunur yazılamaz (only read) tuple'lara benzer
        # bir indexleri yoktur.
        # diğer isimleri 'küme'dir.
        # ? birleşim , | , .union(setB)
        # ? fark , - , difference
        # ? kesişim , & , intersection
        # * Aynı eleman girilemez kümlerdeki bütün elemanlar birbirinden farklıdır.
        # .union(set), .intersection(set).difference(set),
        # .symmetric_difference().add(x) ,.difference_update(set),
        # .discard(x) ,# .intersection_update(set),.issubset(set),
        # .union(set),.clear()
        setA = {1, 2, 3, 4, 5}
        setB = {1, 3, 4, 6, 7, 8}

        print(setA | setB)
        print(setA.union(setB))
        print(setB.union(setA))

        print(setA & setB)
        print(setA.intersection(setB))
        print(setB.intersection(setA))

        print(setA - setB)
        print(setA.difference(setB))
        print(setB.difference(setA))

        print(setA ^ setB)
        print(setA.symmetric_difference(setB))
        print(setB.symmetric_difference(setA))

    def setsVerb2():
        samedataSet = {"aydın", "AYDIN", "AYDIN", "AYDIN", "AYVA"}
        print(samedataSet)
        set1 = set(["Apple", "Amazon", "Microsoft", "Google"])
        set1.add("Tesla")
        print(set1)

        set2 = {1, 2, 3, 4, 5, 6, 7}
        set3 = {9, 8, 7, 6, 5}
        print("""'difference'
    set 1 : {}
    set2 : {}
    set 1 - set 2 : {}
    """.format(set2, set3, set2.difference(set3)))

        set4 = {1, 2, 3, 4, 5, 6, 7}
        set5 = {9, 8, 7, 6, 5}
        print("""'difference_update'
    set 1 : {}
    set2 : {}""".format(set4, set5))
        set4.difference_update(set5)
        print("set 1 = ", set4)

        set6 = {1, 2, 3, 4, 5, 6, 7}
        print("""'discard'
    set 1 :""", set6)
        set6.discard(1)
        print("set 1: ", set6)

        set7 = {1, 2, 3, 4, 5, 6, 7}
        set8 = {9, 8, 7, 6, 5}
        print("""'intersection'
    set 1 : {}
    set2 : {}
    set 1 & set 2 : {}
""".format(set7, set8, set7.intersection(set8)))

        set9 = {1, 2, 3, 4, 5, 6, 7}
        set10 = {9, 8, 7, 6, 5}
        print("""'intersection_update'
    set 1 : {}
    set2 : {}""".format(set9, set10))
        set9.intersection_update(set10)
        print("set 1 = ", set9)

        set11 = {1, 2, 3, 4, 5, 6, 7}
        set12 = {9, 8, 7, 6, 5, 1, 2, 3, 4, 5, 6, 7}
        print("""'issubset'
    set 1 : {}
    set2 : {}
    set 1 ⊂ set 2 : {}
    """.format(set11, set12, set11.issubset(set12)))

        set13 = {1, 2, 3, 4, 5, 6, 7}
        set14 = {9, 8, 7, 6, 57}
        print("""'union'
    set 1 : {}
    set2 : {}
    set 1 | set 2 : {}
    """.format(set13, set14, set13.union(set14)))

        set15 = {1, 2, 3, 4, 5, 6, 7}
        set16 = {9, 8, 7, 6, 57}
        print("""'clear'
        Before
    set 1 : {}
    set2 : {}
    """.format(set15, set16))
        set15.clear()
        set16.clear()
        print("""        after
    set 1 : {}
    set2 : {}
    """.format(set15, set16))

        frozen = frozenset(["Apple", "Microsoft", "Tesla", "Google"])
        print("Frozen set :", frozen)
        try:
            frozen.add("Epic")
        except Exception as e:
            print(
                "frozen sette bir işlem yapılamaz yapılırsa verilen hata türü  : ", type(e))
        try:
            frozen.discard("Epic")
        except Exception as e:
            print(
                "frozen sette bir işlem yapılamaz yapılırsa verilen hata türü  : ", type(e))

    def mapsVerb():
        sayilar = [1, 2, 3, 4, 5]
        # değişken = list(map(fonksiyon , liste)) şekilinde kullanılır.
        sayilarKareli = list(map(lambda sayi: sayi*sayi, sayilar))

        # for sayi in sayilar:
        #    sayilarKareli.append(sayi*sayi)

        sayilarFiltreli = list(filter(lambda sayi: sayi > 2, sayilar))

        print(sayilarKareli)
        print(sayilarFiltreli)

        from functools import reduce
        sayilarFaktoriyel = reduce(lambda x, y: x*y, sayilar)

        print(sayilarFaktoriyel)

    def enumerateVerb():

        # ! gibi listelerin elemanlarını numaralandırır.
        lists = ["Apple", "Facebook", "Google", "Amazon"]
        enumLists = [(0, "Python"), (1, "Java"), (2, "Kotlin"), (3, "Swift")]
        for i, j in enumLists:
            print("index : ", i, "Eleman : ", j)

        print(list(enumerate(lists)))
        # ? [(0, 'Apple'), (1, 'Amazon'), (2, 'Facebook'), (3, 'Google')][(0, 'Apple'), (1, 'Amazon'), (2, 'Facebook'), (3, 'Google')]

    def roundExp():
        # en yakın sayıya yuvarlar
        # eğer eşit uzaklıkdaysa sayı tek ise yukarı çift ise aşağı yuvarlar
        print(round(5.5))
        print(round(8.5))
        # belirtilen kısma kadar sayıyı yuvarlar
        print(round(5.651545344646, 3))

    def minAndMax():
        lists = [18, 52, 665, 4, 6, 58, 6, 4, 22, 746, 46, 9]
        print(min(lists))
        print(max(lists))
        lists2 = ["a", "b", "c", "d", "z"]
        print(min(lists2))
        print(max(lists2))
        lists3 = ["Apple", "Facebook", "Google", "Amazon", "Zen"]
        print(min(lists3))
        print(max(lists3))

    def sumVerb():
        lists = [18, 52, 665, 4, 6, 58, 6, 4, 22, 746, 46, 9]
        print("Listedeki elemanların toplamı : ", sum(lists))

    def uperLowerVerb():
        strings = "PyThOn"
        print(strings)
        print(strings.upper())
        print(strings.lower())

    def replaceVerb():
        strings = "Apple Facebook Google Amazon Zen"
        print(strings)
        print(strings.replace(" ", " -$- "))

    def starswithEndswithVerb():
        # küçük büyük harf duyarlı.
        strings = "Python"
        print(strings.startswith("P"))
        print(strings.startswith("p"))
        print(strings.endswith("n"))
        print(strings.endswith("N"))

    def splitVerb():
        strings = "Apple Facebook Google Amazon Zen"
        lists = strings.split(" ")
        print("split sonucu : ", lists, " türü : ", type(lists))

    def stripVerb():
        # boşluk siler yada verilen veriyi siler
        a = "               Python                 "
        print(a.strip())
        print(a.lstrip())
        print(a.rstrip())
        x = "xxxxxxxxxxxxxxxxxxPythonxxxxxxxxxxxxxxxxxx"
        print(x.strip("x"))
        print(x.lstrip("x"))
        print(x.rstrip("x"))

    def joinVerb():
        date = ["12", "04", "2020"]
        print(date)
        print("/".join(date))

    def countVerb():
        x = "bu yoğurdu sarımsaklasakda mı saklasak"
        print(x)
        print("İçersindeki a sayısı : ", x.count("a"))

    def findVerb():
        x = "bu yoğurdu sarımsaklasakda mı saklasak"
        print(x)
        print(x.find("sarımsak"))
        print(x.find("a"))  # ilk geçtiği yerde duru ve orayı söyler
        print(x.find("z"))  # yoksa '-1' döndürür

    def extendVerb():
        list1 = [1, 2, 3, 4]
        list2 = [10, 11, 12, 13]
        print(list1)
        print(list2)
        list1.extend(list2)  # list1'e liste 2 yi ekler.
        print(list1)
        print(list2)

    def insertVerb():
        list1 = [1, 2, 3, 4]
        print(list1)
        list1.insert(3, "Python")
        print(list1)

    def popVerb():
        list1 = [1, 2, 3, 4]
        print(list1)
        list1.pop()
        print(list1)
        list1.pop(0)
        print(list1)

    def removeVerb():
        list1 = [1, 2, 3, 4, "Python"]
        print(list1)
        list1.remove(3)
        print(list1)
        list1.remove("Python")
        print(list1)

    def indexVerb():
        list1 = [1, 2, 3, 4, "Python"]
        print(list1.index(3))
        print(list1.index("Python"))

    def sortVerb():
        list1 = [1, 9, 2, 5, 6, 3, 8, 4]
        list1.sort()
        print(list1)
        list1.sort(reverse="True")
        print(list1)
        list2 = ["Python", "Java", "Kotlin", "Swift"]
        list2.sort()
        print(list2)
        list2.sort(reverse="True")
        print(list2)

    def passExp():
        #! pass yazarak fonksiyonu boş bırakabiliriz daha sonra doldurmak üzere.
        pass


class conditionalsVerbs():
    def ifElseVerbs():
        sayi1 = 30
        sayi2 = 30

        if sayi1 == sayi2:
            print("Birşey")
            print("Birşey daha")
        print("başka birşey")

        lights = ["red", "yellow", "pink"]

        currentLight = lights[2]

        print(currentLight)

        lights = ["red", "yellow", "green"]

        currentLight = lights[2]

        print(currentLight)

        if currentLight == "red":
            print("STOP!")

        if currentLight == "yellow":
            print("READY!")

        if currentLight == "green":
            print("GO!")

    def forLoops():
        sehirler = ["Ankara", "İstanbul", "İzmir"]
        # print(sehirler[0])
        # print(sehirler[1])
        # print(sehirler[2])

        # For intro
        for sehir in sehirler:
            if sehir == "İstanbul":
                continue
            print(sehir + " için kod = " + sehir[0:3])
            print("*******")

        # For range
        for x in range(2, 100, 2):
            print(x)

    def forLoops2():
        # bu yöntem ile 3 farklı listeyi aynı anda döndürebiliriz
        number = list(range(0, 50))
        number2 = list(range(50, 100))
        number3 = list(range(100, 150))
        for n1, n2, n3 in zip(number, number2, number3):
            print("""sayı 1 : {}
sayı2 : {}
sayı3 : {}
""".format(n1, n2, n3))

    def whileLoops():
        starsCount = int(input("satır sayısı gir. "))
        x = 0
        z = 0
        stars = ""
        while x < starsCount:
            x = x+1
            while z < x:
                z = z+1
                stars = stars+"*"
            print(stars)

        sayac = 1
        sonuc = 0
        while sayac <= 10:
            sonuc = sonuc + sayac
            sayac = sayac + 1
        print(sonuc)


class sqlliteOpp():

    def selectOperasyonlari():
        import os
        import sqlite3
        connection = sqlite3.connect("chinook.db")

        # cursor = connection.execute("""select FirstName,LastName
        #                            from customers
        #                            where city='Prague' or city='Berlin'
        #                            order by FirstName,LastName desc""")

        # for row in cursor:
        #    print("First Name = "+row[0])
        #    print("Last Name = "+row[1])
        #    print("*********")

        # cursor = connection.execute("""select city,count(*) from Customers
        #                            group by city having count(*)>1
        #                            order by count(*) desc""")
        # for row in cursor:
        #    print("City = "+row[0])
        #    print("Count = "+str(row[1]))
        #    print("*********")

        cursor = connection.execute("""select FirstName,LastName
                                    from customers
                                    where FirstName like '%ja' """)

        for row in cursor:
            print("First Name = "+row[0])
            print("Last Name = "+row[1])
            print("*********")

        connection.close()

    # selectOperasyonlari()

    def insertCustomer():
        import os
        import sqlite3
        connection = sqlite3.connect("chinook.db")
        connection.execute("""insert into customers
                        (firstName,lastName,city,email)
                        values('Fahri','aydın','Ankara',
                        'fahriaydin@gmail.com')""")
        connection.commit()
        connection.close()

    # insertCustomer()

    def updateCustomer():
        import os
        import sqlite3
        connection = sqlite3.connect("chinook.db")
        connection.execute("""update customers set city='İstanbul'
                        where city='Ankara'""")

        connection.commit()
        connection.close()

    # updateCustomer()

    def deleteCustomer():
        import os
        import sqlite3
        connection = sqlite3.connect("chinook.db")
        connection.execute("""Delete from customers
                        where city='İstanbul'""")

        connection.commit()
        connection.close()

    # deleteCustomer()

    def joinOperasyonlari():
        import os
        import sqlite3
        connection = sqlite3.connect("chinook.db")
        cursor = connection.execute("""select albums.Title,
                                    artists.Name from artists
                                    inner join albums
                                    on artists.ArtistId = albums.ArtistId""")

        for row in cursor:
            print("Title = "+row[0]+" Name = "+row[1])

        connection.close()

    # joinOperasyonlari()


class jsonExp():
    def jsonExp1():
        import json
        data = '{"firstName":"Fahri","lastName":"aydın"}'

        y = json.loads(data)

        print(y["firstName"])
        print(y["lastName"])

        customer = {
            "firstName": "Fahri",
            "email": "fahriaydin@gmail.com"
        }

        customerJson = json.dumps(customer)
        print(customer)

        print(json.dumps("Fahri"))

    def jsonExp2():
        import json

        with open("users.json") as users:
            data = json.load(users)

            for x in range(6):
                print(data[x]["username"])
                print(data[x]["email"])
                print(data[x]["address"]["street"])
                print(data[x]["address"]["geo"]["lat"])


class moduleTests():
    #! https://pypi.org/
    # ? bu linkte hazır moduller eklenebilir.
    def importModules():
        # ? 3 farklı şekilde modul import edilebilir
        # ? from kullanırsak eğer moduldeki belirlenen fonksiyonlar eklenir sadece
        # import math as m  #? modul ismini yazarak istediğimiz fonksiyonunu kullanabiliriz. as kullanırsak ismini değiştirmiş oluruz.
        # from math import * #? bütün fonksiyonlarını ekler.
        # from math import factorial, ceil, floor #?belirlenen fonksiyonlarını ekler sadece
        import math as m

        print(m.factorial(5))

    def osModules():
        import os
        if os.name == "posix":
            print("Bu kod Unix/Linux veya MacOS üzerinde çalışıyor.")
        elif os.name == "nt":
            print("Bu kod Windows işletim sistemi üzerinde çalışıyor.")
        else:
            print("Bilinmeyen bir sistem!")
        print(os.getcwd())
        # print(os.makedirs("data"))
        print(os.getlogin())
        print(os.cpu_count())

    def subprocessModules():
        import subprocess as sp
        sp.call("notepad.exe")

    def webbrowserModule():
        import webbrowser as web
        web.open("www.google.com.tr")
        web.open("www.python.org")

    def sysModule():
        import sys
        print(sys.version)
        print(sys.platform)
        print(sys.copyright)

    def randomModule():
        import random as rd
        print(rd.random())  # 0.0-1.0 arası değer atar
        print(rd.randrange(5, 10))  # verilen değer arasında sayı tahmini yapar
        # başlangıç değerini almaz son değer dahil değildir
        print(rd.randrange(10))
        # verilen değer arasında değer atar.son değer dahildir.
        print(rd.randint(5, 15))
        choiceList = ["Apple", "Facebook", "Google", "Amazon"]
        print(rd.choice(choiceList))  # listeden rastgele bir eleman seçer

    def timeModule():
        import time
        print(time.asctime())  # sistem tarihi
        time.sleep(10)  # programı belirlenen sürede bekletir saniye cinsi

    def myModules():
        import tools.module.matematikModule
        help(tools.module.matematikModule)
        tools.module.matematikModule.topla(2, 3)
        tools.module.matematikModule.carp(2, 3)
        import tools.module.matematikModule as mm
        mm.carp(3, 4)
        print(mm.customer["firstName"])
        from tools.module.matematikModule import topla
        topla(2, 4)
        from tools.module.matematikModule import customer
        print(customer["firstName"])

    def importNetworkModules():
        #! https://pypi.org/
        # ? bu linkte hazır moduller eklenebilir.
        # ? klasör url'sine cmd yazıp entere tıklıyoruz
        # ? python setup.py install
        import math2d
        help(math2d)

    def dateTimes():
        def help():
            print("""
['MAXYEAR',
 'MINYEAR',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'date',
 'datetime',
 'datetime_CAPI',
 'sys',
 'time',
 'timedelta',
 'timezone',
 'tzinfo']""")
        help()
        from datetime import datetime
        import locale
        now = datetime.now()
        print(now)
        print(datetime.strftime(now, "%Y"))
        print(datetime.strftime(now, "%A"))
        print(datetime.strftime(now, "%B"))
        print(datetime.strftime(now, "%A"))
        print(datetime.timestamp(now))
        print(locale.setlocale(locale.LC_ALL, ""))
        print(datetime.strftime(now, "%Y %B %A"))
        now_sec = datetime.timestamp(now)
        print(now_sec)
        date = datetime.fromtimestamp(now_sec)
        print(date)
        print(datetime.fromtimestamp(1600849791.11357))
        print(datetime.fromtimestamp(0))

    def request():
        import requests
        from bs4 import BeautifulSoup as bsp
        url = "https://www.imdb.com/chart/top/"
        response = requests.get(url)
        # print(response)
        content = response.content
        print(content)
        html_data = bsp(content, "html.parser")
        pretty_html_data = html_data.prettify
        # print(pretty_html_data)
        # for i in html_data.find_all("a"):
        #   print(i.text)
        #   print("*****************")
        product_list = list()
        for i in html_data.find_all("td", {"class": "titleColumn"}):
            temp = i.text
            temp = temp.replace("\n", "")
            temp = temp.strip()
            product_list.append(temp)
        print(product_list)
        ratings = list()
        for i in html_data.find_all("td", {"class": "titleColumn"}):
            temp = i.text
            temp = temp.replace("\n", "")
            temp = temp.strip()
            ratings.append(temp)
        for i, j in zip(product_list, ratings):
            print("Film:", i, "Rating:", j)

            # Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
            # Film: 1.      The Shawshank Redemption(1994) Rating: 9.2
            # Film: 2.      The Godfather(1972) Rating: 9.1
            # Film: 3.      The Godfather: Part II(1974) Rating: 9.0
            # Film: 4.      The Dark Knight(2008) Rating: 9.0
            # Film: 5.      12 Angry Men(1957) Rating: 8.9
            # Film: 6.      Schindler's List(1993) Rating: 8.9
            # Film: 7.      The Lord of the Rings: The Return of the King(2003) Rating: 8.9
            # Film: 8.      Pulp Fiction(1994) Rating: 8.8
            # Film: 9.      Il buono, il brutto, il cattivo(1966) Rating: 8.8
            # Film: 10.      The Lord of the Rings: The Fellowship of the Ring(2001) Rating: 8.8
            # Film: 11.      Fight Club(1999) Rating: 8.8
            # Film: 12.      Forrest Gump(1994) Rating: 8.8
            # Film: 13.      Inception(2010) Rating: 8.7
            # Film: 14.      Star Wars: Episode V - The Empire Strikes Back(1980) Rating: 8.7
            # Film: 15.      The Lord of the Rings: The Two Towers(2002) Rating: 8.7
            # Film: 16.      The Matrix(1999) Rating: 8.6
            # Film: 17.      Goodfellas(1990) Rating: 8.6
            # Film: 18.      One Flew Over the Cuckoo's Nest(1975) Rating: 8.6
            # Film: 19.      Shichinin no samurai(1954) Rating: 8.6
            # Film: 20.      Se7en(1995) Rating: 8.6
            # Film: 21.      La vita è bella(1997) Rating: 8.6
            # Film: 22.      Cidade de Deus(2002) Rating: 8.6
            # Film: 23.      The Silence of the Lambs(1991) Rating: 8.6
            # Film: 24.      It's a Wonderful Life(1946) Rating: 8.6
            # Film: 25.      Star Wars(1977) Rating: 8.6
            # ...
            # Film: 247.      Mandariinid(2013) Rating: 8.0
            # Film: 248.      Aladdin(1992) Rating: 8.0
            # Film: 249.      Trois couleurs: Rouge(1994) Rating: 8.0
            # Film: 250.      A Wednesday(2008) Rating: 8.0


class classVerbs():
    def startClassVerb():
        class Matematik:
            def __init__(self, sayi1, sayi2):
                self.sayi1 = sayi1
                self.sayi2 = sayi2

            def topla(self):
                return self.sayi1 + self.sayi2

            def cikar(self):
                return self.sayi1 - self.sayi2

            def carp(self):
                return self.sayi1 * self.sayi2

            def bol(self):
                return self.sayi1 / self.sayi2

        matematik = Matematik(2, 78)
        matematik2 = Matematik(3, 76)
        print("Toplam = " + str(matematik2.topla()))

        # Property

        class Person:
            def __init__(self, firstName, lastName, age):
                self.firstName = firstName
                self.lastName = lastName
                self.age = age

        person1 = Person("Fahri", "aydın", 33)
        print(person1.firstName)

        class Worker(Person):
            def __init__(self, salary):
                self.salary = salary

        class Customer(Person):
            def __init__(self, creditCardNumber):
                self.creditCardNumber = creditCardNumber

        ahmet = Worker(person1)

        mehmet = Customer(person1)


class exceptionsVerbs():
    def exceptionsInfo():
        print("""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
""")

    def verbs1():
        try:
            sayi = int(input("Sayı giriniz"))
        except ValueError:
            print("Tip uyuşmazlığı : Lütfen sayı giriniz")
        except ZeroDivisionError:
            print("Payda sıfır olamaz")
        except:
            print("Bir hata oluştu")

        print("Bitti")

    def verbs2():
        try:
            sayi = int("a")
        except Exception as e:
            print("Bir hata oluştu. Hata tipi : ", type(e))

    def verb3():
        import sys
        liste = [7, 'Fahri', 0, 3, "6"]
        for x in liste:
            try:
                print("Sayı: " + str(x))
                sonuc = 1/int(x)
                print("Sonuç : " + str(sonuc))
            except ValueError:
                print(str(x) + " bir sayı değil")
            except ZeroDivisionError:
                print(str(x) + " için sıfıra bölme hatası")
            except:
                print(str(x) + " hesaplanamadı")
                print("Sistem diyor ki : " + str(sys.exc_info()[0]))
            finally:
                print("İşlemler bitti")
        try:
            file = open("myCodes/tools/abc.txt")
        except:
            file = open("myCodes/tools/abc.txt", "w")
            print("dosya hatası")
        finally:
            file.close()
            print("dosya kapandı")


class fileVerbs():
    # ? r(read),r+(read and append),a(append),w(write), rb(binary dosyaları açar)
    # ? open, close, read, write, readlines, writelines, readable, writable, seek, tell, readable, writable
    def verb1():
        import os
        f = open("myCodes/tools/clients.txt")
        # print(f.read())
        print("**********")
        # print(f.readline())
        # print(f.readline())
        for l in f:
            print(l)
        f.close()
        # r Read, a append, w write, x create
        fileToAppend = open("myCodes/tools/students.txt", "w")
        fileToAppend.write("\n")
        fileToAppend.write("Ahmet")
        fileToAppend.close()
        #! dosya silme
        if os.path.exists("myCodes/tools/students.txt"):
            os.remove("myCodes/tools/students.txt")
        else:
            print("Dosya yok")
            os.rmdir("empty")

    def verb2():
        students = ["Fahri", "Selin", "Salih", "Ali", "Ayşe"]
        fileToAppend = open("myCodes/tools/students.txt", "a")
        for ogrenci in students:
            fileToAppend.write(ogrenci)
            fileToAppend.write("\n")

        fileToAppend.close()

    def verb3():
        try:
            file = open("abc.txt", "a", encoding="utf-8")
        except:
            file = open("abc.txt", "w", encoding="utf-8")
        file.write("ışç\n")
        file.close()

    def verb4():
        try:
            file = open("abc.txt", "a", encoding="utf-8")
        except:
            file = open("abc.txt", "w", encoding="utf-8")
        file.write("Demet\nSelin\nSelma\nFahri\nAybüke\n")
        file.close()
        fileRead = open("abc.txt", "r", encoding="utf-8")
        fileList = fileRead.readlines()  # ! bütün satırları okur ve listeye dönüştürür
        print(fileList)
        print(type(fileList))
        fileRead.close()

    def verb5():
        file = open("file.txt", "w", encoding="utf-8")
        file.write("Koç\nApple\nMicrosoft\nTesla\nGoogle\nEpic\nCestnyTR")
        print(file.readable())
        print(file.writable())
        file.close()
        with open("file.txt", "r+", encoding="utf-8") as file:
            print(file.read())
            print(file.tell())
            file.seek(10)
            print(file.read(10))
            print(file.readable())
            print(file.writable())

        # Dosyaların Sonuna Ekleme Yapmak
        file = open("file.txt", "a", encoding="utf-8")
        file.tell()
        file.write("\nNeurolink")
        file.close()
        # Dosyaların başına Ekleme Yapmak
        file = open("file.txt", "r+", encoding="utf-8")
        fread = file.read()
        print(file.seek(0))
        print(file.tell())
        file.write("SpaceX\n"+fread)
        print(file.read())
        file.close()
        # dosyanın ortasına veri yazdırma
        with open("file.txt", "r+", encoding="utf-8") as file:
            list = file.readlines()
            middle = round(len(list)/2)
            list.insert(middle, "Samsung\n")
            file.seek(0)
            for i in list:
                file.write(i)


class funcsVerb:
    def funcsInfo():
        print("""# Fonksiyonlar "First Class Citizen" yani "Birinci Sınıf Vatandaş"tırlar
    +Bir değişkene atanabilir.
    +Çalışma anında oluşturulabilir.
    +Fonksiyonlardan döndürülebilir.
    +Parametre olarak geçirilebilir.
    +def funcName(*args):
    +def funcName(**kwargs):
""")

    def args():
        # fonksiyona istediğimiz kadar everi gönderebiliriz
        def argsExp(*args):
            return args
        arg = argsExp(1, 2, 3, 4, 5, 6)
        print("Türü : ", type(arg), "\nVeri : ", arg)

    def kwargs():
        # fonksiyona istediğimiz kadar everi gönderebiliriz
        def kwargsExp(**kwargs):
            return kwargs
        kwargs = kwargsExp(name="Fahri", num=12345)
        print("Türü : ", type(kwargs), "\nVeri : ", kwargs)

    def funcToVariable():
        def helloWorld():
            print("Hello world")
        helloWorld()
        x = helloWorld
        print("helloWorld type : ", type(helloWorld))
        print("x type : ", type(x))
        del helloWorld
        try:
            print("helloWorld type : ", type(helloWorld))
            helloWorld()
        except Exception as e:
            print("Hata : ", type(e))
        x()
        print("x type : ", type(x))

    def parametreToFunc():
        def square(a):
            return a ** 2

        def cube(a):
            return a ** 3

        def square_cube(func1, func2):
            op = input("İşlemi Giriniz:")
            num = int(input("Bir Sayı Girin:"))

            if (op == "kare"):
                return func1(num)
            elif (op == "kup"):
                return func2(num)
            else:
                print("Geçersiz İşlem!")
        print(square_cube(square, cube))

    def decoraterExp():
        def decorater(func):
            def wrapper(x):
                import time
                startTime = time.time()
                result = func(x)
                endTime = time.time()
                resultTime = endTime-startTime
                print("fonsiyon süresi  : ", resultTime)
                return result
            return wrapper

        @decorater
        def calcTimeList(num):
            lists = list()
            for i in range(num):
                lists.append(i)
            return lists

        @decorater
        def calcTimeSet(num):
            sets = set()
            for i in range(num):
                sets.add(i)
            return sets
        print(calcTimeList(10000000))
        calcTimeSet(10000000)

    def iterators():
        sehirler = ["Ankara", "İstanbul", "İzmir", "Van"]
        iteratorum = iter(sehirler)
        print(next(iteratorum))
        print(next(iteratorum))
        print(next(iteratorum))
        print(next(iteratorum))
        for sehir in sehirler:
            print(sehir)

    def myIterators():
        class tsk():
            def __init__(self, rank):
                self.rank = rank
                self.index = -1

            def __iter__(self):
                return self

            def __next__(self):
                self.index += 1
                if (self.index < len(self.rank)):
                    return self.rank[self.index]
                else:
                    self.index = -1
                    raise StopIteration

        solider = tsk(["sözleşmeli er", "uzman onbaşı", "uzman çavuş", "astsubay çavuş",
                       "astsubay kıdemli çavuş", "astsubay üstçavuş", "astsubay kıdemli üstçavuş",
                       "astsubay başçavuş", "astsubay kıdemli başçavuş", "teğmen", "üstteğmen", "yüzbaşı",
                       "binbaşı", "yarbay", "albay", "tuğgeneral", "orgeneral"])
        for i in solider:
            print(i)

    def generators():
        from sys import getsizeof

        def function():
            myLists = list()
            for i in range(300):
                myLists.append(i)
            return myLists

        def generator():
            for i in range(300):
                yield i
        print(type(function))
        print(type(generator))
        func = function()
        gen = generator()
        print(type(func))
        print(type(gen))
        print(getsizeof(func))
        print(getsizeof(gen))
        print("fonksiyon değerler : ", func)
        print("Generator değeri : ", gen)
        genList = list()
        for i in gen:
            genList.append(i)
        print("Generator değeri list : ", genList)
        print("Fonksiyon belleği : ", getsizeof(func), "Tipi : ", type(func))
        print("Generator belleği : ", getsizeof(gen), "Tipi : ", type(gen))
        print("Generator listesi belleği : ", getsizeof(
            genList), "Tipi : ", type(genList))
        print("tek satırda oluşturula generator ; list[] ,generator()")
        funcList = [x for x in range(300)]
        generatorList = (x for x in range(300))
        print(type(funcList))
        print(type(generatorList))
        print(getsizeof(funcList))
        print(getsizeof(generatorList))
        print("fonksiyon değerler : ", func)
        print("Generator değeri : ", gen)
#! demos


class Foulium:
    def trProvices():
        import folium
        import pandas
        cityData = pandas.read_excel(
            "myCodes/basicOfPython/tools/tr-cities.xlsx")
        worldMap = folium.Map(tiles="CartoDB Voyager")
        cityList = list(cityData["City"])
        xList = list(cityData["Enlem"])
        yList = list(cityData["Boylam"])
        for x, y, name in zip(xList, yList, cityList):
            worldMap.add_child(folium.Marker(
                location=(x, y), icon=folium.Icon(color="green"), popup=name))
        worldMap.save("myCodes/basicOfPython/tools//Türkiye_ileçeler.html")

    def corona_virus():
        import folium
        import pandas

        def calculate_radius(case, values, calc):
            if case < values[0]:
                return calc[0]
            elif case < values[1]:
                return calc[1]
            elif case < values[2]:
                return calc[2]
            else:
                return calc[3]

        def calculate_color(case, values, color):
            if case < values[0]:
                return color[0]
            elif case < values[1]:
                return color[1]
            elif case < values[2]:
                return color[2]
            else:
                return color[3]

        cv_data = pandas.read_excel(
            "myCodes/basicOfPython/tools/world_coronavirus_cases.xlsx")

        worldMap = folium.Map(tiles="CartoDB Voyager")
        sum_case_map = folium.FeatureGroup("Toplam vaka sayılar")
        death_rate_map = folium.FeatureGroup("Ölüm oranı")
        active_case_map = folium.FeatureGroup("Aktif vaka dağılımı")
        test_rate_map = folium.FeatureGroup("Test oranı haritası")
        demographic_map = folium.FeatureGroup("Nufus dağılım haritısı")

        x_list = list(cv_data["Enlem"])
        y_list = list(cv_data["Boylam"])
        sum_cases = list(cv_data["Toplam Vaka"])
        death_rates = list(cv_data["Vefat Edenler"])
        active_cases = list(cv_data["Aktif Vakalar"])
        test_counts = list(cv_data["Toplam Test"])
        populations = list(cv_data["Nüfus"])
        colors = ("green", "white", "orange", "red")
        opacity = 0.4
        values = (100000, 300000, 750000)
        radius = (50000, 100000, 200000, 400000)
        raito = (2.5, 5, 7.5)
        raito_radius = (25000, 50000, 100000, 20000)
        for x, y, sum in zip(x_list, y_list, sum_cases):
            sum_case_map.add_child(folium.Circle(
                location=(x, y),
                radius=calculate_radius(
                    sum, values, radius),
                color=calculate_color(sum, values, colors),
                fill=calculate_color(sum, values, colors), fill_opacity=opacity))
        for x, y, sum, death_rate in zip(x_list, y_list, sum_cases, death_rates):
            death_rate_map.add_child(folium.Circle(
                location=(x, y),
                radius=calculate_radius(
                    ((death_rate/sum)*100), raito, raito_radius),
                color=calculate_color(
                    ((death_rate/sum)*100), raito, colors),
                fill=calculate_color(((death_rate/sum)*100), raito, colors), fill_opacity=opacity)
            )
        for x, y, active_case in zip(x_list, y_list, active_cases):
            active_case_map.add_child(folium.Circle(
                location=(x, y),
                radius=calculate_radius(
                    active_case, values, radius),
                color=calculate_color(
                    active_case, values, colors),
                fill=calculate_color(active_case, values, colors), fill_opacity=opacity))
        for x, y, population, test_count in zip(x_list, y_list, populations, test_counts):
            test_rate_map.add_child(folium.Circle(
                location=(x, y),
                radius=calculate_radius(
                    ((test_count/population)*100), raito, raito_radius),
                color=calculate_color(
                    ((test_count/population)*100), raito, colors),
                fill=calculate_color(((test_count/population)*100), raito, colors), fill_opacity=opacity)
            )
        demographic_map.add_child(folium.GeoJson(
            data=(open("myCodes/basicOfPython/tools/world.json",
                       "r", encoding="utf-8-sig").read()),
            style_function=lambda x: {'fillColor':
                                      calculate_color(x["properties"]["POP2005"],
                                                      (20000000, 50000000, 100000000), colors)
                                      }))
        worldMap.add_child(sum_case_map)
        worldMap.add_child(death_rate_map)
        worldMap.add_child(demographic_map)
        worldMap.add_child(active_case_map)
        worldMap.add_child(test_rate_map)

        worldMap.add_child(folium.TileLayer("OpenStreetMap"))
        worldMap.add_child(folium.TileLayer("Cartodb dark_matter"))

        worldMap.add_child(folium.LayerControl())
        worldMap.save("myCodes/basicOfPython/tools/world_coronavirus.html")


class PyQt5:
    def exp():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.main_exp as main
        app = QtWidgets.QApplication(sys.argv)
        window = main.Window()
        sys.exit(app.exec_())

    # ? yazı , resim  ve buton ekleme

    def exp1():
        import sys
        from PyQt5 import QtWidgets, QtGui
        app = QtWidgets.QApplication(sys.argv)

        window = QtWidgets.QWidget()
        window.setWindowTitle("PyQt5 Demo")
        window.setGeometry(450, 100, 500, 500)

        text = QtWidgets.QLabel(window)
        text.setText("Hello world")
        text.move(50, 50)

        pic = QtWidgets.QLabel(window)
        pic.setPixmap(QtGui.QPixmap(
            "myCodes/basicOfPython/tools/python.png"))
        pic.move(125, 100)

        buton = QtWidgets.QPushButton(window)
        buton.setText("Button")
        buton.move(220, 400)

        window.show()
        sys.exit(app.exec_())

    # ? layout ,.addStretch()
    def exp2():
        import sys
        from PyQt5 import QtWidgets
        app = QtWidgets.QApplication(sys.argv)

        buton1 = QtWidgets.QPushButton()
        buton1.setText("Button1 verticalLayout")

        buton2 = QtWidgets.QPushButton()
        buton2.setText("Button2 verticalLayout")
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addStretch()
        verticalLayout.addWidget(buton1)
        verticalLayout.addWidget(buton2)

        buton3 = QtWidgets.QPushButton()
        buton3.setText("Button3 horizantelLayout")

        buton4 = QtWidgets.QPushButton()
        buton4.setText("Button4 horizantelLayout")

        horizantelLayout = QtWidgets.QHBoxLayout()
        horizantelLayout.addStretch()
        horizantelLayout.addLayout(verticalLayout)
        # horizantelLayout.addWidget(buton3)
        # horizantelLayout.addWidget(buton4)

        window = QtWidgets.QWidget()
        window.setWindowTitle("PyQt5 Demo")
        window.setGeometry(450, 100, 500, 500)
        # window.setLayout(verticalLayout)
        window.setLayout(horizantelLayout)

        window.show()
        sys.exit(app.exec_())

    # ? butonlara fonksiyon ekeleme
    def exp3():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.btn_func as btn
        app = QtWidgets.QApplication(sys.argv)
        window = btn.Window()
        sys.exit(app.exec_())

    # ? kullanıcıdan  input alma ve inputları kontrol etme
    def exp4():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.user_input as ui
        app = QtWidgets.QApplication(sys.argv)
        window = ui.Window()
        sys.exit(app.exec_())

    # ? checkbox örneği
    def exp5():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.checkbox as ch
        app = QtWidgets.QApplication(sys.argv)
        window = ch.Window()
        sys.exit(app.exec_())

    # ? Radio buton örneği
    def exp6():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.radiobutton as rd
        app = QtWidgets.QApplication(sys.argv)
        window = rd.Window()
        sys.exit(app.exec_())

    # ? menu bar oluşturma
    def exp7():
        import sys
        from PyQt5 import QtWidgets
        import tools.module.menu as menu
        app = QtWidgets.QApplication(sys.argv)
        window = menu.Window()
        sys.exit(app.exec_())


class demos():
    #!dilekçe yazdırma (FORMAT)

    def stringsFormat():
        dilekce = ("""
        python dekanlığına konya {}/{}/{}
        Konu: {}
        Gereğnin yapılmasını arz ederim.Saygılarımla,
        Ad-Soyad : {}
        Adres bilgileri : {}
        Telefon : {}

        """)
        gun = input("GÜn : ")
        ay = input("ay : ")
        yil = input("yıl : ")
        konu = input("konu : ")
        isim = input("isim : ")
        adres = input("adres : ")
        telefon = input("telefon : ")
        print(dilekce.format(gun, ay, yil, konu, isim, adres, telefon))

#!çift/tek,/kare küp  ve kökünü yazdırma
    def calcSquare():
        sayi = int(input("sayi giriniz : "))
        if (sayi % 2 == 0):
            {print(sayi, " sayı çifttir")}
        else:
            {print(sayi, "tektir")}
        kare = sayi**2
        kup = sayi**3
        kok = sayi**(1/2)
        print("{} sayısının\nkaresi : {} \nküpü : {} \nkökü {}".format(
            sayi, kare, kup, kok))

#!girlen textin kaç karekter olduğunu yazdırma / karekter atlıyarak yazdırma / her karekterden sonra nokta ekleme
    def calcCharecter():
        text = input("yazı giriniz : ")
        print("yazı uzunluğu ", len(text),
              "\nkarekter atlıyarak yazıdrma : ", *text[0:10:2], sep=".")

#! şekil alan ve çevre hesplama
    def calcShape():
        pi = 3.14
        def triangleAreaCalc(a, h): return a*h*1/2
        def trianglePerimeterCalc(a, b, c): return a+b+c

        def circleAreaCalc(r): return r*r*pi
        def circlePerimeterCalc(r): return 2*r*pi

        def squareAreaCalc(a): return a*a
        def squarePerimeterCalc(a): return 4*a

        def rectanglePerimeterCalc(a, b): return a*b
        def rectangleAreaCalc(a, b): return 2*(a+b)

        while True:
            print("""Şekil Cevre-Alan Hesaplama Programına Hoşgeldiniz
                        Hesaplama Yapılabilen Şekiller
                        Kare
                        Dikdörtgen
                        Üçgen
                        Daire
                        Programdan çıkmak için 'q' tuşlaması yapın!""")
            shape = input("şekli giriniz").lower()
            calcWhat = input("""Çevre hesaplamak için C
            Alan hesaplamak için A yazınız.""").lower()
            if shape == "kare" and calcWhat == "c":
                squareSide = int(
                    input("Kare şeklinin kenar uzunluğunu giriniz."))
                print("kare çevresi : ", squarePerimeterCalc(squareSide))
            elif shape == "kare" and calcWhat == "a":
                squareSide = int(
                    input("Kare şeklinin kenar uzunluğunu giriniz."))
                print("kare Alan : ", squareAreaCalc(squareSide))

            elif shape == "dikdörtgen" and calcWhat == "c":
                rectangleL = int(
                    input("Dikdörtgen şeklinin uzun kenar uzunluğunu giriniz."))
                rectangleS = int(
                    input("Dikdörtgen şeklinin kısa kenar uzunluğunu giriniz."))
                print("Dikdörtgen çevresi : ",
                      rectanglePerimeterCalc(rectangleL, rectangleS))
            elif shape == "dikdörtgen" and calcWhat == "a":
                rectangleL = int(
                    input("Dikdörtgen şeklinin uzun kenar uzunluğunu giriniz."))
                rectangleS = int(
                    input("Dikdörtgen şeklinin kısa kenar uzunluğunu giriniz."))
                print("Dikdörtgen Alan : ", rectangleAreaCalc(
                    rectangleL, rectangleS))

            elif shape == "üçgen" and calcWhat == "c":
                triangleA = int(
                    input("Üçgen şeklinin 1. kenar uzunluğunu giriniz."))
                triangleB = int(
                    input("Üçgen şeklinin 2. kenar uzunluğunu giriniz."))
                triangleC = int(
                    input("Üçgen şeklinin taban kenar uzunluğunu giriniz."))
                print("Üçgen çevresi : ", trianglePerimeterCalc(
                    triangleA, triangleB, triangleC))
            elif shape == "üçgen" and calcWhat == "a":
                triangleC = int(
                    input("Üçgen şeklinin taban kenar uzunluğunu giriniz."))
                triangleH = int(
                    input("Üçgen şeklinin yükseklik uzunluğunu giriniz."))
                print("Üçgen Alan : ",  triangleAreaCalc(triangleC, triangleH))

            elif shape == "daire" and calcWhat == "c":
                circleR = int(
                    input("Daire şeklinin yarıçap uzunluğunu giriniz."))
                print("Daire çevresi : ", circlePerimeterCalc(triangleH))
            elif shape == "daire" and calcWhat == "a":
                circleR = int(
                    input("Daire şeklinin yarıçap uzunluğunu giriniz."))
                print("Daire Alan : ",  circleAreaCalc(triangleH))
            elif shape == "q":
                print("Program kapatılıyor...")
                break
            else:
                print("hatalı şekil girdiniz.")
#! en büyük sayıyı bulma

    def bigestNum():
        number1 = int(input("1.sayıyı giriniz. "))
        number2 = int(input("2.sayıyı giriniz. "))
        number3 = int(input("3.sayıyı giriniz. "))
        theNumber = 0
        if (number1 > number2):
            theNumber = number1
        else:
            theNumber = number2
        if (theNumber < number3):
            theNumber = number3
        print("en büyük sayı ", theNumber)
#! fakötriyel hesaplama

    def calcFactorial():
        num = int(input("sayı giriniz. "))

        if num < 0:
            return "negatif sayıların faktöriyeli olamaz"
        total = 1
        for x in range(1, num+1):
            total = total*x
        print("faktöriyeli = ", total)
#! matris hesaplama

    def matrisSum():
        matris1 = [[1, 3, 5], [2, 4, 1], [1, 5, 7]]
        matris2 = [[3, 3, 4], [2, 4, 1], [3, 5, 4]]
        sumMatris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(len(matris1)):
            for y in range(len(matris1)):
                sumMatris[x][y] = (matris1[x][y]+matris2[x][y])
        print("matris toplamı = ", sumMatris)
#! alfabeye göre yada küçükden büyüğe sıralama

    def ABCD():
        senteces = "bugün hava çok güzel ama"
        words = senteces.split()
        words.sort()
        for x in words:
            print(x)
#! hesap makinesi

    def calcMath():
        print("1 : topla")
        print("2 : çıkart")
        print("3 : çarp")
        print("4 : böl")
        mathOp = int(input("işlem giriniz. "))
        num1 = int(input("birinci sayıyı giriniz. "))
        num2 = int(input("ikinci sayıyı giriniz. "))

        if mathOp == 1:
            print(num1+num2)
        elif mathOp == 2:
            print(num1-num2)
        elif mathOp == 3:
            print(num1*num2)
        elif mathOp == 4:
            print(num1/num2)
        else:
            print("1-4 arasında bir sayı giriniz.")

    def calcMath2():
        while (True):
            print("""Lütfen aşağıdaki işlemlerden birisini seçerek entre'a basın.
            Toplama = +
            Çıkarma = -
            Çarpma = *
            Bölme = /
            Çıkmak için 'q'""")
            opp = input("Lütfen seçtiğiniz işlemi girin: ")
            a = int(input("Lütfen ilk sayıyı girin: "))
            b = int(input("Lütfen ikinci sayıyı girin: "))
            if (opp == "q"):
                print("Programdan çıkılıyor...")
                break
            elif (opp == "+"):

                print(a+b)
            elif (opp == "-"):

                print(a - b)
            elif (opp == "*"):

                print(a * b)
            elif (opp == "/"):

                print(a / b)
            else:
                print("Geçersiz İşlem")
#! asal sayı

    def checkPrimeNum():
        pNumber = int(input("sayı giriniz. "))
        isPrimeNum = True
        for x in range(2, pNumber):
            print(pNumber, x)

            print(pNumber % x)
            if (pNumber % x == 0):
                isPrimeNum = False
                break
        if isPrimeNum:
            print("asal sayı")
        else:
            print("asal sayı değildir")
#! en büyük sayıyı bulma

    def checkBigestNum():
        number1 = int(input("1.sayıyı giriniz. "))
        number2 = int(input("2.sayıyı giriniz. "))
        number3 = int(input("3.sayıyı giriniz. "))
        theNumber = 0
        if (number1 > number2):
            theNumber = number1
        else:
            theNumber = number2
        if (theNumber < number3):
            theNumber = number3
        print("en büyük sayı ", theNumber)
#! parola

    def defindPassword():
        while (True):
            print("parola 8 karekterden az 3 karekterden fazla olmalıdır.")
            password = input("parola  belirleyiniz.")
            if (len(password) > 3 and len(password) < 8):
                print("parola başarılı bir şekilde oluşturulmuştur.")
                break

#! list arasındaki fark

    def compareList():
        firs_list = [1, 2, 4, 8, 101, 203, 568, 784, 45, 63, 52, 89, 45,
                     36, 21, 410, 23, 56, 78, 45, 14, 459, 125, 456, 98, 96, 621]
        sec_list = [1, 2, 8, 101, 568, 45, 63, 21, 52,
                    21, 410, 78, 459, 96, 103, 460, 452, 602]
        diff = 0
        for i in firs_list:
            if not i in sec_list:
                diff += 1
                print(
                    "ilk listenin ikinci listeden farkı {} ve adeti {}".format(i, diff))

#! cümlede isteniler harftan kaç tane var

    def countLetter():
        sentence = """Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır
            metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat
            numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı
            1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır.
            Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden
            elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren
            Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi
            Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur."""
        theWord = input("sayısını bilmek istediğiniz harfi giriniz")
        print(len(theWord))
        while True:
            if len(theWord) < 2 or len(theWord) > 0:
                print("bir harf giriniz.")
                theWord = input("sayısını bilmek istediğiniz harfi giriniz")
            else:
                for i in sentence:
                    if theWord == i:
                        count += 1
            break

        print("{} harfinin cümledeki sayısı : {}".format(theWord, count))

#!kelimeleri tersten yazma
    def reverseIt():
        reverse = input("tersten yazılmasını istediğiniz kelimeyi giriniz : ")
        print(*reverse[::-1])
#! iki fakrlı değişken arasında birbirleri ile değişken değerlerini değiştirme

    def exchanceNum():
        x = 10
        y = 20
        x, y = y, x
        # temp = x
        # x = y
        # y = temp
        print("x = " + str(x))
        print("y = " + str(y))
#! mil hesaplama

    def calcKmToMil():
        kmToMil = 0.621371192
        km = int(input("Kaç km?"))

        mil = km * kmToMil
        print(str(km) + " Km = "+str(mil)+" mil eder")
#! manav fonksiyon

    def calcFruit():
        print("Manava Hoşgeldiniz")

        def muhasebe():
            kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
            tutar = kilo * 5
            print("Ödemeniz Gereken Tutar:", tutar)
        meyve = input("Lütfen İstediğiniz Meyveyi Girin(Kilosu 5 TL):")
        if (meyve == "elma"):
            muhasebe()
        elif (meyve == "armut"):
            muhasebe()
        elif (meyve == "portakal"):
            muhasebe()
        else:
            print("Malesef Elimizde Bu Meyve Yok!")

#! sayı tahmin uygulaması
    def guesNumber():
        import time as t
        import random as rd

        print("""sayı tahmin uygulamasına hoş geldiniz.
yanlızca 5 tahmin hakkınız vardır.
çıkmak için 'q' tuşuna tıklayınız.""")

        def countDown():
            for i in range(3, 0, -1):
                t.sleep(1)
                print(i)

        def exit():
            for i in range(3, 0, -1):
                print("Program Sonlandırılıyor.")
                t.sleep(0.5)
                print(".")
                t.sleep(0.5)
                print("..")
                t.sleep(0.5)
                print("...")
                break

        def startGues():
            print("Oyun Başlatılıyor.")
            t.sleep(0.5)
            print(".")
            t.sleep(0.5)
            print("..")
            t.sleep(0.5)
            print("...")
            t.sleep(0.5)
            game_start()

        def wantContinue():
            continueToGues = input("""Devam etmek için : 'Y'
Bitirmek için : 'Q'
Tuşlarına basınız.""")
            if continueToGues.lower() == "y":
                startGues()
            else:
                exit()

        def game_start(life=5):
            theNum = rd.randint(0, 10)
            while True:
                userGues = input(
                    """Tahmin ettiğiniz sayıyı giriniz.
(çıkmak için 'q' tuşuna basınız.)""")
                if (userGues.lower() == "q"):
                    exit()
                elif (int(userGues) == theNum):
                    print(
                        "Harika {}. hakkınız varken doğru sayıyı buldunuz".format(life))
                    wantContinue()
                elif (int(userGues) != theNum):
                    print(
                        "Üzgünüm doğru sayıyı tahmin edemediniz. kalan hakkınız", life)
                elif (life == 0):
                    print("Doğru sayıyı bulamadınız doğru sayı : ", theNum)
                    wantContinue()
                else:
                    print("hatalı karekter girdiniz.")
                life -= 1
                countDown()

        game_start()
#! OOP örnek oyun saldır - savun

    def atackDef():
        import time
        import sys
        import random

        def errorPoint():
            print("!Eksik ya da Hatalı Tuşlama!")

        def addPoint():
            print(".")
            time.sleep(.3)
            print("..")
            time.sleep(.3)
            print("...")
            time.sleep(.3)

        class Player():
            def __init__(self, pName, life=10, power=100, puan=0):
                self.pName = pName
                self.life = life
                self.power = power
                self.puan = puan

            def showInfo(self):
                print("""Oyuncu bilgileri;
isim : {}
Can : {}
Güç : {}
Puan : {}""".format(self.pName, self.life, self.power, self.puan))

            def atack(self, enemy):
                position = self.atack_defance_count()
                if position == 1:
                    print("Saldırı Başladı...")
                    addPoint()
                    print("Saldırı Başarılı")
                    self.power -= 10
                    self.puan += 10
                    enemy.life -= 1
                    self.showInfo()
                    enemy.showInfo()
                else:
                    print("Saldırı Başladı...")
                    addPoint()
                    print("Saldırı Başarısız")
                    self.life -= 1
                    self.power -= 10
                    enemy.puan = 10
                    self.showInfo()
                    enemy.showInfo()
                self.checkWinner(enemy)

            def defence(self, enemy):
                position = self.atack_defance_count()
                if position == 1:
                    print("Saldırı Başladı...")
                    addPoint()
                    print("Saldırı Başarılı")
                    self.power -= 10
                    self.puan += 10
                    enemy.life -= 1
                    self.showInfo()
                    enemy.showInfo()
                else:
                    print("Saldırı Başladı...")
                    addPoint()
                    print("Saldırı Başarısız")
                    self.life -= 1
                    self.power -= 10
                    enemy.puan = 10
                    self.showInfo()
                    enemy.showInfo()
                self.checkWinner(enemy)

            def atack_defance_count(self):
                return random.randint(1, 2)

            def checkWinner(self, enemy):
                if self.life == 0 or enemy.puan == 100 or self.power <= 0:
                    addPoint()
                    print("Oyunun Kazananı:", enemy.pName)
                elif enemy.life == 0 or self.puan == 100 or enemy.power <= 0:
                    addPoint()
                    print("Oyunun Kazananı:", self.pName)

            def exit():
                print("Oyun Kapatılıyor...")
                addPoint()
                sys.exit()

        player1 = Player("Fahri")
        player2 = Player("Mahmut")
        while True:
            move = input("""
1-Saldır
2-Savun
3-Çık
Hamle Seçimi:
""")
            if (move == "1"):
                player1.atack(player2)
            elif move == "2":
                player1.defence(player2)
            elif move == "3":
                player1.exit
            else:
                errorPoint()

    def costCalc():
        def calcPrice(line):
            line = line[:-1]
            lists = line.split(",")
            cost = int(lists[1])/100*20
            fee = int(lists[1])/100*18
            income = int(lists[1])/100*25
            lastPrice = int(lists[1])+cost+fee+income
            return "Ürün: " + lists[0] + " || Satış Fiyatı: " + str(lastPrice) + "\n"

        with open("Costs.txt", "r", encoding="utf-8") as file:
            for l in file:
                product = []
                product.append(calcPrice(l))
                with open("salePrice.txt", "a", encoding="utf-8") as sell:
                    sell.writelines(product)

    def smartDicProject():
        import json
        from difflib import get_close_matches as match
        with open("myCodes/tools/data.json") as data:
            dicData = json.load(data)

        def dictionary(word):
            word = word.lower()
            if word in dicData:
                return dicData[word]
            elif (len(match(word, dicData.keys(), cutoff=0.8)) > 0):
                answer = input("Did you mean %s ? Y/N: " %
                               match(word, dicData.keys())[0])
                if (answer.lower() == "y"):
                    return dicData[match(word, dicData.keys())[0]]
                elif (answer.lower() == "n"):
                    return "The word doesn't exist!"
                else:
                    return "Error!"
            else:
                return "The word doesn't exist!"

        word = input("bir kelime giriniz : ")
        output = dictionary(word)
        if (type(output) == list):
            for i in output:
                print(i)
        else:
            print(output)


PyQt5.exp()
