#import numpy as np
import pylab as pl
import enum
import random

class Direction(enum.Enum):
    NORTH = enum.auto()
    SOUTH = enum.auto()
    EAST  = enum.auto()
    WEST  = enum.auto()

def direction_from_rand(rand_nr):
    if rand_nr < 0.25:
        return Direction.NORTH
    if rand_nr < 0.5:
        return Direction.SOUTH
    if rand_nr < 0.75:
        return Direction.EAST
    return Direction.WEST

def step_from_direction(direction_in):
    if direction_in == Direction.NORTH:
        return [0,1]
    if direction_in == Direction.SOUTH:
        return [0,-1]
    if direction_in == Direction.EAST:
        return [1, 0]
    return [-1, 0]

def update_position(position_list, step):
    current_position = position_list[-1]
    new_position = [current_position[0] + step[0], current_position[1] + step[1]]
    position_list.append(new_position)
    return position_list


NUMBER_POINTS = 1000
START = [0,0]

positions = [START]
x = [START[0]]
y = [START[1]]

for number in range(NUMBER_POINTS):
    random_number = random.random()
    direction = direction_from_rand(random_number)
    step = step_from_direction(direction)
    positions = update_position(positions, step)
    x.append(positions[-1][0])
    y.append(positions[-1][1])

pl.plot(x,y,'o-')
pl.show()
