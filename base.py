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

import robot
import Task
import Coordinate

def create_robots(set):

    TYPE_GROUND = "ground_robot"
    TYPE_AERIAL = "aerial_robot"
    BASE_LOCATION_X = 100
    BASE_LOCATION_Y = 100
    BASE_LOCATION_Z = 0
    TASK_LIST_GROUND = [ground_fire_extinguish, ground_rescue]
    TASK_LIST_AERIAL = [aerial_fire_extinguish, aerial_rescue] 
    SET_ONE_ID = [1,2,3,4,5]

    BASE_COORDINATES = Coordinate(BASE_LOCATION_X, BASE_LOCATION_Y, BASE_LOCATION_Z)


    # set-1, 1 aerial robot, 4 ground robots
    if(set == 1):
        aerial_robot_one = robot(SET_ONE_ID(0), TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL)
        ground_robot_one = robot(SET_ONE_ID(1), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND)
        ground_robot_two = robot(SET_ONE_ID(2), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND)
        ground_robot_three = robot(SET_ONE_ID(3), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND)
        ground_robot_four = robot(SET_ONE_ID(4), TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND)



def main():
    sample = 0



if __name__ == '__main__':
    main()
