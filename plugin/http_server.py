##############################################################################
#                         <<< http_server >>>                           
#                                                                            
#                        2011 E2OpenPlugins          
#                                                                            
#  This file is open source software; you can redistribute it and/or modify  
#     it under the terms of the GNU General Public License version 2 as      
#               published by the Free Software Foundation.                   
#                                                                            
##############################################################################

from Components.config import config
from Tools.Directories import fileExists
from twisted.internet import reactor
from twisted.web import server, http, static, resource, error
from ow_contents import get_Info_content, get_Ajax_Tabs


global http_running
http_running = ""

def buildRootTree(session):
	basepath = get_BasePath()
	root = BuildPage(session, basepath + "/www/html")
	root.putChild("js", static.File(basepath + "/www/html/js"))
	root.putChild("css", static.File(basepath + "/www/html/css"))
	root.putChild("ajax", static.File(basepath + "/www/html/ajax"))
	root.putChild("media", static.File("/media"))
	return root

def HttpdStart(session):
	if config.OpenWebif.enabled.value == True:
		global http_running
		port = config.OpenWebif.port.value


		root = buildRootTree(session)
		if config.OpenWebif.auth.value == True:	
			root = AuthResource(session, root)
		site = server.Site(root)
		
		http_running = reactor.listenTCP(port, site)

		print "[OpenWebif] started on %i"% (port)
		
def HttpdStop(session):
	if http_running:
		http_running.stopListening().addCallback(HttpdDoStop, session)

def HttpdDoStop(session):
	print "[OpenWebif] stopped"
	
def HttpdRestart(session):
	if http_running:
		http_running.stopListening().addCallback(HttpdDoRestart, session)

def HttpdDoRestart(ign, session):
	HttpdStart(session)

class AuthResource(resource.Resource):
	def __init__(self, session, root):
		resource.Resource.__init__(self)
		self.resource = root
		

	def render(self, request):
		if self.login(request.getUser(), request.getPassword()) == False:
			request.setHeader('WWW-authenticate', 'Basic realm="%s"' % ("OpenWebif"))
			errpage = error.ErrorPage(http.UNAUTHORIZED,"Unauthorized","401 Authentication required")
			return errpage.render(request)
		else:
			return self.resource.render(request)


	def getChildWithDefault(self, path, request):
		if self.login(request.getUser(), request.getPassword()) == False:
			request.setHeader('WWW-authenticate', 'Basic realm="%s"' % ("OpenWebif"))
			errpage = error.ErrorPage(http.UNAUTHORIZED,"Unauthorized","401 Authentication required")
			return errpage
		else:
			return self.resource.getChildWithDefault(path, request)
		
		
	def login(self, user, passwd):
		from crypt import crypt
		from pwd import getpwnam
		from spwd import getspnam
		cpass = None
		try:
			cpass = getpwnam(user)[1]
		except:
			return False
		if cpass:
			if cpass == 'x' or cpass == '*':
				try:
					cpass = getspnam(user)[1]
				except:
					return False			
			return crypt(passwd, cpass) == cpass
		return False

class BuildPage(resource.Resource):
	def __init__(self, session, path):
		resource.Resource.__init__(self)

		self.session = session
		self.path = path

	def render(self, request):
		basepath = get_BasePath()
		request.setResponseCode(http.OK)
		htmlout = self.loadHtmlSource(basepath + "/www/html/index.html")
        	OpenWebIfMainBody = self.get_Main_body(self.path)
		request.write(htmlout.format(**locals()))
		request.finish()

		return server.NOT_DONE_YET
		
	def getChild(self, path, request):
		path = self.path + "/" + path
		if path[-1] == "/":
			path += "index.html"
		return BuildPage(self.session, path)

	def loadHtmlSource(self, file):
		out = ""
		if fileExists(file):
			f = open(file,'r')
 			out = f.read()
 			f.close()
		return out
		
	def get_Main_body(self, path):
		if path.find('index.html') != -1:
			return get_Ajax_Tabs()
		elif path.find('box_info.html') != -1:
			htmlout = self.loadHtmlSource(self.path)
			owinfo = get_Info_content()
			owif_info_brand = owinfo['brand']
			owif_info_model = owinfo['model']
			owif_info_chipset = owinfo['chipset']
			owif_info_fpver = owinfo['fp_version']
			owif_info_memtot = owinfo['mem1']
			owif_info_memfree = owinfo['mem2']
			owif_info_uptime = owinfo['uptime']
			owif_info_kernel = owinfo['kernelver']
			owif_info_image = owinfo['imagever']
			owif_info_e2 = owinfo['enigmaver']
			owif_info_tuners = owinfo['tuners']
			owif_info_hdd = owinfo['hdd']
			return htmlout.format(**locals())
		else:
			return self.loadHtmlSource(self.path)
		
def get_BasePath():
	return "/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif"


