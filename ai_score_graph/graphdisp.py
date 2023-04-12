from ai_scores import *
import matplotlib.pyplot as plt
from math import ceil
import numpy as np
import operator
from scipy.interpolate import make_interp_spline

def split():
    tmp = get_scores()
    scores = sort_scores(tmp)
    x = []
    y = []
    for elm in scores:
        x.append(elm[0])
        y.append(elm[1])
    return (x,y)

def create_line_plot(prc,gr_type,vline= -1.0):
    plt.rcParams.update({'font.size': 6})
    y = split()[1]
    limit = math.ceil(max(y)+prc)
    val = share_out(prc,y,limit)

    data = [0] * math.ceil(limit* (1/prc))
    j = 0
    for i in range(len(data)):
        data[i] = round(j,1)
        j += prc

    fig = plt.figure(figsize = (12,7))
    if gr_type == 'bar':
        plt.bar(data,val,color='green',width=prc,
                edgecolor='black', align='edge',label='Class results')
    else:
        x_y_spline = make_interp_spline(data,val)
        _x = np.linspace(min(data),max(data),500)
        _y = x_y_spline(_x)
        plt.plot(_x,_y,color='blue',label='Class results')
    plt.axvline(x = vline,color ='red',linestyle='--',label='ID score')

    plt.xlabel('Scores')
    plt.ylabel('Student')
    plt.xticks(np.arange(0,limit,step=prc))
    plt.xlim([0,max(data)+prc])
    plt.ylim([0,max(val)+prc])

    plt.title('Repartition of notation in AI class')
    plt.legend(loc='best')
    plt.show()

def share_out(prc, l, limit):
    nb_dash = math.ceil(limit * (1/prc))
    res = [0] * nb_dash
    for src in l:
        index = int(src/prc)
        res[index] +=1
    return res


