#!/usr/bin/python

import sys


def main(thing):
    """
	Use binary search to guess some number between 1 and 1000
	
    thing = thing you're looking for
    big_thing = list of int
    counter = n passes through loop
	n = current guess
		
    """
    thing = int(thing)    
    big_thing = [x for x in range(1,1000,1)]  
    counter = 0
    n = 0 
    while counter < 11:
        n = big_thing[len(big_thing)//2]
        counter += 1
        print('n is: '+str(n))			
        if thing > n:
            print('higher')
            big_thing = big_thing[len(big_thing)//2:len(big_thing)]
        elif thing < n:
            print('lower')
            big_thing = big_thing[0:len(big_thing)//2]   
        else:
            break
    print('n is thing! counter: '+str(counter)+' big_thing: '+str(big_thing))
    return counter   

	
if __name__ == '__main__':
    main(sys.argv[1])
