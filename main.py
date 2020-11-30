from board import player_board, enemy_board
from ai import ai_shooting_pos
import time
from constants import LETTERS_TO_NUMBERS, LETTERS

run = True

def main():
    player_board_shoot_highlight = []
    enemy_board_shoot_highlight = []
    while run:
        try:
            if enemy_board.count_ships() <= 0:
                print('YOU WON THE GAME!!!')
                print('With ', player_board.count_ships(), ' occupied positions remaining.')
                break
            if player_board.count_ships() <= 0:
                print('YOU LOST THE GAME!!!')
                print('With ', enemy_board.count_ships(), " enemy's occupied positions remaining.")
                break

            player_board.draw('player_board', player_board_shoot_highlight)
            enemy_board.draw('enemy_board', enemy_board_shoot_highlight)

            not_shot = True

            while not_shot:
                shoot_pose = input('Choose your shooting position (e.g A 9) : ').replace(' ', '')
                shoot_pose = (shoot_pose[0]+' '+shoot_pose[1:]).split(' ')
                try:
                    if int(shoot_pose[1]) >= 10 or int(shoot_pose[1]) > 0:
                        is_col_wrong_num = False
                    else:
                        is_col_wrong_num = True
                except:
                    is_col_wrong_num = True
                if shoot_pose[0].upper() not in LETTERS or is_col_wrong_num:
                    print('\n')
                    print('Please enter a valid postion (e.g A 9) !!!', end='\n'*3)
                    continue
                print('\n')
                shoot_pose = [LETTERS_TO_NUMBERS[shoot_pose[0].upper()]-1, int(shoot_pose[1])-1]
                if shoot_pose in enemy_board.get_valid_shoots():
                    gotten_enemy_board = enemy_board.get_board()
                    if gotten_enemy_board[shoot_pose[0]][shoot_pose[1]] == 1:
                        print('You hit the enemy ship!', end="\n"*2)
                    else:
                        print('You missed the shoot!', end="\n"*2)

                    enemy_board.shoot(shoot_pose[0], shoot_pose[1])
                    not_shot = False
                else:
                    print("Please enter a position which you didn't already chose!", end="\n"*3)
                    continue
            enemy_board_shoot_highlight = shoot_pose


            poses_and_types_of_ships = player_board.count_types_and_get_poses_of_ships_onboard()
            enemy_shooting_pos = ai_shooting_pos(
                player_board,
                poses_and_types_of_ships['ships_poses'],
                poses_and_types_of_ships['types_of_ships']['big_ships'],
                poses_and_types_of_ships['types_of_ships']['medium_ships'],
                poses_and_types_of_ships['types_of_ships']['small_ships']
            )
            player_board_shoot_highlight = enemy_shooting_pos

            gotten_player_board = player_board.get_board()
            if gotten_player_board[enemy_shooting_pos[0]][enemy_shooting_pos[1]] == 1:
                print('Your ship has been hit!', end="\n"*3)
            else:
                print('Enemy missed the shoot!', end="\n"*3)

            player_board.shoot(enemy_shooting_pos[0], enemy_shooting_pos[1])

            print('Next round starts in... (CTRL+C to skip)', end="\n"*2)
            time.sleep(1)
            try:
                for i in range(5, 0, -1):
                    print(i)
                    time.sleep(1)
            except KeyboardInterrupt:
                continue
        except KeyboardInterrupt:
            pass

main()
