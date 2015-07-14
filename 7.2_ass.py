fname = raw_input('Enter the file name: ')
try :
	fh = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
count = 0
total = 0.0
for line in fh :
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :   continue
    count = count + 1
    floatpos = line[20:]
    con = float(floatpos)
    total = total + con
    
print 'Average spam confidence:', total / count
