#!/usr/bin/python

import sqlite
import sys

try:

    con = sqlite.connect("programko.db")
    cur = con.cursor()
    SQLselect = 'SELECT * from kontakty order by jmeno;'
    SQLdelete = 'DELETE FROM kontakty WHERE id=%d;'
    SQLupdate = 'UPDATE kontakty SET jmeno=%s,prijmeni=%s,cislo=%d WHERE id=%d;'

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
            cislo = 6
            i=zaznam[cisloKontaktu-1][0]

    if cislo == 2:
        jmeno=raw_input("Zadejte jmeno: ")
        prijmeni=raw_input("Zadejte prijmeni: ")
        telCislo=int(raw_input("Zadejte tel. cislo: "))
        execute = 'INSERT INTO kontakty values (null, \'%s\', \'%s\', %d);' %(jmeno,prijmeni,telCislo)
        cur.execute(execute)
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
        telCislo=int(raw_input("Zadejte tel. cislo: "))

    if cislo == 6:
        cur.execute(SQLdelete, i)
        con.commit()
        print "Uspesne smazano"

except sqlite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con != None:
        con.close()