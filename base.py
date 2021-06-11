# Base simulation code

# our scenario assumes that the tasks are being found by external agents. These tasks pop-up in the taskQueue

# the following pseudo code represents a allocation mechanism

# while (taskQueue has some tasks)
# start loop

# check to see if the tasks in the queue can be accomplished by the current robots available 
# if a task is not able to be handled by the vacant robots check if there are any busy robots capable of handling this task
# if there are robots capable compare the utility values of the currently assigned task to the new task. 
# if the new task is of a significant higher priority such as a rescue operation, rellocate the robot this new task and add the old task back in the queue

# calculate the distances of all the robots to the tasks in the task queue
# if the number of robots and tasks is 5 each, we will get 5 x 5 distance combinations
# the distance is the 3d euclidean distance of the task and the robot 

# calculate the visibility of all the robots to the tasks 
# visibility is the inverse of the distance
# if a task is more visible, robots will be attracted more

# calculate the relative quality of the tasks 
# this is done to make sure that the sum of all the relative qualities is 1
# to find the relative quality of any task, we take the scalar quality and divide it by the summation of all the other tasks scalar quality

# calculate the probability of allocation for each robot and task set 
# this is done by taking the multiple of the tasks relative quality to the tasks visibility for that robot and dividing the result to the sum of all the other possible combinations
# Again the sum of the probabilities will be equal to 1. 

# depending on the probability values, the tasks are assigned to the best possible robot
# the robot also has to be capable of performing the task
# if the robot has the highest score but it isn`t capable, the task is assigned to the next capable robot
# after assignment of a task, the robot is marked as occupied and will show up as unavailable in the search queue until it finishes the task


# end loop  

from robot import robot
from Task import Task
from Coordinate import Coordinate
import math

robot_list = []
task_list = []

