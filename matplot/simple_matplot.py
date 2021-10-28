#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
from matplotlib import gridspec
import pandas as pd
import os

# 0. font
#font_name=font_manager.FontProperties(fname='/usr/share/fonts')

if __name__ == '__main__':
    df=pd.read_csv(f'{os.getcwd()}/file.csv', index_col='idx')

    png_name=f'{os.getcwd()}/picture.png'

    title='L2 Cache Hit Ratio'

    colors=['fuchsia', 'orange', 'gold', 'limegreen', 'blue', 'darkblue']

    ax1=plt.figure(figsize=(5,4))
    gs=gridspec.GridSpec(nrows=1, ncols=1, bottom=0.15, top=0.92)
    ax1=plt.subplot(gs[0])
    ax2=ax1.twinx()
    lines=[]
    labels=[]

    line1=ax1.plot(df['name'],df['score'],color=colors[0],linewidth=2)
    lines.append(line1[0])
    labels.append('score!')

    line2=ax2.plot(df['name'],df['weight'],color=colors[3],linewidth=2)
    lines.append(line2[0])
    labels.append('weight!')

    ax1.set_xlabel('Name')
    ax1.set_ylabel('Score')
    ax2.set_ylabel('Weight')
    ax1.grid(True)

    ax1.set_title(title,fontsize=5)
    plt.legend(lines,labels,fontsize=10,loc='upper left')
    plt.savefig(png_name)
    plt.close()