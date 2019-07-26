import socket, string, time, msvcrt, math, base64, codecs

class IRC:
	servidor	= ''
	puerto		= 0
	canal		= ''
	bot			= ''
	nick		= ''
	usuario		= ''
	gancho		= ''

	def __init__ (self, servidor, puerto, canal, bot, nick, usuario):
		print ("""
		 ▄████▄   ██▓ ███▄   ██  ██▓  ██████  ▄▄▄       ██▀███   ▄▄▄▄    ▒█████   ██▀███   ██▓  ██████ 
		▒██▀ ▀█  ▓██▒ ██ ▀█  ██ ▓██▒▒██    ▒ ▒████▄    ▓██ ▒ ██▒▓█████▄ ▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██    ▒ 
		▒▓█    ▄ ▒██▒▓██  ▀▄ ██▒▒██▒░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒ ▄██▒██░  ██▒▓██ ░▄█ ▒▒██▒░ ▓██▄   
		▒▓▓▄ ▄██▒░██░▓██▒  █ ██▒░██░  ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  ▒██░█▀  ▒██   ██░▒██▀▀█▄  ░██░  ▒   ██▒
		▒ ▓███▀ ░░██░▒██░   ███░░██░▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒░▓█  ▀█▓░ ████▓▒░░██▓ ▒██▒░██░▒██████▒▒
		░ ░▒ ▒  ░░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░
SCERIS ---
""")
		self.servidor = servidor
		self.puerto = puerto
		self.canal = canal
		self.bot = bot
		self.nick = nick
		self.usuario = usuario
		print ('servidor: '+str(self.servidor))
		print ('puerto:   '+str(self.puerto))
		print ('canal:    '+str(self.canal))
		print ('bot:      '+str(self.bot))
		print ('nick:     '+str(self.nick))
		print ('usuario:  '+str(self.usuario))

	def conectar (self):
		print ('\n ### Conectando...')
		self.gancho = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print (self.gancho)
		print ('### Socket creado. \n')
		self.gancho.connect((self.servidor, int(self.puerto)))
		print (self.gancho)
		print ('### Conectado al servidor. \n')
		self.gancho.send(b"USER" + b" " + self.nick + b" " + self.nick + b" " + self.nick + b" :" + self.nick + b"\r\n")
		self.gancho.send(b"NICK" + b" " + self.nick + b"\n")
		print ('### Registro enviado \n\n')
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		time.sleep(3)
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		time.sleep(3)
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		time.sleep(3)
		print ("conexion =================================================")
		self.gancho.send(b"JOIN" + b" " + self.canal + b"\n")
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")

	def reto1(self):
		print ("canal join =================================================")
		print (b'PRIVMSG' + b" " + self.bot + b" " + b':!ep1 \r\n' )
		self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" " + b':!ep1 \r\n' )
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		print ('Verificar Verificar')
		resultado = 0
		if b"PRIVMSG" in saco:
			print ('principal', saco)
			saco = saco.split()
			print (saco)
			tres = (saco[3]).decode()
			tres = tres[1:]
			cuatro = (saco[4]).decode()
			cinco = (saco[5]).decode()
			tres = int(tres)
			cinco = int(cinco)
			print (tres)
			print (cinco)
			resultado = math.sqrt(tres) * cinco
			resultado = '%.2f' %resultado
			resultado = resultado.encode()
		print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		print (resultado)
		print ('Previo send')
		print (b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep1 -rep " + resultado + b" " + b'\r\n' )
		self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep1 -rep " + resultado + b" " + b'\r\n' )
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		time.sleep(3)
		print ('FINALIZO RETO 1')
	
	def reto2(self):
		print ("canal join =================================================")
		print (b'PRIVMSG' + b" " + self.bot + b" " + b':!ep2 \r\n' )
		self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" " + b':!ep2 \r\n' )
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		resultado = 0
		if b"PRIVMSG" in saco:
			print ('principal', saco)
			saco = saco.split()
			print (saco)
			tres = (saco[3]).decode()
			print (tres)
			tres = base64.b64decode(tres)
			print (tres)
			print (type(tres))
			resultado = tres
			print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print (resultado)
			print ('Previo send')
			print (b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep2 -rep " + resultado + b" " + b'\r\n' )
			self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep2 -rep " + resultado + b" " + b'\r\n' )
			saco = self.gancho.recv(4096)
			print (str(saco) + "\n")
		time.sleep(3)
		print ('FINALIZO RETO 2')

	def reto3(self):
		print ("canal join =================================================")
		print (b'PRIVMSG' + b" " + self.bot + b" " + b':!ep3 \r\n' )
		self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" " + b':!ep3 \r\n' )
		saco = self.gancho.recv(4096)
		print (str(saco) + "\n")
		resultado = 0
		if b"PRIVMSG" in saco:
			print ('principal', saco)
			saco = saco.split()
			print (saco)
			tres = (saco[3]).decode()
			print (tres)
			tres = tres[1:]
			tres = codecs.encode(tres, 'rot_13')
			print (tres)
			print (type(tres))
			resultado = tres
			resultado = resultado.encode()
			print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print (resultado)
			print ('Previo send')
			print (b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep3 -rep " + resultado + b" " + b'\r\n' )
			self.gancho.send(b'PRIVMSG' + b" " + self.bot + b" :" + b"!ep3 -rep " + resultado + b" " + b'\r\n' )
			saco = self.gancho.recv(4096)
			print (str(saco) + "\n")
		time.sleep(3)
		print ('FINALIZO RETO 3')

irc = IRC(	"irc.root-me.org",
			"6667",
			b"#root-me_challenge",
			b"candy",
			b"CinisArboris",
			b"CinisArboris")

irc.conectar()
#irc.reto1()
#irc.reto2()
irc.reto3()