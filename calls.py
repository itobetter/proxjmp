#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
from bs4 import BeautifulSoup, SoupStrainer
import requests, re


def proxy4free (selector):
		
	try:
		proxy4free = requests.get("http://www.proxy4free.com/list/webproxy1.html")
		l = []
		P = BeautifulSoup(proxy4free.text, parse_only= SoupStrainer('tbody'))
		for i in P.select('a'):	
			a = (i.get('href'))
			if re.search('^http:', a) or re.search('^https', a): l.append(a)
			else: pass
		if selector == "c":
			e = " proxy4free detecto %s proxys" %len(l)
		if selector == "r":
			e = l
			
		return e
	except Exception, e:
		return ("error al conectarse a proxy4free")	


def p (sentencias):
	sentencias = sentencias.split(" ")
	a= []
	b = []
	x = 0
	for i in sentencias:
		if i != "|":
			a.append(i)
		elif i == "|":
			x = sentencias.index(i)
			for i in xrange(x +1,len(sentencias)):
				b.append(sentencias[i])
			break
	try:
		
		p1 = Popen(a,  stdout=PIPE, stderr=PIPE).communicate()
		if len(b) == 0:
			return p1.stdout.read()
			p1.stdout.close()
		else:
			p2 = Popen(b,  stdin=p1.stdout, stdout=PIPE, stderr=PIPE).communicate()
			return p2.stdout.read()
			p1.stdout.close()
			p2.stdout.close()
		
	except Exception, e:
		return e
	
def app(e):	
	distro = re.search("\w+", p("cat /etc/issue")).group()
		
	if e == "opennic":
		l = []
		try:
			opennic = requests.get("http://wiki.opennicproject.org/ClosestT2Servers")
			o = BeautifulSoup(opennic.text, parse_only=SoupStrainer('div',{'id':'content'}))
			o = str(o).split("<br/>")
			
			for i in o:
				try:
					i = re.search("^\n\d+\.\d+\.\d+\.\d+",i)
					if i:
						l.append (str(i.group())[1:])
					else: pass
				except Exception: pass
			
		except Exception: e = "no se pudo establecer coneccion con opennic"
		dnsserver = open("/etc/resolv.conf", "w")
		dnsserver.write("# Generated by proxjmp\nnameserver "+ l[0]+"\nnameserver "+ l[1])

	if e == "dnscrypt": pass
	if e == "proxychains": pass
	if e == "openvpn": pass
	if e == "tor": pass
"""check_call("sudo pacman -Sy dnscrypt-proxy", shell=True)
"""