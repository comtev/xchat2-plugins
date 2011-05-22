#!/usr/bin/python
# coding=UTF-8

import os,random,xchat

__module_name__ = "Fortunes de Kaamelott" 
__module_version__ = "1.0" 
__module_description__ = "Citations de Kaamelott"

filename= os.path.expanduser("~/.xchat2/kaamelott.txt")
def command_kaameloterie(word, word_eol, userdata):
	
	file = open(filename,'r')
	file_size = os.stat(filename)[6]
	file.seek((file.tell()+random.randint(0,file_size-1))%file_size)
	file.readline()
	line = file.readline()
	line = line.rstrip()
	xchat.command("say 02.::Kaamelott::. " +line)
kaameloterie = command_kaameloterie
xchat.hook_command("kaameloterie",    kaameloterie,	help="Citations de Kaamelott")
print "Fortunes de Kaamelott correctement chargées !"

