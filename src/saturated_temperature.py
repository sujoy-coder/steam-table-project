import pandas as pd
data=pd.read_csv('./src/dataset/steam-table_saturated.csv')
temperature=list(data['temperature'])

''' The excuation for given input temperature'''

def get_index(in_t):
    i=0
    for i in range(0,119):
        if temperature[i]==in_t:
            break
    return i

def get_index_for_interpolation(in_t):
    i=0
    for i in range(0,119):
        if temperature[i]>in_t:
            break

    return i

def calculate(l1,l2,in_t):
    l3=[]
    i=0
    for i in range(0,11):
        if i!=1:
            k=l2[i]+((l1[i]-l2[i])*(in_t-l2[1])/(l1[1]-l2[1]))
            l3.append(k)
        else:
            l3.append(in_t)
    return l3

def linerinterpolation(index,preindex,in_t):
    l1=list(data.iloc[index])
    l2=list(data.iloc[preindex])
    l3=calculate(l1,l2,in_t)

    return l3

def from_temperature(in_t):
    if in_t in temperature:
        index=get_index(in_t)
        var=list(data.iloc[index])
        return var
    else:
        index=get_index_for_interpolation(in_t)
        var=linerinterpolation(index,index-1,in_t)
    return var








