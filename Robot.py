#Class of the robot

# Contains variables like:
#robotID = Used to identify the robot.
#\item robotType = Used to identify the type of the robot.
#\item robotLocation = Used to store the 3D coordinates of the robot in the simulation environment.
# #\item taskAssigned = Used to keep track of the current task assigned to the robot.
#\item isBusy = Used to ascertain whether the robot is busy completing a task or navigating.
#\item isCapable = Used to define the tasks that this robot can complete.

class Robot:
    '''Base class to represent the robot object type in the experiment.'''

    def __init__(self, robotID, robotType, robotLocation, isCapable):
        self.robotID = robotID
        self.robotType = robotType
        self.robotLocation = robotLocation
        self.taskAssigned = 0
        self.isBusy = False
        self.isCapable = isCapable

    def assign_task(self,task):
        self.taskAssigned = task
        self.isBusy = True

    def set_robot_location(self,newLocation):
        self.robotLocation = newLocation

    pass
