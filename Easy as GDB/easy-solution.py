import time, string, gdb

flag = list("------------------------------")
FLAGLEN = len(flag) 
ALLOWED_CHARS = "{}_" + string.ascii_letters + string.digits

gdb.execute("file brute")
gdb.Breakpoint("*0x5655598e")
gdb.execute("run << " + "(python -c 'print(\"" + ''.join(flag) + "\")')")

for f in range(0, FLAGLEN, 1):
    
    dl = gdb.parse_and_eval("$dl")
    al = gdb.parse_and_eval("$al")

    if dl == al:
        gdb.execute("c")
    else:
        for char in ALLOWED_CHARS:
            flag[f] = char
            gdb.execute("run < " + "<(python -c 'print(\"" + ''.join(flag) + "\")')")
            for con in range(0,f):
                gdb.execute('c')

            dl = gdb.parse_and_eval("$dl")
            al = gdb.parse_and_eval("$al")

            if dl == al:
                gdb.execute('!clear')
                print("Got the char: [" + char + "]!\n Flag is now: " + ''.join(flag))
                time.sleep(5) 
                gdb.execute('c')
                break
    gdb.execute('!clear')
    print("Flag: {}".format(''.join(flag)))
gdb.execute('q')
