### Description

* A toy robot that can execute a set number of commands to move around a series of obstacles or a preselected maze all enclosed in a rectangular border.
* This programme has a turtle graphics component that is initialised on execution of the programme by including the command-line argument `turtle` 
  e.g.  `python3 robot.py turtle`.
* To navigate through one of the mazes included in this repo specify on execution:
   * Default `python3 robot.py` (random blocks of 5x5 will appear for the robot to navigate around)
   * Text maze `python3 robot.py new_maze`
   * Turtle graphics `python3 robot.py turtle new_maze`
* Use the help function to learn more about what the robot can do

### To Run

* `python3 robot.py`
* optional flags for commandline are:
  - turtle
  - mazes (default == `obstacles`):
     ** `stupid_maze` or `new_maze`
* follow the input prompts to move your robot around

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.
