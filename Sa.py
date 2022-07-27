import warehouse_ar as wr
import numpy as np
import math

def objetivo(e,d,l):
    count=0
    g=wr.training(e,d,l)
    while g==10 and count !=10:
        g=wr.training(e,d,l)
        count+=1
    return g

def S_init():
    e = 0.7 #the percentage of time when we should take the best action (instead of a random action)
    d = 0.89 #discount factor for future rewards
    l = 0.5 #the rate at which the agent should learn
    return e,d,l

def SA():
    alpha =0.90
    it = 10
    Tf = 1
    T0 = 10
    s=S_init()
    print(s)
    valor=objetivo(s[0],s[1],s[2])
    print("Episodios iniciai:", valor)
    
    Xb = s
    xxb=valor

    T = T0
    while T >= Tf:
        for i in range(it):
            #print('-----------------ITERAÇÃO------------------')
            xx=objetivo(s[0],s[1],s[2])
            Y=s
            rd = np.random.randint(0,2)
            if rd == 0:
                N1(Y)
                
            elif rd == 1:
                N2(Y)

            elif rd == 2:
                N3(Y)
            yy=objetivo(Y[0],Y[1],Y[2])
            print(Y)
            if yy==10:
                continue
            delta = yy-xx
            if delta <= 0:
                SOL = Y
                xx = yy
            else:
                rr = (np.random.randint(0,100))/100
                if rr < math.exp(-delta/T):
                    SOL = Y
                    xx = yy
            if xx < xxb:
                Xb = SOL
                xxb = xx
            #print(xxb)
        T=alpha*T
    s=Xb    
    solucao=xxb
    print("Minimo de episodios: ", solucao)
    print("Parametros otimos: ", s)
    

     
def N1(s):
    e,d,l=s
    j=random_neighbour(e)
    s=(j,s,l)
    print(s)
def N2(s):
    e,d,l=s
    j=random_neighbour(d)
    s=(e,j,l)
def N3(s):
    e,d,l=s
    j=random_neighbour(l)
    s=(e,d,j)

def random_neighbour(x, fraction=1):
    """Move a little bit x, from the left or the right."""
    amplitude = fraction / 10
    delta = (-amplitude/2.) + amplitude * np.random.random_sample()
    return x+delta

SA()