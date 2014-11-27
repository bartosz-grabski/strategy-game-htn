#from pyhop import *
import pyhop
import methods

state1 = pyhop.State('state1')
state1.gold = 100
state1.peons = 1
state1.houses = 0
state1.free_places = 2
state1.wood = 20

#pyhop.print_methods()
#pyhop.print_operators()

def build_town(state):
	print state
	return [('build_barracks_task',),('build_watchtower_task',),('build_watchtower_task',),('build_barracks_task',),('build_barracks_task',)]

pyhop.declare_methods('build_town',build_town)

pyhop.pyhop(state1,[('build_town',)],verbose=2)