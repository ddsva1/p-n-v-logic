def maulkey(pk):
    g = pk[0]
    h = pk[1]
    t1 = #$Zq
    t2 = #$Zq
    caronpk = [g**t1,h**t2]
    rho = [t1,t2]
    return [caronpk,rho]

def maulcom(c,rho):
    return c**(rho**(-1))#caronc

def maul(alpha):
    alpha
    #depends on the protocol
    return [caronalpha, sigma]

def balopen(d,rho):
    m = d[0]
    r = d[1]
    t1 = rho[0]
    t2 = rho[1]
    caronr = r*t2*t1**(-1)
    return [m, caronr]#carond

def Open(pk,caronc,carond):
    g = pk[0]
    h = pk[1]
    m = carond[0]
    r = carond[1]
    if caronc == g**m * h**r:
        return m #beta
    else: 
        return False #beta

def Bal(gamma, sigma):
    gamma,sigma
    #??
    return carongamma

pk = #wait for pk to be sent from prover
arr1 = maulkey(pk) #(^PK,rho) <-- $maulkey(pk)
caronpk = arr1[0]
rho = arr1[1]
#send ^PK to verifier or verifier firewall

c = #wait for c to be sent back
caronc = maulcom(c, rho) #^c <-- Maulcom(c,rho)
#send caron c to prover

alpha = #wait for alpha to be sent
arr2 = maul(alpha)#(^alpha, sigma) <-- $maul(alpha)
caronalpha = arr2[0]
sigma = arr2[1]
#send ^alpha to verifier

d = #wait for d to be sent back
carond = balopen(d,rho)
#send ^d back to prover

gamma = #wait for gamma or quit signal
if "quit" sent:
    #send "quit" signal
    print("prover quitting!")
    input("press enter to quit!")
    quit()
else:
    beta = Open(pk, caronc,carond)
    if beta == False:
        carongamma = False
    else:
        carongamma = Bal(gamma,sigma)
    #send ^gamma to verifier or verifier firewall
    print('all done!')
    input("press enter to close terminal!")
    quit()