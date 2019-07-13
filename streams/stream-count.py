import io

contents = "0123456789abcdefghijklmopqrstuvw"
contents = "0000s1100000e001023s0000001e0000111e000011s00000111e00000e0001110000e00000111e000001110000s"
contents = "s1100es1000e"
ssock = io.StringIO(contents)

#print('1. read(15)', ssock.read(15)) print('3. read()', )

eachRead = 5



while True:
    words = ssock.read(eachRead)
    print(words)

    #--start--


    #--end--

    if not words:
        break


ssock.close()
