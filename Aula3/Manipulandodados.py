# Vale lembrar que a coisa mais dificil de data science e angariar os dados,
#Tendo em consideracao que esse processo e muito comun, mesmo que nao na ivg.
#Vamos aprender a parcelar a data de paginas html, do yahoo finance.
import pandas as pd
import os
import time
from datetime import datetime

#Path para sua database
path= 'C:/Users/FranciscoFroes/Documents/GitHub/Scikit/Aula2/intraQuarter'

# isso daki esta tentando angariar uma parte especifica das tabelas
def Key_Stats(gather="Total Debt/Equity (mrq)"):
	# Referencia ao stats  path
	statspath= path +'/_KeyStats'
	# Basicamente so pega o nome referenciado na lista  de files
	stock_list  = [x[0] for x in os.walk(statspath)]
	# Rode o pritnt para entender a lista de diretorios
	#print(stock_list)
	for each_dir in stock_list[1:]:
		each_file = os.listdir(each_dir)
		# Isso daki esta listando todos os diretorios da primeira diretoric dentro de statspath, sendo nesse caso o diretorio a de key stats
		#print(each_file)
		#time.sleep(15)
		if len(each_file) >0 :
			for file in each_file:
				date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html'	)
				#Isso daki esta retirando cada file que tem pelo menos o length acima de 0
				unix_time =time.mktime(date_stamp.timetuple())
				#print(date_stamp, unix_time)
				full_file_path= each_dir+'/'+file
				# Path completo para a file
				source= open(full_file_path)
				# Tendo em consideracao que isso e parse em file statica nao a necessidade por url etc,
				#print(source)
				value = source.split(gather)
				time.sleep(15)
Key_Stats()