#Class of the robot

# Contains variables like:
#robotID = Used to identify the robot.
# robotType = Used to identify the type of the robot.
# robotLocation = Used to store the 3D coordinates of the robot in the simulation environment.
# taskAssigned = Used to keep track of the current task assigned to the robot.
# isBusy = Used to ascertain whether the robot is busy completing a task or navigating.
# isCapable = Used to define the tasks that this robot can complete.

class Robot:
    '''Base class to represent the robot object type in the experiment.'''

    def __init__(self, robotID, robotType, robotLocation, isCapable):
        self.robotID = robotID
        self.robotType = robotType
        self.robotLocation = robotLocation
        self.taskAssigned = -1
        self.isBusy = False
        self.isCapable = isCapable

    def assign_task(self,taskID):
        self.taskAssigned = taskID
        self.isBusy = True

    def get_robot_id(self):
        return self.robotID

    def get_robot_type(self):
        return self.robotType

    def get_robot_location(self):
        return self.robotLocation

    def get_is_capable(self):
        return self.isCapable

    def get_robot_location(self):
        return self.robotLocation

    def get_robot_status(self):
        return self.isBusy

    def set_robot_location(self,newLocation):
        self.robotLocation = newLocation

    def set_robot_task(self,newTask):
        self.taskAssigned = newTask

    def set_robot_status(self,newStatus):
        self.isBusy = newStatus

    pass
