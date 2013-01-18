from PyDAQmx import *
from PyDAQmx.DAQmxCallBack import *
from numpy import zeros



class Eyeball(object):
	def __init__(self):
		self.data = numpy.zeros((97,), dtype=numpy.uint8)
		self.i = 0
		self.err=""
		self.read, self.bytesPerSamp=int32(), int32()
		DAQmxResetDevice('dev1')
		self.taskHandle=TaskHandle()
		
		DAQmxCreateTask("",byref(self.taskHandle))
		

		DAQmxCreateDIChan(self.taskHandle,"Dev1/port4","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port7","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port10","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port2","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port5","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port0","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port3","",DAQmx_Val_ChanForAllLines)
		DAQmxCreateDIChan(self.taskHandle,"Dev1/port9","",DAQmx_Val_ChanForAllLines)
		
		DAQmxStartTask(self.taskHandle)

	def close(self):
		print "bye"
		
		DAQmxStopTask(self.taskHandle)
		DAQmxClearTask(self.taskHandle)


	def __del__(self):
		#self.close()
		pass

	def getData(self):
		
		DAQmxReadDigitalLines(self.taskHandle,1,10.0,DAQmx_Val_GroupByChannel,self.data,100,byref(self.read),byref(self.bytesPerSamp),None)
		index=0
		"""
		for each in self.data:
			
			print str(each)+":"+str(index)
			index=index+1
			"""
		all = [self.data[d] for d in range(0,95)]
		all = map(str, all)
		a
		return  [''.join((all[0:16])[::-1])+''.join((all[16:18])[::-1]), ''.join((all[24:32])[::-1])+"".join((all[32:40])[::-1]), ''.join((all[40:48])[::-1])+''.join((all[48:56])[::-1])+''.join((all[56:64])[::-1])]

	
if __name__=='__main__':
	t = Eyeball()
	#t.getData()
	print t.getData()



		

		
		
		
