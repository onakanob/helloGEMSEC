from batchExample.scripts import say
import batchExample.scripts as myScripts
f = open('./batchExample/1.txt')
say(f.read())
f.close

f = open('./batchExample/2.txt')
myScripts.say(f.read())
f.close