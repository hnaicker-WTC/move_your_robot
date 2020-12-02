import world.turtle.world

def run(robot_name, obstacles, environment):
    maze_run_executing = True
    while maze_run_executing:
        # current_coords = world.show_coords()
        # start_coords = (0,0)
        # start_coords = current_coords
        can_continue, reason = environment.update_position(4, obstacles)

        if can_continue:
            message =  ' > '+robot_name+' moved forward by '+str(4)+' steps.'
        else:
            if reason == "obstacles":
                environment.do_left_turn(robot_name)
                can_continue, reason = environment.update_position(4, obstacles)
                environment.do_right_turn(robot_name)
                message = ''+robot_name+': Sorry, there is an obstacle in the way'
                # current_coords = world.show_coords()
            
            # if reason == "obstacles" and current_coords == start_coords:
            #     environment.do_right_turn(robot_name)
            #     can_continue, reason = environment.update_position(4, obstacles)
            #     environment.do_left_turn(robot_name)
            else:
                print(''+robot_name+': Sorry, I cannot go outside my safe zone.')
                return True, ''+robot_name+': I am at the top edge.'

        print(message)
        environment.show_position(robot_name)
