import logging as lg

lg.basicConfig(filename='Test.log',level=lg.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    lg.info("I am trying to read a file")
    with open("subash.txt",'r'):
        lg.info("successfully it has read thr file")
except Exception as e:
    lg.critical("this is a situation for us")
    lg.exception(e) #this will return entire error message
    lg.error(e) #this will only error message only
