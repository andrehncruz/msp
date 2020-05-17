def pegadados(status):
    x = status.replace(",","").split()
    print(x)
    posicao2 = x[2]
    posicao4 = x[4]
    posicao7 = x[7]
    last=[]
    if x[2] == "never":
        last.insert(posicao2)
    if x[2] != "never":
        last.insert(posicao2)
    if x[4]=="never":
        info = ('never')
        return info
    if x[4] != "never":
        info = x[4]
        return info
    if x[7]=="never":
        info = str('Never')
        return info
    if x[7] != "never":
        info = x[7]
        return info
status = "Last input 00:00:03, output 00:00:00, output hang never"
resultado = pegadados (status)
print (resultado)

#n2= status
#x=n2.replace(",","").split()
#if x[2]=="never":
    #print("sim")
#if x[2]!="never":
   # print("nao")

last[2] = 0

last[2] = 0+24