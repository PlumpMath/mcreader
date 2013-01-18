import os
import datetime as dt
import numpy as np
import h5py
import getData
import time

	
def bcd_to_int(bcd_str):
	string= ''
	return int(string.join([str(int(bcd_str[0:2],2)), str(int(bcd_str[2:6],2)), str(int(bcd_str[6:10],2)), str(int(bcd_str[10:14],2)), str(int(bcd_str[14:18],2))]))
	
def bin_to_int(bin_str):
	return int(bin_str,2)

def fileStruct(n_array):
	
	t=dt.datetime.now()
	date = t.strftime("%m-%d-%Y")
	time = t.strftime("%H-%M")
	if not os.path.exists(date):#this is the first file being created for that time
		os.makedirs(date)
	
	path = '/'.join((date,time))
	path = '.'.join((path,"h5"))
	print(path)
	#fn = os.path.join(os.path.dirname(__file__), 'my_file')
	#Sprint(fn)
	
	with h5py.File(str(path), 'w') as h5file:
		h5file.create_dataset("data", data=n_array)
		#set = h5file.create_dataset("data", (100, 100), 'i')
	
	

class datacollector(object):
	def __init__(self):
		self.index = 0
		self.data = np.zeros(1, dtype=[("el", np.int), ("az", np.int), ("time", np.int)])
	def add(self,az,el,time):
		self.data.resize(self.index+1, 1)
		self.data[self.index] = ((az,el,time))
		
		self.index =self.index+ 1
		
	def getData(self):
		return self.data
	
	
if __name__=='__main__':
	'''print(bcd_to_int('101001000000000001'))
	print(bin_to_int('0011'))
	all = getData.getData()
	all = (bcd_to_int(all[0]), bin_to_int(all[1]), bin_to_int(all[2]))
	data = np.zeros(1000, dtype=[("first", np.int), ("second", np.int), ("third", np.int)])
	data[1]=all
	fileStruct(data)
	'''
	data = np.zeros(1000, dtype=[("first", np.int), ("second", np.int)])
	eye = getData.Eyeball()
	Data = datacollector()
	#fileStruct(Data.getData())

	
	while True:
		#time_a = time.time()
		
		
		#timer loop
		all = eye.getData()
		
		all = (bcd_to_int(all[0]), bin_to_int(all[1]), bin_to_int(all[2]))
	
		Data.add(all[0],all[1],all[2])
		print Data.getData()
		
		fileStruct(Data.getData())
		
		
		
		#time_b = time.time()
		#delta = time_b-time_a
		
		#print delta
		
		#time.sleep(.03-delta)
		
		