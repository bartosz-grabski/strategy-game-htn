import pyhop

BARRACKS_COST_GOLD = 100
BARRACKS_COST_WOOD = 50
HOUSE_COST_GOLD = 10
PEON_COST_GOLD = 50
WATCHTOWER_COST_GOLD = 50
WATCHTOWER_COST_WOOD = 20

GATHER_GOLD = 200
GATHER_WOOD = 100



def build_town(state):
	print state
	return [('build_barracks_task',),('build_watchtower_task',),('build_watchtower_task',),('build_barracks_task',)]

pyhop.declare_methods('build_town',build_town)

def build_barracks_task_a(state):
	if state.gold >= BARRACKS_COST_GOLD and state.wood >= BARRACKS_COST_WOOD and state.peons > 0:
		return [('build_barracks',)]
	return False

def build_barracks_task_b(state):
	if state.peons <= 0:
		return [('train_peon_task',),('build_barracks_task',)]
	else:
		return False

def build_barracks_task_c(state):
	if state.gold < BARRACKS_COST_GOLD:
		return [('gather_gold_task',),('build_barracks_task',)]
	else:
		return False

def build_barracks_task_d(state):
	if state.wood < BARRACKS_COST_WOOD:
		return [('gather_wood_task',),('build_barracks_task',)]
	return False


pyhop.declare_methods('build_barracks_task',build_barracks_task_a,build_barracks_task_b,build_barracks_task_c,build_barracks_task_d)

def build_house_task_a(state):
	if state.gold >= HOUSE_COST_GOLD:
		return [('build_house',)]
	else:
		return False

def build_house_task_b(state):
	if state.gold < HOUSE_COST_GOLD:
		return [('gather_gold_task',),('build_house_task',)]
	else:
		return False

pyhop.declare_methods('build_house_task',build_house_task_a,build_house_task_b)

def build_watchtower_task_a(state):
	if state.gold >= WATCHTOWER_COST_GOLD and state.wood >= WATCHTOWER_COST_WOOD and state.peons > 0:
		return [('build_watchtower',)]
	else:
		return False

def build_watchtower_task_b(state):
	if state.peons <= 0:
		return [('train_peon_task',),('build_watchtower_task',)]
	else:
		return False

def build_watchtower_task_c(state):
	if state.gold < WATCHTOWER_COST_GOLD:
		return [('gather_gold_task',),('build_watchtower_task',)]
	else:
		return False

def build_watchtower_task_d(state):
	if state.wood < WATCHTOWER_COST_WOOD:
		return [('gather_wood_task',),('build_watchtower_task',)]
	else:
		return False

pyhop.declare_methods('build_watchtower_task',build_watchtower_task_a,build_watchtower_task_b,build_watchtower_task_c,build_watchtower_task_d)

def train_peon_task_a(state):
	if state.gold >= PEON_COST_GOLD and state.free_places > 0:
			return [('train_peon',)]
	else:
		return False

def train_peon_task_b(state):
	if state.free_places == 0:
		return [('build_house_task',),('train_peon_task',)]
	else:
		return False

pyhop.declare_methods('train_peon_task',train_peon_task_a,train_peon_task_b)

def gather_gold_task_a(state):
	if state.peons > 0:
		return [('gather_gold',)]
	else:
		return False

def gather_gold_task_b(state):
	if state.gold >= PEON_COST_GOLD:
		return [('train_peon_task',),('gather_gold_task',)]
	else:
		return False

pyhop.declare_methods('gather_gold_task',gather_gold_task_a, gather_gold_task_b)

def gather_wood_task_a(state):
	if (state.peons > 0):
		return [('gather_wood',)]
	else:
		return False

def gather_wood_task_b(state):
	if (state.gold >= PEON_COST_GOLD):
		return [('train_peon_task',),('gather_wood_task',)]
	else:
		return False

def gather_wood_task_c(state):
	if state.gold < PEON_COST_GOLD:
		return [('gather_gold_task',),('gather_wood_task',)]
	else:
		return False



pyhop.declare_methods('gather_wood_task',gather_wood_task_a,gather_wood_task_b,gather_wood_task_c)

# operators

def build_barracks(state):
	if state.gold >= BARRACKS_COST_GOLD and state.wood >= BARRACKS_COST_WOOD and state.peons > 0:
		state.gold = state.gold - BARRACKS_COST_GOLD
		state.peons = state.peons - 1
		state.wood = state.wood - BARRACKS_COST_WOOD
		return state
	return False

def gather_gold(state):
	if state.peons > 0:
		state.gold = state.gold + GATHER_GOLD
		return state
	else:
		return False

def gather_wood(state):
	if state.peons > 0:
		state.wood = state.wood + GATHER_WOOD
		return state
	else:
		return False

def train_peon(state):
	if state.gold >= PEON_COST_GOLD and state.free_places > 0:
		state.gold = state.gold - PEON_COST_GOLD
		state.free_places = state.free_places - 1
		state.peons = state.peons + 1
		return state
	return False

def build_house(state):
	if state.gold >= HOUSE_COST_GOLD:
		state.gold = state.gold - HOUSE_COST_GOLD
		state.free_places = state.free_places + 5
		state.houses = state.houses + 1
		return state
	return False

def build_watchtower(state):
	if state.gold >= WATCHTOWER_COST_GOLD and state.wood >= WATCHTOWER_COST_WOOD and state.peons > 0:
		state.gold = state.gold - WATCHTOWER_COST_GOLD
		state.peons = state.peons - 1
		state.wood = state.wood - WATCHTOWER_COST_WOOD
		return state
	return False

pyhop.declare_operators(build_barracks,gather_gold,gather_wood,train_peon,build_house,build_watchtower)
