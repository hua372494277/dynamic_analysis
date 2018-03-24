
from scipy.io import netcdf
f = netcdf.netcdf_file('..\\..\\05_Prod4.nc', 'r', mmap=True)
fw = open('.\\05_Prod4.csv', 'w')
i = 0
for structure in f.variables['coordinates']:
    i = i + 1
    # print(ts)
    atom_num = 0
    for position in structure:
        x,y,z = position
        atom_num = atom_num + 1
        fw.write(str(x) + ',' + str(y) + ',' + str(z) + ',')
        if atom_num == 6389:
            break

    fw.write('\r')

fw.close()
f.close()
print(i)
