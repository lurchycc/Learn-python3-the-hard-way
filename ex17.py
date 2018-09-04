from sys import argv
from os.path import exists

script,from_file,to_file=argv
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
#indata= open(from_file).read()
#indata= in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exists? {exists(to_file)}")
#print("Ready,hit RETURN to continue,CTRL-C abort.")
#input()

open(to_file,'w').write(open(from_file).read())
#out_file.write(indata)

print("Alright,all done!")


#to_file.close()

#from_file.close()