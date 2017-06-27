import sys,platform
print "Version of python Interperter is: " + sys.version # gives the version of python interpreter
print "Python architecture is :" + str(platform.architecture()) # gives if Python is 32 or 64 bit
print "The following modules are installed on the machine :\n"
#help("modules")
import sunaudio
print('sunaudio: {}'.format(sunaudio.MAGIC))
print chr(230)