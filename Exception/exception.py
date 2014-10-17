#/usr/bin/python
soucet = 0
while True:
    try:
        soucet += int(raw_input())
    except KeyboardInterrupt, e:
        print(soucet)
        print("huehuehue, vypnul jsi se.")
        exit(0)
    except ValueError, e:
        print("Spatna volba.")
        continue