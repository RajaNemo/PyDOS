import time

nm = input("What is your name? ")

print("Hello, " + nm + " !")

print("How can I help you, " + nm + " ?")

while 1:


    print("1.Cal = Calculator")
    print("2.Dct = Dictionary")
    print("3.Shk = ShakespeareWrite")
    print("4.Art = Aristotle")
    print("5.Vgn = Van Gogh")
    opt = input("What operation would you like to perform? ")



    if opt == "cal":

        print("1.Add")
        print("2.Substract")
        print("3.Multiply")
        print("4.Divide")

        l = input("Would you like to multiply, divide, add or substract?")


        n = input("First number: ")
        b = input("Second number: ")
        a = float(n)+float(b)
        s = float(n)-float(b)
        m = float(n)*float(b)
        d = float(n)/float(b)
        p = float(n)%float(b)



        if l == "1":
            print("The result is ", a)
        if l == "2":
            print("The result is", s)
        if l == "3":
            print("The result is", m)
        if l == "4":
            print("The result is", d, "+ remaining", p,)
    if opt == "shk":
       exec(open('shkwrt.py').read())
    if opt == "dct":
        print("1.Cal = Calculator")
        print("2.Dct = Dictionary")
        print("3.Shk = ShakespeareWrite")
    if opt == "art":
        exec(open('arist.py').read())

    if opt == "vgn":
        exec(open('vangogh.py').read())

time.sleep(70)



