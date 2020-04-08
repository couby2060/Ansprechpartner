#!/usr/local/bin/python3.7

#pip3 install pyperclip
#pip3 install PTable

#importing the module
import pyperclip
import csv
from prettytable import PrettyTable

def main():
	projektnummer = []
	kunde = []
	projektname = []
	ansprechpartner = []
	#READ CSV File
	with open('/Users/jwilhelm/Desktop/jwi-test/py/Ansprechpartner/currentprojects.csv') as csvDataFile:
		csvReader = csv.reader(csvDataFile, delimiter=';', quotechar='"')
		for row in csvReader:
			#print (row)
			#print(row[0],row[1],row[2],row[3],row[4])
			projektnummer.append(row[0])
			kunde.append(row[1])
			projektname.append(row[2])
			ansprechpartner.append(row[3])

		t = PrettyTable(['ID',projektnummer[0],kunde[0],projektname[0],ansprechpartner[0]])
		
		rowcount = (len(projektname))
		j=1
		while j <= rowcount-1:
			t.add_row([j,projektnummer[j],kunde[j],projektname[j],ansprechpartner[j]])
			j = j+1
		print(t)
		
	#aks for project id
	print('Daten zu welcher Projekt-ID willst du in den Cache bekommen?')
	projectid = int(input())

	#ask for jira vs txt
	print('Sollen die Daten im Text-Format (t) in den Cache oder im Jira-Format (j)?')
	cacheformat = input()
	if cacheformat == 't':
		pyperclip.copy('Kunde: ' + kunde[projectid] + '\n' + 'Projekt: ' + projektnummer[projectid] + ' – ' + projektname[projectid] + '\n' + 'Auftrag von: ' + ansprechpartner[projectid] + '\n\n')
		print ('Done')
	elif cacheformat == 'j':
		pyperclip.copy('Kunde: ' + '*{color:#d04437}' + kunde[projectid] + '{color}*' + '\n' + 'Projekt: ' + '*{color:#d04437}' + projektnummer[projectid] + ' – ' + projektname[projectid] + '{color}*' + '\n' + 'Auftrag von: ' + '*{color:#d04437}' +ansprechpartner[projectid] + '{color}*' + '\n' + '\n' + '----' + '\n\n')
		print ('Done')
	else:
		print ('Bitte gib einen gültigen Wert ein.')
	

if __name__ == "__main__":
	main()