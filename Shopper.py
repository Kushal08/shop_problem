# this is to read csv files
import csv
import sys

if __name__ == "__main__":

    # opening csv file taking argument from command line
    f1 = open(sys.argv[1], 'rb')
    input_file = csv.reader(f1)
    
    # creating an empty list here.
    l1 = []
    # taking inputs from the command line
    desired_product = sys.argv[2:]
    # creating set of all desired product
    set_desired = set(desired_product)
    #print desired_product
    
	#defining three dictionaries to store products, price and desired shop and prices.
    products_dict = dict()
    price_dict = dict()
    final_dict = dict()

    count = 0;
    
    # iterating over all the entries in the file.
    for line in input_file:

    # print row
    	x = 0;
    	#combo = set([s.strip() for s in line[2:]])
    	#print combo
    	
  	if line[0] in products_dict:
        # append the new number to- the existing array at this slot
        	products_dict[line[0]].append(line[2].strip())
        	#print products_dict
    	else:
        # create a new array in this slot
        	products_dict[line[0]]=[line[2].strip()]

 	if line[0] in price_dict:
        # append the new number to the existing array at this slot
    		price_dict[line[0]].append(float(line[1]))
        	        	
    	else:
        # create a new array in this slot
        	price_dict[line[0]]=[float(line[1])]
	
	#x =  sum(price_dict[line[0]])
	#final_dict[line[0]] = x



	#print products_dict
	#print final_dict   

	# this is for finding those shops which have all the products one need.
    for k, v in products_dict.items():
    		#print(k, v)
    		x1 = set(v)
    		#print x1
    		#print set_desired
    		
    		if x1.intersection(set_desired) == set_desired:
    			l1.append(k)
    
    # checking whether the list l1 that contains all the shop numbers who have all desired products is empty or not		
    if not l1:
    	print "None"
    else:
    				
    	for p in l1:
    		x4=0
    		for q in desired_product:
    			x3 = products_dict[p].index(q)
    			x4 += price_dict[p][x3]
		    	
    		final_dict[p] = [float(x4)]
    	#print final_dict	

	# getting min price for a product corresponding to a shop
		shop = min(final_dict, key=final_dict.get)
    	print "==>"+shop+","+str(final_dict[shop])	
   
