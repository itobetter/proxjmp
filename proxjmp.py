#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urlscraping import *


def prints(funcion):
	if type(funcion) is list:
		for x in funcion:
			print "/|------------------>  %s \n" %x
	else:
		print funcion

def menu():
	while True:
		x = raw_input('\v |>>>  ')

		if x == "shodanhq":
			spider(url).shodanhq_s("r")
		elif x == "google":
			spider(url).google_s("r")
		elif x == "bing":
			spider(url).bing_s("r")
		elif x == "gyffu":
			spider(url).gyffu_s("r")
		elif x == "yahoo":
			spider(url).yahoo_s("r")
		elif x == "myip":
			spider(url).myip("r")
		elif x == "lanctrl":
			spider(url).lanctrl("r")
		elif x == "ip":
			spider(url).rutas_ip()
		elif x == "servidor dns":
			spider(url).local_dns_server()
		elif x == "ip rutas":
			spider(url).ruta_ip()
		elif x == "nombre rutas":
			spider(url).rutas_n()
		elif x == "cambiar dnsserver":
			spider(url).cambiar_dnsserver()
		elif x == "salir":
			break
	
def banner():

	print" \____________________________________________________ "
	print" \|.+?~=~Z...........+.............i..... .    .......|"
	print" \|. Spiderp,.. ...  ,Z.............7,.....    .......|"
	print" \|. :Z: