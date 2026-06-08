# ROS 2 - Publisher nodes and subscriber nodes examples
 
## Description
 
The package contains some basic publisher and subscriber nodes examples for testing fuctions of ros2.
 
## Prerequisites
 
- ROS 2 installed
- Python 3
- Created ROS 2 workspace (`ros2_ws`)

## How to run

Assuming you have a ros2 workspace (for example, ```ros2_ws```), which has been built with ```colcon build``` and has the ```src``` folder inside, you have to follow these steps:

- First, add the package inside the ```src``` folder in you workspace. Change its name to ```ros2_fundamentals_examples```. Your workspace should be like:

-```ros2_ws``` (or your workspace name)
|
|-```build```
|
|-```install```
|
|-```log```
|
|-```src```
    |
    |-```ros2_fundamentals_examples``` (the package folder)
        |
        |-```include```
        |
        |-```ros2_fundamentals_examples```
        |
        |-```scripts```
        |
        |-```src```
        |
        |-```CMakeLists.txt```
        |
        |-```LICENSE```
        |
        |-```README.md```
        |
        |-```package.xml```

- Second, build again your workspace with ```colcon build```, and then run ```source ~/.bashrc```.

- Third, run a node with the command ```ros2 run ros2_fundamentals_examples marco_polo_publisher.py```. 

That is just an example, but you can use all this nodes:

- ```marco_polo_publisher``` -Publishes the message "marco polo" every .5 seconds on the topic - ```/marco_polo```.

- ```marco_polo_subscriber``` -Listens to the topic ```/marco_polo``` and logs the lenght of the messages published there.

- ```milky_publisher``` -Publishes the message "milky" every .5 seconds on the topic ```/milky```.

- ```milky_subscriber``` -Listens to the topic ```/milky``` and logs the lenght of the messages published there.

- ```carico_pub_sub``` -Listens to the topic ```/marco_polo``` and publishes the lenght of the message published there multiplied by 40, divided by 35 and then converted to and integer.

## Author and credits

Every thing here is based on the work of Automatic Addison.

Modified by Francisco Ibarra