#!/usr/bin/python

import os,random,xchat

__module_name__ = "sooneries" 
__module_version__ = "1.0" 
__module_description__ = "Sooneries au hasard :d"

filename= os.path.expanduser("~/.xchat2/soon.txt")
def command_soonerie(word, word_eol, userdata):
	
	file = open(filename,'r')
	file_size = os.stat(filename)[6]
	file.seek((file.tell()+random.randint(0,file_size-1))%file_size)
	file.readline()
	line = file.readline()
	line = line.rstrip()
	xchat.command("say 02.::soonerie::. " +line)
soonerie = command_soonerie
xchat.hook_command("soonerie",    soonerie,	help="quote de soon")
print "06Sooneries module loadaide suksaisfouly"


