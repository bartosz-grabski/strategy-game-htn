## Simple Strategy Game Planning - base on HTN planning ##

This project was created to demonstrate a simple example of using HTN planning. The planner implementation used is Pyhop

https://bitbucket.org/dananau/pyhop

Our goal is to build a small town. Number of buildings is defined by us

## Domain ##

There are 2 types of resources:
* gold
* wood

There are 3 types of buildings:
* barracks
* watchtower
* house

There are workers (peons), who require resources and free spaces in houses. If there are no free places then 
a house must be built

Each building cost along with workers are defined in methods.py file. You can manipulate it to see what will be 
the output for different parameters.

The initial state (peons, gold, wood, free places) is defined in htn.py file

To run the algorithm enter
```python
python htn.py
```

## Example methods and operators ##

To see all methods and operators see file methods.py

Example code explained.

```python
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

def build_house(state):
	if state.gold >= HOUSE_COST_GOLD:
		state.gold = state.gold - HOUSE_COST_GOLD
		state.free_places = state.free_places + 5
		state.houses = state.houses + 1
		return state
	return False
```

The above code declares a complex task 'build_house_task'. If preconditions are met then 'build_house' action(operator) is called. Otherwise call another complex task 'gather_gold_task' and after that try to return to this task ('build_house_task')

I maintained a naming convention where complex tasks had the _task suffix, while operators hadn't.

## Example output ##

Town should hava a barracks and a watchtower
