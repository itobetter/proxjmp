#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re #libreria encargada de las regulares expreciones (regex)
from socket import socket
from sys import argv
import commands
try:
	import requests # "urllib for human." libreria que permite conectarse con la url
	from bs4 import BeautifulSoup # libreria que permite la manupulacion de html
	from bs4 import SoupStrainer
	from scapy.all import *
	from asyncdns import AsyncResolver

except ImportError:
	from subprocess import check_output
	check_output('pip install requests', shell=True)
	
	check_output('pip install bs4', shell=True)
	
	check_output('pip install scapy', shell=True)
	
	check_output('pip install asyncdns', shell=True)
	
	try:
		from asyncdns import AsyncResolver
		import requests
		from bs4 import BeautifulSoup
		from bs4 import SoupStrainer
		from scapy.all import *
	except ImportError:
		print "problemas para conectar pip a la red revise su firewall"

class spider():
	"""manupulacion de las url obtenidas por los spider"""
	def __init__(self, url):

		if re.match(r'http://www.(?:\w+\.)*(\w+\.com)', url) or re.match(r'https://www.(?:\w+\.)*(\w+\.com)', url): 
		 	self.url  = url	# regex que nos garantiza que el link este bien compuesto y la retorna
		else:
	 		print "la url no esta completa, 'http://www.ejemplo.com' o 'https://www.ejemplo.com'"

		if re.match(r'https://www.(?:\w+\.)*(\w+\.com/)', url):
			self.url1 = url[8:-1]	# regex que nos garantiza que el link este bien compuesto y la retorna
			self.url2 = url[11:-1]
		elif re.match(r'http://www.(?:\w+\.)*(\w+\.com/)', url):
			self.url1 = url[7:-1]
			self.url2 = url[10:-1]
		elif re.match(r'https://www.(?:\w+\.)*(\w+\.com)', url):
			self.url1 = url[8:]
			self.url2 = url[11:]
		elif re.match(r'http://www.(?:\w+\.)*(\w+\.com)', url):
			self.url1 = url[7:]
			self.url2 = url[10:]
		

	def conectar(self):

		r = requests.get(self.url) #buscando la pagina por metodo get
		if r.status_code == requests.codes.ok:
			e = "200, pagina disponible, coneccion directa"
		else:
			e = "404 Not found, determinar falla...?"
		return e

		def google_s (self,selector):
			
			try:
				google = requests.get("https://www.google.co.ve/search?q="+ url +"&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=sb&gfe_rd=cr&ei=yPYRU4TTFs-atweSkoGIAg#channel=sb&newwindow=1&q=site:"+ url +"&rls=org.mozilla:en-US:official&safe=off")
				l = []
				G = BeautifulSoup(google.text, parse_only= SoupStrainer(id="center_col"))
				for i in G.select('a[href*='+ self.url2+']'):	
					a = (i.get('href'))
					a = a.replace('/url?q=','')
					l.append(a)

				if selector == "c":
					e = " google detecto %s resultados relacionado con la pagina" %len(l)
				if selector == "r":
					e = l
				return e

			except Exception:
				return ("error al conectarse a google")	
		
	def bing_s (self,selector):
		
		try:
			l = []
			bing = requests.get("http://www.bing.com/search?q="+ url +"&qs=n&form=QBRE&filt=all&pq=" + url + "&sc=0-0&sp=-1&sk=")
			B = BeautifulSoup(bing.text, parse_only= SoupStrainer(id="results"))

			for i in B.select('a[href*='+ self.url2+']'):	
				l.append (i.get('href'))

			if selector == "c":
				e = "Bing detecto %s resultados relacionado con la pagina" %len(l)
			if selector == "r":
				e = l
			return e
		except Exception, e:
			print "no se puede conectarr con bing"

	def gyffu_s (self, selector):
		
		try:
			gyffu = requests.get("http://www.gyffu.com/result.php?hidden=&buscador=site%3A" + self.url + "&submit=Buscar")
			l = []
			G = BeautifulSoup(gyffu.text, parse_only= SoupStrainer(id="resultados"))
			for i in G.select('a[href*='+ self.url2+']'):
				l.append (i.get('href'))

			if selector == "c":
				e = "gyffu detecto %s resultados relacionado con la pagina" %len(l)
			if selector == "r":
				e = l
			return e

		except Exception:
			print ("error al conectarse a la gyffu")
	
	def yahoo_s (self,selector):
		
		try:
			yahoo = requests.get("http://es.search.yahoo.com/search;_ylt=A0LEV2vi_xFTNj4AasuT.Qt.;_ylc=X1MDMjExNDcxNDAwMwRfcgMyBGJjawM2bG9qNzJwOWYzOWEwJTI2YiUzRDMlMjZzJTNEM24EZnIDeWZwLXQtOTA3BGdwcmlkA29vT0ZNbF8wU19XVmRlUmVrUnNsNUEEbXRlc3RpZANudWxsBG5fcnNsdAMxMARuX3N1Z2cDMARvcmlnaW4DZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMyOARxdWVyeQNodHRwOi8vd3d3LmFndWFjYXRldmVyZGUuY29tBHRfc3RtcAMxMzkzNjg4NTYzOTY4BHZ0ZXN0aWQDbnVsbA--?gprid=ooOFMl_0S_WVdeRekRsl5A&pvid=iIzfRjk4LjFq4mcWUvGlQAWfMTkwLlMR_.L_q3CI&p=" + self.url + "&fr2=sb-top&fr=yfp-t-907&rd=r1")
			Y = BeautifulSoup(yahoo.text, parse_only= SoupStrainer(id="web"))
			l=[]
			for i in Y.select('a[href*='+ self.url2+']'):
				l.append (i.get('href'))

			if selector == "c":
				e = "Yahoo detecto %s resultados relacionado con la pagina" %len(l)
			if selector == "r":
				e = l
			return e
		except Exception:
			return ("error al conectarse a la yahoo")			
		
	def myip (self, selector):
		try:
			myip= requests.get("http://myip.es/" + self.url1)
			M = BeautifulSoup(myip.text)
			l = []
			for i in M.find_all('table'):
				try:
					l.append(i.get_text().encode('UTF-8'))
				except Exception, e:
					print e

			if selector == "c" and len(l) == 1:
				e = "Myipwhois detecto resultados whois relacionado con la pagina" 
			if selector == "r":
				e = l
			return e

		except Exception:
			print "error al conectarse a myip.es"
				

	def lanctrl (sleft, selector):
		try:

			l = []
			lanctrl = requests.get("http://whois.lanctrl.com/index.php?query="+ selft.url1 + "%2F&Submit=+Whois+" )
			S = BeautifulSoup(lanctrl.text)
			for i in S.find_all('pre'):
				l.append( i.get_text())
				
			if selector == "c" and len(l) == 1:
				e = "lanctrl detecto resultados whois relacionado con la pagina" 
			if selector == "r":
				e = l
			return e
			
		except Exception,e:
			print e
			print "es posbile que posea errores para conectarse a al conectarse a lanctrl"

	def shodanhq_s (self, selector):
		
		try:
			shodanhq = requests.get("http://www.shodanhq.com/search?q=http%3A%2F%2F"+ self.url1 )
			S = BeautifulSoup(shodanhq.text)
			l = []
			for i in S.find_all('p'):
				l.append( i.get_text())

			if selector == "c":
				e = "shodan detecto %s resultados relacionado con la pagina" %len(l)
			if selector == "r":
				e = l
			return e

		except Exception:
			print "error al conectarse a shodanhq"

	def existe(self):
		if self.conectar() == "200, pagina disponible, coneccion directa" and self.url1 in self.gyffu_s("r")[1] :
			e = 'no existe blockeo de un proxy para %s' %self.url1
		
		if self.conectar() == "404 Not found, determinar falla...?" and self.url1 in self.gyffu_s("r")[1] :
			e = 'es posible que exista blockeo de un proxy para %s' %self.url1

		if self.conectar() == "404 Not found, determinar falla...?" and not self.url1 in self.gyffu_s("r")[1] :
			e = 'es posible que %s no exista en la red' %self.url1
		
		return e

	def rutas_ip(self):
		"""hace una traceroute al servidor dns 4.2.2.1 
		determina si existe hihacking dns"""

		conf.verb=1
		interactive = False
		ans,unans=traceroute(url1)
		l = []
		for i in ans:
			i = str(i).split('|')[4]
			i = re.search(r'src=\w+.\w+.\w+.\w+', i).group()
			i = i[4:]
			if i in self.l:
				pass
			else:	
				l.append(i)
		return l
		

	def rutas_n(self,x):
		x = self.rutas_ip(self.url1)
		for i in x:
			e = "ip \t url \t hostname  \v %s %s %s"%(socket.gethostbyaddr(i)[2], i, socket.gethostbyaddr(i)[0],)
		return e

	def local_dns_server(self,e):
		l = commands.getoutput('nslookup'+ self.url1)
		if e is "c":
			e = re.search("Server:\t\t\w+.\w+.\w+.\w+\nAddress:\t\w+.\w+.\w+.\w+#53",l).group()
		else:
			e = l 
		retunr e 

	def comprobar_p():
		z = re.search(r'IP:\w+.\w+.\w+.\w+', str(self.myipwhois("r"))).group()
		z = str(z).lstrip("IP:")
		if z == socket.gethostbyname(self.url1)
			e = "no existe ninguna intervercion con el dominio solicitado"
		else:
			e = "las resultados dns onlines y locales no coinciden \n o existe un servidor espejo en su red \n te sujiero cambiar tu dns"
		return e