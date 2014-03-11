Name : Jitesh agrawal

Contents  
        Introduction
		Environment 
		get_highestStock.py
		invalid_stock_pricelist.csv
		valid_stock_pricelist.csv
		unit_test screen shot
        
		
Introduction :

This package is used to get high stocks price of the stock with month and year 

Environment :
	Python 2.7 
	Linux OS
	
get_highestStock.py :
     Python file. this python file content a function that is used for retrieve the csv file content and return a highest stocks price of stocks list with month and year.
	 
invalid_stock_pricelist.csv : csv invalid file use for unit testing
valid_stock_pricelist.csv : csv valid file use for unit testing
	
Example:
  PYTHONPATH FILENAME -v CSV FILE NAME
  eg:1) I/P :- python get_highestStock.py -v valid_stock_pricelist.csv
        O/P :- ##################
		       ITC : 2008, Dec, 680
		       PVR :2007, Jun, 780
		       TATAMOTORS : 2012, Mar, 880
		       ##################
  
  
  
  eg:2)  I/P :- python get_highestStock.py -v invalid_stock_pricelist.csv
         O/P :- Please select valid CSV file
  
	