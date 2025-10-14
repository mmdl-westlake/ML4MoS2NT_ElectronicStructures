import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from matplotlib.ticker import ScalarFormatter


arial_path = '/fs2/home/huangju/software/miniconda3/envs/deeph2/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/arial.ttf'

if not os.path.exists(arial_path):
    raise FileNotFoundError(f"Font file not found at {arial_path}")

fm.fontManager.addfont(arial_path)

arial_font = fm.FontProperties(fname=arial_path)

plt.rcParams['font.family'] = arial_font.get_name()

SMALL_SIZE = 10
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=SMALL_SIZE)
plt.rc('axes', labelsize=SMALL_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.rc('axes', linewidth=1)
plt.rc('figure', figsize=(3.33,0.75*3.33))
plt.rc('figure', dpi=300)


train_loss = pd.read_csv('./train_loss.csv')
validation_loss = pd.read_csv('./validation_loss.csv')
lr = pd.read_csv('./learning_rate.csv')

fig, ax1 = plt.subplots()

ax1.plot(train_loss['Step'], train_loss['Value'] * 1e6, label='Train Loss', color='#8db7d2')
ax1.plot(validation_loss['Step'], validation_loss['Value'] * 1e6, label='Validation Loss', color='#C74375')
ax1.set_xlabel(r'$N$')
ax1.set_ylabel(r'Loss ($\mathrm{eV}^2$)', color='#8db7d2')

ax2 = ax1.twinx()
ax2.plot(lr['Step'], lr['Value'] * 1e3, label='Learning Rate', color='#2ca02c')
ax2.set_ylabel('Learning Rate', color='#2ca02c')

ax1.set_ylim(0, 100)  
ax2.set_ylim(0, 4) 
ax1.tick_params(axis='y', labelcolor='#8db7d2')
ax2.tick_params(axis='y', labelcolor='#2ca02c')

ax1.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.yaxis.get_offset_text().set_fontsize(SMALL_SIZE)
ax2.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax2.yaxis.get_offset_text().set_fontsize(SMALL_SIZE)

ax1.annotate(r'$\times 10^{-6}$', xy=(1, 1), xytext=(-180, 10),
             xycoords='axes fraction', textcoords='offset points',
             ha='left', va='center', color='#8db7d2')

ax2.annotate(r'$\times 10^{-3}$', xy=(1, 1), xytext=(0, 10),
             xycoords='axes fraction', textcoords='offset points',
             ha='left', va='center',color='#2ca02c')



fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85), fontsize=8, frameon=False)
ax1.tick_params(axis='both',      
                which='both',      
                direction='in')
ax2.tick_params(axis='both',    
                which='both',   
                direction='in')
fig.tight_layout()

plt.savefig('train_validation_loss_lr.png',bbox_inches="tight", dpi=800)
plt.savefig('train_validation_loss_lr.pdf',bbox_inches="tight")

