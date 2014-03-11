import getopt, sys,csv,codecs
class read_Stock(file):   
    def __init__(self, fp):
        self.read_file(fp)
    
    def read_file(self, fp = None):        
        records_data = [row for row in csv.reader(codecs.open(fp, 'rb', encoding="utf_8"))]        
        row_count= (sum(1 for row in records_data)) -1
        matched_columns = False
        column_match =1
        while matched_columns == False:
            column_match +=1
            try:
                col_matched = records_data[0][column_match]
            except:
                matched_columns=True
        column_count=column_match-1
        CcompanyStart = 2
        Selected_company=[]
        while CcompanyStart <= (column_count):
            rowIndex=1
            highestShare=rowIndex
            while rowIndex <=row_count:
                try:
                 if int(records_data[highestShare][CcompanyStart]) <= int(records_data[rowIndex][CcompanyStart]):
                    highestShare=rowIndex                
                 rowIndex+=1
                except:
                    print "Please Select Valid CSV file"
                    return 1
            Selected_company.append(str(records_data[0][CcompanyStart])+": "+str(records_data[highestShare][0]) +", "+str(records_data[highestShare][1])+", "+str(records_data[highestShare][CcompanyStart]))
            CcompanyStart +=1
        print '######################\n'
        for item in Selected_company:
            print item
        print '\n######################'


def main():
    try:
        fnopt, args = getopt.getopt(sys.argv[1:], "v:c")
    except getopt.GetoptError as err:        
        sys.exit("Usage: %s -v <Pass csvfile in the Program>" % (sys.argv[0]))
    for o, value in fnopt:
            if o == '-v':
                try:
                    sa = read_Stock(value)                    
                except (StockException), e:
                    print e
                finally:
                    sys.exit()             
    sys.exit("Usage: %s -v <Pass csvfile in the Program>" % (sys.argv[0]))

if __name__ == "__main__":
    main()
