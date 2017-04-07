import csv
import sys

if __name__ == "__main__":

    # opening csv file taking argument from command line
    f1 = open(sys.argv[1], 'rb')
    input_file = csv.reader(f1)
    
    l1 = []
    # taking inputs from the command line
    desired_product = sys.argv[2:]
    set_desired = set(desired_product)
    #print desired_product
    years_dict = dict()
    another_dict = dict()
    final_dict = dict()
    last_dict = dict()
    count = 0;
    for line in input_file:

    # print row
    	x = 0;
    	#combo = set([s.strip() for s in line[2:]])
    	#print combo
    	
  	if line[0] in years_dict:
        # append the new number to- the existing array at this slot
        	years_dict[line[0]].append(line[2].strip())
        	#print years_dict
    	else:
        # create a new array in this slot
        	years_dict[line[0]]=[line[2].strip()]

 	if line[0] in another_dict:
        # append the new number to the existing array at this slot
    		another_dict[line[0]].append(float(line[1]))
        	        	
    	else:
        # create a new array in this slot
        	another_dict[line[0]]=[float(line[1])]
	
	x =  sum(another_dict[line[0]])
	final_dict[line[0]] = x



	#print years_dict
	#print final_dict   

    for k, v in years_dict.items():
    		#print(k, v)
    		x1 = set(v)
    		#print x1
    		#print set_desired
    		
    		if x1.intersection(set_desired) == set_desired:
    			l1.append(k)
    		
    			
    
    min1 = final_dict['1']
    
    if not l1:
    	print "None"
    else :
    	for p in l1:
    		if min1 > final_dict[p]:
    			min1 = final_dict[p]
        	        shop = p;
                
    	print "==> " + shop +", "+str(min1)
    
    			
