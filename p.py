def Gen():
    g = #sample from BIG G excluding 1(BIG G)
    h = #sample from BIG G excluding 1(BIG G)
    return [g,h] #pk

def Open(pk, c, d):
    g = pk[0]
    h = pk[1]
    m = d[0]
    r = d[1]
    if c == g**m * h**r:
        return m
    else: 
        return False

def P1(x, w, a):
    x, w, a #used
    #???
    return alpha

def P2(x,w,beta,alpha):
    x,w,beta, alpha#used
    #?????
    return gamma


x=#x
w=#w
a = #??????

pk = Gen()#$Gen(1^lambda)
#send pk to either prover firewall or verifier group

caronc = #wait for ^C to be sent from prover firewall or verifier group
alpha = P1(x,w,a)
#send alpha to prover firewall or verifier group

carond = #wait for ^D to be sent
beta = Open(pk,caronc,carond)
if beta !=False:
    gamma = P2(x,w,beta,alpha)
    #send gamma out
    print('done! all good - beta not false!')
    input("press enter to quit!")
    quit()
else:
    print('yikes! beta found to be false! quitting')
    #send "quit" signal out
    input("press enter to quit!")
    quit()


