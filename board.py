import random
import time
from constants import ROWS, COLS, NUMBER_OF_BIG_SHIPS , NUMBER_OF_MEDIUM_SHIPS, NUMBER_OF_SMALL_SHIPS, LETTERS


class Board:
    def __init__(self):
        self.board = [[0]*10 for x in range(10)]
        self.generate_ships(
            NUMBER_OF_BIG_SHIPS,
            NUMBER_OF_MEDIUM_SHIPS,
            NUMBER_OF_SMALL_SHIPS
        )

    def get_board(self):
        return self.board

    def generate_ships(self, n_big_ships, n_medium_ships, n_small_ships):
        self.add_ships_in_random_pos(n_big_ships, 3)
        self.add_ships_in_random_pos(n_medium_ships, 2)
        self.add_ships_in_random_pos(n_small_ships, 1)

    def add_ships_in_random_pos(self, n_of_ships, ship_length):
        for i in range(n_of_ships):
            random_pos = self.generate_random_untaken_pos(ship_length)
            for x in range(len(random_pos)-1):
                self.board[random_pos[0]][random_pos[x+1]] = 1

    def get_untaken_poses(self):
        untaken_poses = []
        for row in range(ROWS-1):
            for col in range(COLS-1):
                if self.board[row][col] == 0:
                    untaken_poses.append((row, col))
        return untaken_poses

    def generate_random_untaken_pos(self, ship_length):
        random_row, random_col = random.randint(0, ROWS-1), random.randint(0, COLS-3-ship_length)
        random_pos = [random_row]
        for i in range(ship_length+2):
            if self.board[random_row][random_col+i] == 0:
                random_pos.append(random_col+i)
            else:
                return self.generate_random_untaken_pos(ship_length)

        random_pos.pop(len(random_pos)-1)
        random_pos.pop(1)

        return random_pos

    def count_ships(self):
        counter = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1:
                    counter +=1
        return counter

    def count_types_and_get_poses_of_ships_onboard(self):
        ships_poses = []
        current_ship = []
        n_of_big_ships = 0
        n_of_medium_ships = 0
        n_of_small_ships = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1 or self.board[row][col] == 2:
                    if len(current_ship) == 0:
                        current_ship.append(row)
                    current_ship.append([col, self.board[row][col]])
                elif self.board[row][col-1]  != 0:
                    if len(current_ship) == 2:
                        n_of_small_ships += 1
                    elif len(current_ship) == 3:
                        n_of_medium_ships += 1
                    else:
                        n_of_big_ships += 1
                    ships_poses.append(current_ship)
                    current_ship = []

        return {
            'ships_poses': ships_poses,
            'types_of_ships': {
                'big_ships': n_of_big_ships,
                'medium_ships': n_of_medium_ships,
                'small_ships': n_of_small_ships
            }
        }

    def draw(self, view_type='player_board', shoot_highlight=[]):
        print('\n')
        if view_type == 'player_board':
            print('-'*12 + ' YOUR BOARD ' + '-'*12)
        else:
            print('-'*12 + ' ENEMY BOARD ' + '-'*12)
        print('\n')
        print(' '*6, end='')
        for num in range(10):
            print(str(num+1) + ' '*2, end='')
        print('\n'*2)
        if view_type == 'player_board':
            player_board_view = [[0]*10 for x in range(10)]
            for row in range(ROWS):
                for col in range(COLS):
                    if self.board[row][col] == -1:
                        player_board_view[row][col] = ' '
                    elif self.board[row][col] == 2:
                        player_board_view[row][col] = 'X'
                    elif self.board[row][col] == 1:
                        player_board_view[row][col] = 1
                    elif self.board[row][col] == 0:
                        player_board_view[row][col] = 0
            for row in range(ROWS):
                print(LETTERS[row], end=' '*5)
                for col in range(COLS):
                    print(''.join(str(player_board_view[row][col])), end=' '*2, flush=True)
                    if len(shoot_highlight) == 2 and row == shoot_highlight[0] and col == shoot_highlight[1]:
                        time.sleep(2)
                    else:
                        time.sleep(0.01)
                print('\n')
        else:
            enemy_board_view = [[0]*10 for x in range(10)]
            for row in range(ROWS):
                for col in range(COLS):
                    if self.board[row][col] == -1:
                        enemy_board_view[row][col] = ' '
                    elif self.board[row][col] == 2:
                        enemy_board_view[row][col] = 'X'
                    elif self.board[row][col] == 1 or self.board[row][col] == 0:
                        enemy_board_view[row][col] = '?'
            for row in range(ROWS):
                print(LETTERS[row], end=' '*5)
                for col in range(COLS):
                    print(''.join(str(enemy_board_view[row][col])), end=' '*2, flush=True)
                    if len(shoot_highlight) == 2 and row == shoot_highlight[0] and col == shoot_highlight[1]:
                        time.sleep(1.25)
                    else:
                        time.sleep(0.01)
                print('\n')

    def get_valid_shoots(self):
        valid_shoots = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1 or self.board[row][col] == 0:
                    valid_shoots.append([row, col])
        return valid_shoots

    def shoot(self, row, col):
        if self.board[row][col] == 1:
            self.board[row][col] = 2
        elif self.board[row][col] == 0:
            self.board[row][col] = -1



player_board = Board()
enemy_board = Board()
