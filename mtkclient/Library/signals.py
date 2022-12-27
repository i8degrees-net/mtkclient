import signal
# import time
 
def handler(signum, frame):
	print("Application is terminating... CTRL+C was signaled.")
	exit(6)
 
signal.signal(signal.SIGINT, handler)
