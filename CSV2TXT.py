import csv
def ReadCSV(filename):
    file = open(filename, encoding='utf-8')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row[1:])
    return rows

def RemoveIDfromTXT(input_filename,output_filename):
    #path = 'taxonomy.zh-TW.txt'
    fReader = open(input_filename,'r',encoding='utf-8')
    fWriter = open(output_filename,'w',encoding='utf-8')
    for row in fReader.readlines():
        fWriter.write(row .split('-')[1][1:])
    fWriter.close()
    fReader.close()

'''
def WriteCSV(rows, output_filename):
    path = output_filename
    f = open(path, 'w')
    for row in rows:
        for i in range(len(row)):
            f.write(row[i])
'''


if __name__ == "__main__":
    CatRow = ReadCSV('taxonomy-with-ids.zh-TW.csv')
    print(CatRow)
    RemoveIDfromTXT('taxonomy-with-ids.zh-TW.txt','taxonomy.zh-TW.txt')