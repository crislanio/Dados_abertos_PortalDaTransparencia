# -*- coding: UTF-8 -*-
import csv
import pandas as pd

ano ='2016'
listdias = ['31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31' ]
listmes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' ]

# ano ='2017'
# listdias = ['31', '28', '31']#,'30', '31', '30', '31', '31', '30', '31', '30', '31' ]
# listmes = ['01', '02', '03']# , '04', '05', '06', '07', '08', '09', '10', '11', '12' ]

m=0

for d in listdias:
	data = pd.read_csv('/home/lupum/Dados Abertos/dados_servidores/'+ano+'/'+ano+listmes[m]+'_Servidores/'+ano+listmes[m]+d+'_Cadastro.csv', delimiter="\t", encoding="ISO-8859-9")

	print (ano+listmes[m]+d)

	csvTable = data[['UORG_LOTACAO', 'ORG_LOTACAO', 'ORGSUP_LOTACAO']]

	tabelaOrgaoDF = pd.DataFrame(csvTable, columns = ['UORG_LOTACAO', 'ORG_LOTACAO', 'ORGSUP_LOTACAO'])

	tabelaOrgaoDF.to_csv('/home/crislanio.macedo/DADOSABERTOS/Dados Abertos/dados_servidores/'+ano+'/'+ano+listmes[m]+'_Servidores/'+ano+listmes[m]+d+'_ORG.csv')

	
	m+=1


