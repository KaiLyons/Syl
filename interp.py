file = input("File name: ")
print("")
app = open(file,"r")
contents = app.read()

def read():
    e = contents.strip()
    egg = e.startswith("int _main()")
    if(egg):
        eg = e.split(":")[1]
        egg2 = e.endswith(";")
        egr = eg.strip()
        y = e.split("print")[1]
        r = y.split("\")")[0]
        g = r.split("(\"")[1]
        def prfn():
            if(egr.startswith("print")):
                if(y):
                    if(y.startswith("(")):
                        print(g)
                    else:
                        print("failed to find string area")
        if(egg2):
            prfn()
        else:
            print("missing ;")
    else:
        print("no detection of main int")

read()
