#!/usr/bin/python

import sqlite
import sys

try:

    con = sqlite.connect("programko.db")
    cur = con.cursor()
    SQLselect = 'SELECT * from kontakty order by jmeno;'
    SQLdelete = 'DELETE FROM kontakty WHERE id=%d;'
    SQLinsert = 'INSERT INTO kontakty values (null, \'%s\', \'%s\', %d);'
    SQLupdateParams = ''
    SQLupdate = 'UPDATE kontakty SET %s WHERE id=%d;'
    while True:
        cur.execute(SQLselect)
        print "1.Zobrazit kontakt | 2.Pridat kontakt | 3.Smazat kontakt"
        cislo=int(raw_input("Zadejte operaci: "))
        i = 1
        if cislo == 1:
            print "-----------Kontakty-----------"
            for zaznam in cur.fetchall():
                print "ID: %s | Jmeno: %s" %(i , zaznam[1])
                i += 1
            print "------------------------------"
            cisloKontaktu=int(raw_input("Zadejte cislo kontaktu: "))
            cur.execute(SQLselect)
            zaznam = cur.fetchall()
            print "Jmeno:      %s" %zaznam[cisloKontaktu-1][1]
            print "Prijmeni:   %s" %zaznam[cisloKontaktu-1][2]
            print "Tel. Cislo: %s" %zaznam[cisloKontaktu-1][3]
            print "1.Pridat kontakt | 2.Smazat kontakt | 3.Smazat tento kontakt | 4.Upravit tento kontakt"
            cislo=int(raw_input("Zadejte operaci: "))
            cislo += 1
            if cislo == 5:
                i=zaznam[cisloKontaktu-1][0]
            if cislo == 4:
                cislo = 99
                i=zaznam[cisloKontaktu-1][0]

        if cislo == 2:
            jmeno=raw_input("Zadejte jmeno: ")
            prijmeni=raw_input("Zadejte prijmeni: ")
            telCislo=raw_input("Zadejte tel. cislo: ")
            if telCislo != '':
                telCislo = int(telCislo)
            else:
                telCislo = 0
            SQLinsert = SQLinsert %(jmeno, prijmeni, telCislo)
            cur.execute(SQLinsert)
            con.commit()
            print "Uspesne pridano"
        if cislo == 3:
            print "-----------Kontakty-----------"
            for zaznam in cur.fetchall():
                print "ID: %s | Jmeno: %s" %(i , zaznam[1])
                i += 1
            print "------------------------------"
            radek=int(raw_input("Zadejte id ke smazani: "))
            cur.execute(SQLdelete, radek)
            con.commit()
            print "Uspesne smazano"
        if cislo == 5:
            jmeno=raw_input("Zadejte jmeno: ")
            prijmeni=raw_input("Zadejte prijmeni: ")
            telCislo=raw_input("Zadejte tel. cislo: ")
            if telCislo != '':
                telCislo = int(telCislo)
            else:
                telCislo = 0
            if jmeno != '' and prijmeni != '' and telCislo != 0:
                SQLupdateParams = "jmeno='%s',prijmeni='%s',cislo=%d" %(jmeno, prijmeni, telCislo)
            elif jmeno != '' and prijmeni != '':
                SQLupdateParams = "jmeno='%s',prijmeni='%s'" %(jmeno, prijmeni)
            elif jmeno != '' and telCislo != 0:
                SQLupdateParams = "jmeno='%s',cislo=%d" %(jmeno, telCislo)
            elif prijmeni != '' and telCislo != 0:
                SQLupdateParams = "prijmeni='%s',cislo=%d" %(prijmeni, telCislo)
            elif jmeno != '':
                SQLupdateParams = "jmeno='%s'" %jmeno
            elif prijmeni != '':
                SQLupdateParams = "prijmeni='%s'" %prijmeni
            elif telCislo != '':
                SQLupdateParams = "cislo=%d" %telCislo

            if SQLupdateParams != '':
                SQLupdate = SQLupdate %(SQLupdateParams, i)
                print SQLupdate
                cur.execute(SQLupdate)
                con.commit()
                print "Uspesne zmeneno"


        if cislo == 99:
            cur.execute(SQLdelete, i)
            con.commit()
            print "Uspesne smazano"

except sqlite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con != None:
        con.close()