#!/usr/bin/env python

import numpy as np

def read_antfile():
	antdata = np.loadtxt("pueo_antpos.txt", skiprows=1, delimiter=',')

	tantdata = np.transpose(antdata)

	antarr = np.recarray(len(tantdata[0]), dtype=[('ant_id', int), ('x', float), ('y', float), ('z', float)])

	antarr['ant_id'] = tantdata[0]
	antarr['x'] = tantdata[1]
	antarr['y'] = tantdata[2]
	antarr['z'] = tantdata[3]

	return antarr

if __name__=="__main__":
	antfile = read_antfile()
	print(antfile)
