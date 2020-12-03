import world.turtle.world

def run(robot_name, obstacles, environment, edge):

    
    maze_run_executing = True
    while maze_run_executing:
        
        current_coords = set(world.show_coords())
        can_continue, reason = environment.update_position(4, obstacles)

        if can_continue and edge == 'top':
            message =  ' > '+robot_name+' moved forward by '+str(4)+' steps.'

        elif edge =='bottom':
            environment.do_left_turn(robot_name)
            environment.do_left_turn(robot_name)
            can_continue, reason = environment.update_position(4, obstacles)
            message =  ' > '+robot_name+' moved forward by '+str(4)+' steps.'

        elif edge == 'right':
            environment.do_right_turn(robot_name)
            can_continue, reason = environment.update_position(4, obstacles)
            message =  ' > '+robot_name+' moved forward by '+str(4)+' steps.'

        elif edge == 'left':
            environment.do_left_turn(robot_name)
            can_continue, reason = environment.update_position(4, obstacles)
            message =  ' > '+robot_name+' moved forward by '+str(4)+' steps.'
        else:
            if reason == "obstacles":
                environment.do_left_turn(robot_name)
                can_continue, reason = environment.update_position(4, obstacles)
                environment.do_right_turn(robot_name)
                message = ''+robot_name+': Sorry, there is an obstacle in the way'
                current_coords.update(world.position_x, world.position_y)
            
            # if reason == "obstacles" and current_coords == start_coords:
            #     environment.do_right_turn(robot_name)
            #     can_continue, reason = environment.update_position(4, obstacles)
            #     environment.do_left_turn(robot_name)
            else:
                print(''+robot_name+': Sorry, I cannot go outside my safe zone.')
                return True, ''+robot_name+': I am at the top edge.'

        print(message)
        environment.show_position(robot_name)
