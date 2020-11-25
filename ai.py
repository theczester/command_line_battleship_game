import random
from constants import ROWS, COLS

def ai_shooting_pos(board, ships_poses, n_of_big_ships, n_of_medium_ships, n_of_small_ships):
  if n_of_big_ships > 0:
    for i in range(len(ships_poses)):
        for x in range(1, len(ships_poses[i])):
            if ships_poses[i][x][1] == 2:
              valid_shoot_poses = board.get_valid_shoots()
              if [ships_poses[i][0], ships_poses[i][x][0]-1] in valid_shoot_poses:
                return [ships_poses[i][0], ships_poses[i][x][0]-1]
              if [ships_poses[i][0], ships_poses[i][x][0]+1] in valid_shoot_poses:
                return [ships_poses[i][0], ships_poses[i][x][0]+1]
              if ships_poses[i][x][1]+1 == 2:
                if [ships_poses[i][0], ships_poses[i][x][0]+2] in valid_shoot_poses:
                  return [ships_poses[i][0], ships_poses[i][x][0]+2]

  if n_of_medium_ships > 0:
      for i in range(len(ships_poses)):
          for x in range(1, len(ships_poses[i])):
              if ships_poses[i][x][1] == 2:
                gotten_board = board.get_board()
                if gotten_board[ships_poses[i][0]][ships_poses[i][x][0]-1] != 2 and gotten_board[ships_poses[i][0]][ships_poses[i][x][0]+1] != 2:
                  valid_shoot_poses = board.get_valid_shoots()
                  if [ships_poses[i][0], ships_poses[i][x][0]-1] in valid_shoot_poses:
                    return [ships_poses[i][0], ships_poses[i][x][0]-1]
                  if [ships_poses[i][0], ships_poses[i][x][0]+1] in valid_shoot_poses:
                    return [ships_poses[i][0], ships_poses[i][x][0]+1]

  random_shoot = [random.randint(0, 10-1), random.randint(0, 10-1)]
  if random_shoot in board.get_valid_shoots():
      return random_shoot
  return ai_shooting_pos(board, ships_poses, n_of_big_ships, n_of_small_ships, n_of_medium_ships)