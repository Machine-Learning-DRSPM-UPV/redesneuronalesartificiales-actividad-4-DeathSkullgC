from glob import glob as ls
import re
url = ls("./*/*/*/*/")
#print(ls(url[0]+"*"))
#DireccionesdeFicheros = ls(url[2]+"*")
#Fichero = open(DireccionesdeFicheros[120],'r')

for u in url:
	DireccionesdeFicheros = ls(u+"*")
	for f in DireccionesdeFicheros:	
		Fichero = open(f,'r')
		parrafo = Fichero.read()
		Fichero.close()
		parrafo = re.sub('<br />'," ",parrafo)
		parrafo = re.sub('[^A-Za-z\']'," ",parrafo)
		parrafo = re.sub('\s\s'," ",parrafo)
		parrafo = re.sub('\s\s'," ",parrafo)
		parrafo = parrafo.lower()
		parrafo = parrafo.split(" ")
		parrafo = set(parrafo)
		palabrasnoutiles = ['some','need','for','even','they','mens','look','there\'s','the','actors','me','make','there','story','were', 'expect','his','guy','of','it','so','let','spots','own','at','same','parts','want','masturbation','if','makes',' and','be','again','can', 'movie','eat','this','made','seen','movies','its','when','as','which','my','a','quickly','time','business','by','mini','seeing','junk',
		'call' ,'each','poline','spit','how','women','on','spot','kinda','tree','is','he','does','whole','part','am','hour','called','neighborhood',
		'going','still','house','through','road','three','people','dvd','was','i','brother','sister','being','doesn\'t','way','play','then','run',
		'runs','many','off','why','abe','either','characters','feature','william','some','five','one','two','reviews','katt','to','who','lady',
		'i\'m','situation','writers','stereotypical','their','your','him','will','actually','episode','just','tv','series','about','builds','shes',
		'review','made','island','means','girls','think','little','film','psychiatrist','his','second','a','viewing','remembered','family','rural',
		'sleeper','older','having','have','has','watched','noticed','feels','equally','jason','twelve','dialogue','mom','dad','mother','father',
		'common','karl','media','cakes','match','husband','previous','himself','you','we','us','them','our','mine','yours','hers','ours','yours',
		'theirs', 'myself','yourself','himself','herself','itself','ourself','yourselves','themselves','here','beyond','under', 'opposite','also',
		'over there','to the left','in the distance','in particular','furthermore','of curse','but','however','on the other hand','otherwise','unlike','conversely','at the same time','in spite of','later', 'after','before','next','soon','therefore','thus','because','hence','due to','as a result','too','in addition to','clock','achieved','makes','since','daughter','new','lines','away','faces','clash','cocktail','previous','climax', 'rima','veteran','vs','credit','any','american','both','son\'s','together','rate','happen','i\'ve','that\'s','must','with', 'or','harry','john','star','absolutely','all','roles','role','rides','competitor','very', 'around','company','types','also','teen','comes','came','come','only','cover','clips','sex','away','money','names','name','class','normally', 'are','and','girl','boy','edition','altrought','from','these']
		for palabrainutil in palabrasnoutiles:
			if palabrainutil in parrafo:
				parrafo.remove(palabrainutil)
		Dataset = open('datasetpalabras.csv','a')
		for palabras in parrafo:
			Dataset.write(palabras+',')
		Dataset.close()
Dataset = open('datasetpalabras.csv','a')
Dataset.write('Clasificacion\n')
Dataset.close()
print('Llenando de 0 y 1')
Ldata = open('datasetpalabras.csv','r')
palabrasdata = Ldata.read()
Ldata.close()
palabrasdata = palabrasdata.split(',')
binario = open('datasetpalabras.csv','a')
for u in url:
	DireccionesdeFicheros = ls(u+"*")
	for f in DireccionesdeFicheros:	
		Fichero = open(f,'r')
		parrafo = Fichero.read()
		Fichero.close()
		parrafo = re.sub('<br />'," ",parrafo)
		parrafo = re.sub('[^A-Za-z\']'," ",parrafo)
		parrafo = re.sub('\s\s'," ",parrafo)
		parrafo = re.sub('\s\s'," ",parrafo)
		parrafo = parrafo.lower()
		for palabra in parrafo:
			for palabradata in palabrasdata:
				if palabra is palabradata:
					binario.write('1,')
				elif palabradata is 'Clasificacion':
					if re.search('neg',DireccionesdeFicheros):
						binario.write('0,')
					elif re.search('pos',DireccionesdeFicheros):
						binario.write('1,')
				else:
					binario.write('0,')
		binario.write('\n')
binario.close()		
