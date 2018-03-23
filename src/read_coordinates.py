# import MDAnalysis
#
# ncdf = MDAnalysis.coordinates.TRJ.NCDFReader('../04_Hold_1.ncdf')
#
# print 'hello'

import MDAnalysis as mda

# Load simulation results with a single line
u = mda.Universe('../05_Prod1.ncdf')

# Select atoms
# ag = u.select_atoms('name OH')

# Atom data made available as Numpy arrays
# print ag.positions
# ag.velocities
# ag.forces

# Iterate through trajectories
fw = open('../05_Prod1.csv', 'w')
i = 0
for ts in u.trajectory:
    i = i + 1
    # print(ts)
    atom_num = 0
    for position in ts.positions:
        atom_num = atom_num + 1
        x,y,z = position
        fw.write(str(x) + ',' + str(y) + ',' + str(z) + ',')
        if atom_num == 6389:
            break

    fw.write('\r')


fw.close()
print(i)