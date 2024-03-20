def maulkey(pk):
    g = pk[0]
    h = pk[1]
    t1 = #$Zq
    t2 = #$Zq
    caronpk = [g**t1,h**t2]
    rho1 = [t1,t2]
    return [caronpk,rho1]

def randcom(c,rho1):
    c, rho1
    #???
    return [caronc, rho2]

def maul(alpha):
    alpha
    #???
    return [caronalpha, sigma]

def balopen(d,arr):
    m = d[0]
    r = d[1]
    rho1 = arr[0]
    rho2 = arr[1]
    caronr = r*rho2*rho1**(-1)
    return [m,caronr]#carond

def Open(pk, caronc,carond):
    g = pk[0]
    h = pk[1]
    m = carond[0]
    r = carond[1]
    if caronc == g**m * h**r:
        return m #beta
    else: 
        return False #beta
    
def Bal(gamma, sigma):
    gamma, sigma
    #???
    return carongamma

pk = #wait for pk from prover group
arr1 = maulkey(pk) #(^pk, rho1) <-- $maulkey(pk)
caronpk = arr1[0]
rho1 = arr1[1]
#send to verifier ^pk

c = #wait for c from verifier
arr2 = randcom(c,rho1) #(^C,rho2) <-- $randcom(c,rho1)
caronc = arr2[0]
rho2 = arr2[1]
#send ^c to prover group

alpha = #wait for alpha from prover group
arr3 = maul(alpha)#(^alpha, sigma) <--$maul(alpha)
caronalpha = arr3[0]
sigma = arr3[1]
#send ^alpha to verifier

d = #wait for d from verifier
carond = balopen(d,[rho1, rho2])
#send ^d to prover group

gamma = #wait for gamma or quit signal
if gamma == "quit":
    #send "quit" to verifier to quit due to being false
    print("yikes! prover group quit")
    input("press enter to quit!")
    quit()
else:
    caronbeta = Open(pk,caronc,carond)
    if caronbeta == False:
        carongamma = False
    else:
        carongamma = Bal(gamma,sigma)
    #send carongamma to verifier
    print("all done! quitting")
    input("press enter to quit!")
    quit()