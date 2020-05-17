#função manda comando
velocidade = "g"
portas = 48
x= 0
while x < portas:

    x+=1
    command = "show int {0}/0/{1} | i input".format(velocidade,x)
    print(command)
    #inputsw = pexpctet.sendline(command)
    #n = pexpctet.getline()

    #############################################

#função tratamento dos dado

n1 = "Last input 00:00:00, output 00:00:00, output hang neverola"
n2 = "Last input never, output never, output hang never"
n3 = "Last input never, output 7w5d, output hang never"

x=n2.replace(",","").split()
if x[2]=="never":
    print("sim")
if x[2]!="never":
    print("nao")
print(x[2]+x[1])