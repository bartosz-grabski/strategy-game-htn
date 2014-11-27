strategy-game-htn
=================

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
''' python htn.py '''

