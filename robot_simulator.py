# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

def change_direction(direction,turn):
        directions = [SOUTH,WEST,NORTH,EAST]
        start_index = directions.index(direction)
        if turn == "L":
                end_index = start_index - 1   
                if end_index < 0:
                        end_index = len(directions) - 1      
        else:
                end_index = start_index + 1
                if end_index >= len(directions):
                        end_index = 0
        return directions[end_index]

def advance_move(direction, x_pos, y_pos):
        if direction == EAST:
            x_pos += 1
        elif direction == WEST:
            x_pos -= 1
        elif direction == NORTH:
            y_pos += 1
        elif direction == SOUTH:
            y_pos -= 1
        coordinates = (x_pos, y_pos)
        return coordinates

class Robot:
    def __init__(self, direction, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)


    def move(self, action):
        for item in action:
            if item == "R" or item == "L":
                self.direction = change_direction(self.direction, item)
            else:
                x, y = self.coordinates
                self.coordinates = advance_move(self.direction, x, y)
        return self.direction, self.coordinates

robot = Robot(NORTH, 0, 0)
print(robot.move("RAALAL"))