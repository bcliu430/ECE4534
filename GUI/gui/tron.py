import sys
import math
import time
import numpy as np
from enum import Enum

try:
    import Tkinter
except:
    import tkinter as Tkinter

width = 6
height = 4
board = Tkinter.Tk()


class Direction(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rover:
    def __init__(self):
        self.trace = []
        self.init_pos = None

    def def_init_pos(self, x, y):
        self.init_pos = Point(x, y)

    def add_trace(self, x, y):
        point = Point(x, y)
        self.trace.append(point)


# main function to run on AITron competition website
def main():
    # game loop
    user = Rover()
    ai = Rover()

    while True:
        # n: total number of players (2 to 4).
        # p: your player number (0 to 3).
        n, p = [int(i) for i in input().split()]
        # for i in range(n):

        if p == 0:
            x0, y0, x1, y1 = [int(j) for j in input().split()]
            ai.def_init_pos(x0, y0)
            ai.add_trace(x1, y1)
            x0, y0, x1, y1 = [int(j) for j in input().split()]
            user.def_init_pos(x0, y0)
            user.add_trace(x1, y1)
        elif p == 1:
            x0, y0, x1, y1 = [int(j) for j in input().split()]
            user.def_init_pos(x0, y0)
            user.add_trace(x1, y1)
            x0, y0, x1, y1 = [int(j) for j in input().split()]
            ai.def_init_pos(x0, y0)
            ai.add_trace(x1, y1)

        # print(ai, file=sys.stder

        # print(ai, file=sys.stderr)
        # use minimax to find the list of equal points
        # loop through the point to get the closest path direction

        # A single line with UP, DOWN, LEFT or RIGHT
        direct = attack_predict(ai.trace, user.trace, ai, user)
        print(user.trace[-1].x, user.trace[-1].y, file=sys.stderr)
        print(ai.trace[-1].x, ai.trace[-1].y, file=sys.stderr)

        if direct == Direction.up:
            print("UP")
        elif direct == Direction.down:
            print("DOWN")
        elif direct == Direction.left:
            print("LEFT")
        elif direct == Direction.right:
            print("RIGHT")


def test():
    user = Rover()
    ai = Rover()

    user.add_trace(15, 14)
    user.add_trace(15, 13)
    # ai.add_trace(10, 7)
    # ai.add_trace(9, 7)

    ai.add_trace(19, 4)
    ai.add_trace(18, 4)
    # user.add_trace(17, 0)
    # user.add_trace(17, 1)

    direct = attack_predict(ai.trace, user.trace, ai, user)
    print(direct)


class Tron:
    def __init__(self):
        self.user_direct = Direction.down

    def connecting_head_with_keys(self, event=None):
        # print('hit')
        key = event.keysym
        if key == 'Left':
            direct = Direction.left
        elif key == 'Right':
            direct = Direction.right
        elif key == 'Up':
            direct = Direction.up
        elif key == 'Down':
            direct = Direction.down
        self.user_direct = direct

    def test2(self):
        user = Rover()
        ai = Rover()
        x = np.random.randint(width - 1)
        y = np.random.randint(height - 1)
        user.add_trace(x, y)
        user.def_init_pos(x, y)
        x = np.random.randint(width)
        y = np.random.randint(height)
        ai.add_trace(x, y)
        ai.def_init_pos(x, y)

        frame = Tkinter.Frame(board, width=100, height=100)
        board.bind('<Any-KeyPress>', self.connecting_head_with_keys)
        frame.pack()
        cur_matrix = np.zeros(shape=(height, width), dtype=np.int)

        state = 0

        while True:
            board.update_idletasks()
            board.update()
            if state == 0:
                direction = attack_predict(ai, user)
                ai_x = ai.trace[-1].x
                ai_y = ai.trace[-1].y

                if direction == Direction.up:
                    ai.add_trace(ai_x, ai_y - 1)
                elif direction == Direction.down:
                    ai.add_trace(ai_x, ai_y + 1)
                elif direction == Direction.left:
                    ai.add_trace(ai_x - 1, ai_y)
                elif direction == Direction.right:
                    ai.add_trace(ai_x + 1, ai_y)

                if cur_matrix[ai.trace[-1].y, ai.trace[-1].x] != 0:
                    print('You Win!')
                    break

                user_x = user.trace[-1].x
                user_y = user.trace[-1].y

                # print(user_direct)

                if self.user_direct == Direction.up:
                    user.add_trace(user_x, user_y - 1)
                elif self.user_direct == Direction.down:
                    user.add_trace(user_x, user_y + 1)
                elif self.user_direct == Direction.left:
                    user.add_trace(user_x - 1, user_y)
                elif self.user_direct == Direction.right:
                    user.add_trace(user_x + 1, user_y)

                if cur_matrix[user.trace[-1].y, user.trace[-1].x] != 0:
                    print('You Lose!')
                    break

                m_map, hit = visualize_map(user.trace, ai.trace)
                cur_matrix = m_map
                print(m_map)
                print()

                if hit:
                    print('Game Stop!')
                    break
                    # user.add_trace(x, y)
            time.sleep(0.1)
            state = state + 1
            if state == 9:
                state = 0


def visualize_map(trace1, trace2):
    matrix = np.zeros(shape=(height, width), dtype=np.int)
    for i in trace1:
        # print(i.x, i.y, file=sys.stderr)
        # if matrix[i.y, i.x] != 0:
        #     return matrix, True
        matrix[i.y, i.x] = 1

    for i in trace2:
        # if matrix[i.y, i.x] != 0:
        #     return matrix, True
        matrix[i.y, i.x] = 2

    return matrix, False


def mini_max(trace1, trace2):
    matrix1, matrix2 = flood_fill(trace1, trace2)
    # print(matrix1)
    # print("\n")
    # print(matrix2)
    # print("\n")

    matrix3 = (matrix1 < matrix2)
    # print(matrix3)

    return matrix3


def unique_count(matrix):
    unique, counts = np.unique(matrix, return_counts=True)
    result = dict(zip(unique, counts))
    return result


def attack_predict(ai, user):
    # initial moving direction can be improved.
    trace1 = ai.trace
    trace2 = user.trace

    if len(trace1) == 1:
        if ai.init_pos.y > height / 2:
            return Direction.up
        else:
            return Direction.down

    last_p = trace1[-2]
    current_p = trace1[-1]
    current_dir = None

    if last_p.x == current_p.x:
        if last_p.y > current_p.y:
            current_dir = Direction.up
        else:
            current_dir = Direction.down
    elif last_p.y == current_p.y:
        if last_p.x > current_p.x:
            current_dir = Direction.left
        else:
            current_dir = Direction.right

    matrix = mini_max(trace1, trace2)
    # print(matrix)
    result = unique_count(matrix)
    # print(result)

    x = trace1[-1].x - trace1[-2].x
    y = trace1[-1].y - trace1[-2].y

    straight_x = trace1[-1].x + x
    straight_y = trace1[-1].y + y

    left = 0
    right = 0

    left_x, left_y = 0, 0
    right_x, right_y = 0, 0

    if y == 0:
        if x > 0:
            left = -1
            right = 1

        if x < 0:
            left = 1
            right = -1

        left_y = trace1[-1].y + left
        left_x = trace1[-1].x

        right_y = trace1[-1].y + right
        right_x = trace1[-1].x

    elif x == 0:
        if y > 0:
            left = 1
            right = -1
        if y < 0:
            left = -1
            right = 1

        left_x = trace1[-1].x + left
        left_y = trace1[-1].y

        right_x = trace1[-1].x + right
        right_y = trace1[-1].y

    straight_predict = list(trace1)

    p = Point(straight_x, straight_y)
    straight_predict.append(p)

    left_predict = list(trace1)
    left_predict.append(Point(left_x, left_y))

    right_predict = list(trace1)
    right_predict.append(Point(right_x, right_y))

    straight_hit = False
    left_hit = False
    right_hit = False

    if check_trace_rep(ai, user, trace1, trace2, Point(straight_x, straight_y)) or check_hit_wall(
            Point(straight_x, straight_y)):
        straight_hit = True
    if check_trace_rep(ai, user, trace1, trace2, Point(left_x, left_y)) or check_hit_wall(Point(left_x, left_y)):
        left_hit = True
    if check_trace_rep(ai, user, trace1, trace2, Point(right_x, right_y)) or check_hit_wall(Point(right_x, right_y)):
        right_hit = True

    # print("check out", straight_hit, left_hit, right_hit, file=sys.stderr)

    if not straight_hit:
        result1 = unique_count(mini_max(straight_predict, trace2))
        # print(result1, file=sys.stderr)
    if not left_hit:
        result2 = unique_count(mini_max(left_predict, trace2))
        # print(result2, file=sys.stderr)
    if not right_hit:
        result3 = unique_count(mini_max(right_predict, trace2))
        # print(result3, file=sys.stderr)

    # print(straight_hit, left_hit, right_hit)

    max_v = 0
    max_index = -1
    if not straight_hit:
        if result1.get(True) > max_v:
            max_v = result1.get(True)
            max_index = 0
    # print(result2.get(True), file=sys.stderr)
    if not left_hit:
        if result2.get(True) > max_v:
            max_v = result2.get(True)
            max_index = 1
    if not right_hit:
        if result3.get(True) > max_v:
            max_v = result3.get(True)
            max_index = 2

    predict_direct = 0
    if max_index == 0:
        predict_direct = Direction.up
    if max_index == 1:
        predict_direct = Direction.left
    if max_index == 2:
        predict_direct = Direction.right

    # need if you are playing on ai tron website
    # print(predict_direct, file=sys.stderr)
    predict_direct = direction_interp(current_dir, predict_direct)
    return predict_direct


def check_trace_rep(ai, user, trace1, trace2, point):
    for i in trace1:
        if point.x == i.x and point.y == i.y:
            return True
    for i in trace2:
        if point.x == i.x and point.y == i.y:
            return True
    if ai.init_pos.x == point.x and ai.init_pos.y == point.y:
        return True
    if user.init_pos.x == point.x and user.init_pos.y == point.y:
        return True

    return False


def check_hit_wall(point):
    if 0 <= point.x < width and 0 <= point.y < height:
        return False
    return True


def flood_fill(trace1, trace2):
    point1 = trace1[-1]
    point2 = trace2[-1]

    to_continue = True
    matrix = np.zeros(shape=(height, width))
    for i in trace1:
        # print(i.x, i.y, file=sys.stderr)
        matrix[i.y, i.x] = -1

    for i in trace2:
        matrix[i.y, i.x] = -1

    # print(matrix)
    # print("\n")
    matrix[trace1[-1].y][trace1[-1].x] = 0
    matrix[trace2[-1].y][trace2[-1].x] = 0

    orig = matrix.copy()
    # print(orig)
    matrix1 = flood_fill_helper(matrix, trace1[-1].x, trace1[-1].y, 1)
    # print(orig)
    matrix2 = flood_fill_helper(orig, trace2[-1].x, trace2[-1].y, 1)

    # matrix2 = np.zeros(1)
    return matrix1, matrix2
    # return flood_set1, flood_set2


def direction_interp(cur_direct, direct):
    if direct == Direction.up:
        return cur_direct
    if cur_direct == Direction.up:
        if direct == Direction.left:
            return Direction.left
        if direct == Direction.right:
            return Direction.right
    if cur_direct == Direction.down:
        if direct == Direction.left:
            return Direction.right
        if direct == Direction.right:
            return Direction.left
    if cur_direct == Direction.left:
        if direct == Direction.left:
            return Direction.down
        if direct == Direction.right:
            return Direction.up
    if cur_direct == Direction.right:
        if direct == Direction.left:
            return Direction.up
        if direct == Direction.right:
            return Direction.down


def flood_fill_helper(matrix, x, y, value):
    matrix[y][x] = value
    to_continue = True
    points = [(x, y)]
    while to_continue:
        value = value + 1
        new_p = []
        for i in points:
            y = i[1]
            x = i[0]
            # print(matrix)
            # print(x, y, len(points))
            if x < width - 1:
                if matrix[y][x + 1] == 0:
                    matrix[y][x + 1] = value
                    new_p.append((x + 1, y))
            if x > 0:
                if matrix[y][x - 1] == 0:
                    matrix[y][x - 1] = value
                    new_p.append((x - 1, y))
            if y < height - 1:
                if matrix[y + 1][x] == 0:
                    matrix[y + 1][x] = value
                    new_p.append((x, y + 1))
            if y > 0:
                if matrix[y - 1][x] == 0:
                    matrix[y - 1][x] = value
                    new_p.append((x, y - 1))
        if len(new_p) == 0:
            to_continue = False
        # print(new_p)
        points = new_p

    return matrix


def check_point(point, plist):
    for i in plist:
        if point.x == plist.x and point.y == plist.y:
            return True
    return False


def get_direction_string(dir):
    if dir == Direction.up:
        return "UP"
    if dir == Direction.down:
        return "DOWN"
    if dir == Direction.left:
        return "LEFT"
    if dir == Direction.right:
        return "RIGHT"


# main()
# test()
# tron = Tron()
# tron.test2()
