import pandas as pd
data=pd.read_csv('./src/dataset/steam-table_saturated.csv')
pressure=list(data['pressure'])

''' The excuation for given input pressure'''

def get_index(in_p):
    i=0
    for i in range(0,119):
        if pressure[i]==in_p:
            break
    return i

def get_index_for_interpolation(in_p):
    i=0
    for i in range(0,119):
        if pressure[i]>in_p:
            break

    return i

def calculate(l1,l2,in_p):
    l3=[]
    l3.append(in_p)
    i=1
    for i in range(1,11):
        k=l2[i]+((l1[i]-l2[i])*(in_p-l2[0])/(l1[0]-l2[0]))
        l3.append(k)
    
    return l3

def linerinterpolation(index,preindex,in_p):
    l1=list(data.iloc[index])
    l2=list(data.iloc[preindex])
    l3=calculate(l1,l2,in_p)

    return l3

def from_pressure(in_p):
    if in_p in pressure:
        index=get_index(in_p)
        var=list(data.iloc[index])
        return var
    else:
        index=get_index_for_interpolation(in_p)
        var=linerinterpolation(index,index-1,in_p)
    return var

def round_off(lst, n=8):
    i=0
    for i in range(len(lst)):
        lst[i]=round(lst[i],n)
    return lst







