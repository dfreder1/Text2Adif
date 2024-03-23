'''
   See README.md
'''
#
# Open the input file
infile = open("textinput.txt", mode = "r")
# Create the ouptput file
outfile = open("adiforimport.adi", mode = "w")
#
# Heading - Abandoned the ADX version
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
  freq =float(qsosplit[1])
  print(freq)
  if freq <= 138:
      band = '2200M'
  elif freq <= 479:
      band = '600M'
  elif freq <= 2000:
      band = '160M'
  elif freq <= 4000:
      band = '80M'
  elif freq <= 5410:
      band = '60M'
  elif freq <= 7300:
      band = '40M'
  elif freq <= 10150:
      band = '30M'
  elif freq <= 14350:
      band = '20M'
  elif freq <= 18168:
      band = '17M'
  elif freq <= 21450:
      band = '15M'
  elif freq <= 24990:
      band = '12M'
  elif freq <= 29700:
      band = '10M'
  elif freq <= 54000:
      band = '6M'
  elif freq <= 148000:
      band = '2M'
  elif freq <= 225000:
      band = '1.25M'
  elif freq <= 450000:
      band = '70CM'
  elif freq <= 928000:
      band = '33CM'
  elif freq <= 1300000:
      band = '23CM'
  elif freq <= 2310000:
      band = '13CM'
  elif freq <= 2450000:
      band = '13CM'
  elif freq <= 3500000:
      band = '9CM'
  elif freq <= 5925000: 
      band = '6CM'
  elif freq <= 10500000: 
      band = '3CM'
  else: 
      #freq <= 24250000
      band = '1.25CM'
  print(band)
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