def create_robots(set):

    TYPE_GROUND = "ground_robot"
    TYPE_AERIAL = "aerial_robot"
    BASE_LOCATION_X = 100
    BASE_LOCATION_Y = 100
    BASE_LOCATION_Z = 0
    TASK_LIST_GROUND = ["ground_fire_extinguish", "ground_rescue"]
    TASK_LIST_AERIAL = ["aerial_fire_extinguish", "aerial_rescue"] 
    SET_ONE_ID = [1,2,3,4,5]
    SET_TWO_ID = [1,2,3,4,5,6,7,8,9,10]
    BASE_COORDINATES = Coordinate(BASE_LOCATION_X, BASE_LOCATION_Y, BASE_LOCATION_Z)

    # set-1, 1 aerial robot, 4 ground robots
    if(set == 1):
        robot_list.add(robot(SET_ONE_ID(0), TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.add(robot(SET_ONE_ID(1), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.add(robot(SET_ONE_ID(2), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.add(robot(SET_ONE_ID(3), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.add(robot(SET_ONE_ID(4), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        print("Created Set-1 of Robot Sets.")

def create_tasks(set):

    SET_ONE_ID = [1,2,3,4,5]

    TASK_AERIAL_FIREFIGHT = "aerial_fire_extinguish"
    TASK_GROUND_FIREFIGHT = "ground_fire_extinguish"
    TASK_AERIAL_RESCUE = "aerial_rescue"
    TASK_GROUND_RESCUE = "ground_rescue"

    QUALITY_AERIAL_FIREFIGHT = 6
    QUALITY_GROUND_FIREFIGHT = 4
    QUALITY_AERIAL_RESCUE = 10
    QUALITY_GROUND_RESCUE = 8

    SAMPLE_COORDINATE_X = 150
    SAMPLE_COORDINATE_Y = 150
    SAMPLE_COORDINATE_Z = 0
    SAMPLE_COORDINATES = Coordinate(SAMPLE_COORDINATE_X, SAMPLE_COORDINATE_Y, SAMPLE_COORDINATE_Z)

    # set-1, 1 aerial firefight, 3 ground firefight, 1 ground rescue 
    if(set == 1):
        task_list.add(Task(SET_ONE_ID(0), QUALITY_AERIAL_FIREFIGHT, SAMPLE_COORDINATES, TASK_AERIAL_FIREFIGHT))
        task_list.add(Task(SET_ONE_ID(1), QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.add(Task(SET_ONE_ID(2), QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.add(Task(SET_ONE_ID(3), QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.add(Task(SET_ONE_ID(4), QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        print("Created Set-1 of Task Sets.")

# calculate the distances of all the robots to the tasks in the task queue
# the distance is the 3d euclidean distance of the task and the robot 
def calculate_distance(robot_coordinates, task_coordinates):
    x_axis_distance = robot_coordinates.get_x_coordinate() - task_coordinates.get_x_coordinate()
    x_axis_distance = pow(x_axis_distance, 2)
    y_axis_distance = robot_coordinates.get_y_coordinate() - task_coordinates.get_y_coordinate()
    y_axis_distance = pow(y_axis_distance, 2)
    z_axis_distance = robot_coordinates.get_z_coordinate() - task_coordinates.get_z_coordinate()
    z_axis_distance = pow(z_axis_distance, 2)
    distance = math.sqrt(x_axis_distance + y_axis_distance + z_axis_distance)
    return distance

# calculate the visibility of all the robots to the tasks 
# visibility is the inverse of the distance
# if a task is more visible, robots will be attracted more
def calculate_visibility(distance):
    visibility = 1/distance
    return visibility


# calculate the relative quality of the tasks 
# this is done to make sure that the sum of all the relative qualities is 1
# to find the relative quality of any task, we take the scalar quality and divide it by the summation of all the other tasks scalar quality
def calculate_relative_quality():
    quality_list = []
    total_quality = 0

    # Get all qualities and add them in the list 
    for task in task_list:
        quality = task.get_task_quality()
        quality_list.add(quality)
    
    # Calculate total quality
    for quality in quality_list:
        total_quality = quality + total_quality
    
    # Calculate relative quality
    for task in task_list:
        quality = task.get_task_quality()
        relative_quality = quality/total_quality
        task.set_relative_quality(relative_quality)


# calculate the probability of allocation for each robot and task set 
# this is done by taking the multiple of the tasks relative quality to the tasks visibility for that robot and dividing the result to the sum of all the other possible combinations
# Again the sum of the probabilities will be equal to 1. 
def calculate_utility(task_robot_visibility_set):
    for visibility_set in task_robot_visibility_set:
        task_index = 0
        task_utility_set = []
        for visibility in visibility_set:
            utility = visibility * task_list(task_index).get_task_relative_quality()
            task_utility_set.add(utility)
            index = index + 1

def main():
    create_robots(1)
    create_tasks(1)
    
    task_robot_visibility_set = [[]]

    # Calculating capability, distance sets, visibility sets
    for task in task_list:
        task_type = task.get_task_type()
        robot_capable = False
        robot_distance_from_task = []
        robot_visibility_from_task = []

        #check to see if the tasks in the queue can be accomplished by the current robots available 
        for robot in robot_list:
            capable_task_list = robot.get_is_capable()

            for capable_task in capable_task_list:
                if(capable_task == task_type):
                    robot_capable = True

            # calculate the distances of all the robots to the tasks in the task queue
            if(robot_capable == True):
                distance = calculate_distance(robot.get_robot_location(), task.get_task_location())
                robot_distance_from_task.add()
                robot_distance_from_task.add(distance)
                visibility = calculate_visibility(distance)
                robot_visibility_from_task.add(visibility)

            # Robot not capable, invalid distances and visibility
            else:
                distance = -1
                visibility = -1
                robot_distance_from_task.add(distance)
                robot_visibility_from_task.add(visibility)

        # Adding sets of robot visibility for this task to the main 2d array
        task_robot_visibility_set.add([robot_visibility_from_task])

    # Calculate relative quality
    calculate_relative_quality()

    # Calculate utility probabilities
    calculate_utility(task_robot_visibility_set)

if __name__ == '__main__':
    main()
