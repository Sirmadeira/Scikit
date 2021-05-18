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
	df= pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
	# Definindo coluinas da dataframe
	# Rode o pritnt para entender a lista de diretorios
	#print(stock_list)
	for each_dir in stock_list[1:]:
		each_file = os.listdir(each_dir)
		ticker=each_dir.split("\\")[1]
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
				source= open(full_file_path,'r').read()
				# Tendo em consideracao que isso e parse em file statica nao a necessidade por url etc,
				#print(source)
				try:
					value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
					df = df.append({'Date':date_stamp,'Unix':unix_time,'Ticker':ticker,'DE Ratio':value,}, ignore_index = True)
					# Toda vez que voce adiciona algo a um dicionario voce preciso ignorar o index
				except Exception as e:
					value = float('nan')
			save=gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
			# isso daki retira os dados inutei da pasta
			print(save)
			df.to_csv(save)
			#Issoprinta os csv
				# Try except para evitar codigos ruins ou fontes erradas
				#Selecionando a parte especifica do source
				#print(ticker+":", value) 
Key_Stats()