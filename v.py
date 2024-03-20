def Com(caronpk, m)
    g = caronpk[0]
    h = caronpk[1]
    r = # $random Zq
    #m = beta
    c = (g**m) * (h**r)
    d = [m,r]
    return [c,d]

def V(x,arr):
    caronalpha = arr[0]
    beta = arr[1]
    carongamma = arr[2]
    x, caronalpha, beta, carongamma
    #???
    answer = "do V!" #change this obv
    return answer

x=#x

caronpk = #wait for ^pk
beta = #${0,1}^L
arr1 = Com(caronpk, beta)#$Com(caronpk,beta)
c = arr1[0]
d = arr1[1]
#send out c to either prover group or to verifier witness

caronalpha = #wait for ^alpha to be sent
#send out d

carongamma = #wait for carongamma to be sent
if carongamma == "quit":
    print("yikes! verifier was found out!")
else:
    ans = V(x,[caronalpha,beta,carongamma])
    if ans == 1:
        print("equals one")
    elif ans == "do V!":
        print("function v in v.py not completed!")
    else:
        print("equals zero")

input("press enter to quit!")
quit()