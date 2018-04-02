from pfac.spm import *
from pfac import const
import os

z = 3
neles = range(1, 3)

dir0 = './'
den = [1.0]

for nele in neles:
    dir1 = './'
    (temp, logt, population) = get_tgrid(z, nele)
    # just use three entries in temp
    temp = temp[::5]
    print 'NION = 2'
    spectrum([nele], temp, den, population,
             'Li', dir0=dir0, dir1=dir1, nion=2)
    print 'NION = 1'
    spectrum([nele], temp, den, population,
             'Li', dir0=dir0, dir1=dir1, nion=1)

    
