'''
   See README.md
'''
#
# Open the input file
infile = open("textinput.txt", mode = "r")
# Create the ouptput file
outfile = open("adiforimport.adi", mode = "w")
#
# Heading 
#outfile.write('<?xml version="1.0" encoding="UTF-8"?>')
#outfile.write("\n")
#outfile.write('<ADX>')
#outfile.write("\n")
#outfile.write("\n")
#outfile.write('  <HEADER>'+"\n"+'  </HEADER>'+"\n")
#outfile.write("\n")
#outfile.write('  <RECORDS>'+"\n")
#outfile.write("\n")
#
# Parse the line into segments
qso = infile.readline()
while qso:
  checkline = qso.split()[0][0:4]
  if checkline == 'date': 
    qso = infile.readline()
  qsosplit = qso.split()
  #get the band from the freq
  freq = int(qsosplit[1])
  if freq in range(135,138,):
      band = '2200M'
  if freq in range(472,479,):
      band = '600M'
  if freq in range(1800,2000,):
      band = '160M'
  if freq in range(3500,4000,):
      band = '80M'
  if freq in range(5330, 5410,):
      band = '60M'
  if freq in range(7000,7300,):
      band = '40M'
  if freq in range(10100,10150,):
      band = '30M'
  if freq in range(14000,14350,):
      band = '20M'
  if freq in range(18068,18168,):
      band = '17M'
  if freq in range(21000,21450,):
      band = '15M'
  if freq in range(24890,24990,):
      band = '12M'
  if freq in range(28000,29700,):
      band = '10M'
  if freq in range(50000,54000,):
      band = '6M'
  if freq in range(144000,148000,):
      band = '2M'
  if freq in range(222000,225000,):
      band = '1.25M'
  if freq in range(420000,450000,):
      band = '70CM'
  if freq in range(902000,928000,):
      band = '33CM'
  if freq in range(1240000,1300000,):
      band = '23CM'
  if freq in range(2300000,2310000,):
      band = '13CM'
  if freq in range(2390000,2450000,):
      band = '13CM'
  if freq in range(3300000,3500000,):
      band = '9CM'
  if freq in range(5600000, 5925000,):
      band = '6CM'
  if freq in range(10000000,10500000,):
      band = '3CM'
  if freq in range(24000000,24250000,):
      band = '1.25CM'
  #pre-process the comment line
  comment = str(qsosplit[9:]).replace(',','')
  comment = comment.replace('[','')
  comment = comment.replace(']','')
  comment = comment.replace('\'','')
  #write the data to the out file
  outfile.write('<QSO_DATE:'+str(len(qsosplit[0]))+'>'+qsosplit[0]+' '+
                '<FREQ:'+str(len(str(float(qsosplit[1])/1000)))+'>'+str(float(qsosplit[1])/1000)+' '+
                '<BAND:'+str(len(band))+'>'+band+' '+
                '<MODE:'+str(len(qsosplit[2]))+'>'+qsosplit[2].upper()+' '+
                '<TX_PWR:'+str(len(qsosplit[3]))+'>'+qsosplit[3]+' '+
                '<TIME_ON:'+str(len(qsosplit[4]))+'>'+qsosplit[4]+' '+
                '<CALL:'+str(len(qsosplit[5]))+'>'+qsosplit[5].upper()+' '+
                '<RST_RCVD:'+str(len(qsosplit[6]))+'>'+qsosplit[6]+' '+
                '<RST_SENT:'+str(len(qsosplit[7]))+'>'+qsosplit[7]+' '+
                '<OPERATOR:'+str(len(qsosplit[8]))+'>'+qsosplit[8].upper()+' '+
                '<COMMENT:'+str(len(comment))+'>'+comment.upper()+' '+
                '<EOR>'+"\n")
  qso = infile.readline()
  #
#outfile.write("\n"+'  </RECORDS>')
#outfile.write("\n")
#outfile.write("\n")
#outfile.write('</ADX>')
