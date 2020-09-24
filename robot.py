import math
import random

import settings
from geometry_utils import position, pose

class robot:
	def __init__(self, position, orientation):
		self.pose = pose(position, orientation)
		self.distance = 0
		self.visited = []
		self.visited.append(self.pose.position.toTuple())
		self.last_bisection = None
		self.previous_pose = self.pose

	'''
	This method prints the pose and current distance of the robot
	'''
	def printPoseAndDistance(self):
		print(self.pose.print(log=False) +" "+ str(round(self.distance)))

	'''
	This method returns a dictionary for each cardinal orientation (north 'N', ...)
	For example:
	If the north and south positions are blocked, the dict will look like this:
	{'N': -1, 'NE': 0, 'E': 0, 'SE': 0, 'S': -1, 'SW': 0, 'W': 0, 'NW': 0}
	'''
	def checkAround(self):
		around = [0, 0, 0, 0, 0, 0, 0, 0]
		check = position((0,0))
		for i in range(8):
			check.x = self.pose.position.x + settings.x_sgn[i] * settings.resolution
			check.y = self.pose.position.y + settings.y_sgn[i] * settings.resolution
			check2 = check.toTuple()
			if check2 not in settings.blocked and check2 not in settings.borders:
				around[i] = 0
			else:
				around[i] = -1

		orientation = dict(zip(settings.direction,around))
		return orientation

	'''
	############################
	THIS IS THE METHOD TO MODIFY
	############################
	'''
	def move(self, goal):


		# Update poses, distances, visited and path
		self.previous_pose = self.pose.__copy__() # copies current pose to previous
		self.pose.position.x = 0 # <- update 
		self.pose.position.y = 0 # <- update
		self.pose.orientation = 'N' # <- update
		self.distance = self.distance # <- update with settings.dist2robot[??]
		self.visited.append(self.pose.position.toTuple())
		settings.path.append(self.pose.__copy__())
