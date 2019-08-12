file = input("File name: ")
print("")
app = open(file,"r")
contents = app.read()

def read():
    e = contents.strip()
    egg = e.startswith("int _main()")
    if(egg):
        eg = e.split(":" + "\n")[1]
        er = eg.startswith(" ")
        egg2 = e.endswith(";")
        y = e.split("print")[1]
        r = y.split("\");")[0]
        g = r.split("(\"")[1]
        def prfn():
            if(er):
                if(y):
                    if(g):
                        print(g)
                    else:
                        print("failed to find string area")
                else:
                    print("failed to find string area")
            else:
                print("no indent found after new line")

        if(egg2):
            prfn()
        else:
            print("missing ;")
    else:
        print("no detection of main int")

read()
