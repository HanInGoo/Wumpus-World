elif (x_value + 100 < 200 and num + 1 <= 15) and (
            visit_sequence[len(visit_sequence) - 1][0] == x_value and visit_sequence[len(visit_sequence) - 1][
        1] == y_value) and ((WorldRandom.wumpus_list_x[num + 1][0] != x_value + 100 and
                             WorldRandom.wumpus_list_x[num + 1][1] != y_value) or (
                                        WorldRandom.pitch_list_x[num + 1][0] != x_value + 100 and
                                        WorldRandom.pitch_list_x[num + 1][1] != y_value)):
# 범위를 넘어가지 않게 유지한다 / 현재 위치가 전에 방문했던 순차 리스트에 존재 하는 확인한다. /다시 돌아가야 하는 길에 wumpus와 구덩이가 없는지 확인한다.
print("왔던 길로 돌아기기 전=")
print(visit_sequence)
print()

t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],
       visit_sequence[(len(visit_sequence) - 1) - 1][1])  # 현재 위치에 오기 전에 왔던 길로 돌아간다.
visit_sequence.pop()  # 마지막으로 이동했던 위치를 리스트에서 삭제한다.

print("왔던 길로 돌아간 후")
print(visit_sequence)
print()

if visit_sequence[len(visit_sequence) - 1][0] + 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
    num = num + 1  # 되돌아간 칸값을 반영하다.(num+1)
elif visit_sequence[len(visit_sequence) - 1][0] - 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
    num = num - 1  # 되돌아간 칸값을 반영하다.(num-1)
elif visit_sequence[len(visit_sequence) - 1][0] == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1] + 100:
    num = num - 4  # 되돌아간 칸값을 반영하다.(num-4)
elif visit_sequence[len(visit_sequence) - 1][0] == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1] - 100:
    num = num + 4  # 되돌아간 칸값을 반영하다.(num+4)

x_value = visit_sequence[(len(visit_sequence) - 1) - 1][0]  # 되돌아간 x좌표 위치를 반영한다.
y_value = visit_sequence[(len(visit_sequence) - 1) - 1][1]  # 되돌아간 y좌표 위치를 반영한다.

elif (x_value - 100 > -200 and num - 1 >= 0) and (
            visit_sequence[len(visit_sequence) - 1][0] == x_value and visit_sequence[len(visit_sequence) - 1][
        1] == y_value) and ((WorldRandom.wumpus_list_x[num - 1][0] != x_value - 100 and
                             WorldRandom.wumpus_list_x[num - 1][1] != y_value) or (
                                        WorldRandom.pitch_list_x[num - 1][0] != x_value - 100 and
                                        WorldRandom.pitch_list_x[num - 1][1] != y_value)):
print("왔던 길로 돌아기기 전==")
print(visit_sequence)
print()

t.goto(x_value - 100, y_value)
visit_sequence.pop()

print("왔던 길로 돌아간 후")
print(visit_sequence)
print()

x_value = x_value - 100  # 움직인 좌표값을 반영한다.(x_value-100)
num = num - 1  # 움직인 좌표값을 반영하다.(num-1)

elif (y_value + 100 < 200 and num - 4 >= 0) and (
            visit_sequence[len(visit_sequence) - 1][0] == x_value and visit_sequence[len(visit_sequence) - 1][
        1] == y_value) and ((WorldRandom.wumpus_list_x[num - 4][0] != x_value and WorldRandom.wumpus_list_x[num - 4][
    1] != y_value + 100) or (WorldRandom.pitch_list_x[num - 4][0] != x_value and WorldRandom.pitch_list_x[num - 4][
    1] != y_value + 100)):
print("왔던 길로 돌아기기 전=")
print(visit_sequence)
print()

t.goto(x_value, y_value + 100)
visit_sequence.pop()

print("왔던 길로 돌아간 후")
print(visit_sequence)
print()

y_value = y_value + 100  # 움직인 좌표값을 반영한다.(y_value+100)
num = num - 4  # 움직인 좌표값을 반영하다.(num-4)

elif (y_value - 100 > -200 and num + 4 <= 15) and (
            visit_sequence[len(visit_sequence) - 1][0] == x_value and visit_sequence[len(visit_sequence) - 1][
        1] == y_value) or ((WorldRandom.wumpus_list_x[num + 4][0] != x_value and WorldRandom.wumpus_list_x[num + 4][
    1] != y_value - 100) or (WorldRandom.pitch_list_x[num + 4][0] != x_value and WorldRandom.pitch_list_x[num + 4][
    1] != y_value - 100)):

print("왔던 길로 돌아기기 전=")
print(visit_sequence)
print()

t.goto(x_value, y_value - 100)
visit_sequence.pop()

print("왔던 길로 돌아간 후")
print(visit_sequence)
print()

y_value = y_value - 100  # 움직인 좌표값을 반영한다.(y_value-100)
num = num + 4  # 움직인 좌표값을 반영하다.(num+4)










(WorldRandom.wumpus_list_x[num+1][0]==x_value+100 and WorldRandom.wumpus_list_x[num+1][1]==y_value)
            or (WorldRandom.wumpus_list_x[num-1][0]==x_value-100 and WorldRandom.wumpus_list_x[num-1][1]==y_value)
            or (WorldRandom.wumpus_list_x[num-4][0]==x_value and WorldRandom.wumpus_list_x[num-4][1]==y_value+100)
            or (WorldRandom.wumpus_list_x[num+4][0]==x_value and WorldRandom.wumpus_list_x[num+4][1]==y_value-100)

            or (WorldRandom.pitch_list_x[num+1][0]==x_value+100 and WorldRandom.pitch_list_x[num+1][1]==y_value)
            or (WorldRandom.pitch_list_x[num-1][0]==x_value-100 and WorldRandom.pitch_list_x[num-1][1]==y_value)
            or (WorldRandom.pitch_list_x[num-4][0]==x_value and WorldRandom.pitch_list_x[num-4][1]==y_value+100)
            or (WorldRandom.pitch_list_x[num+4][0]==x_value and WorldRandom.pitch_list_x[num+4][1]==y_value-100)

            or (WorldRandom.bump_list_x[0][0]==x_value and WorldRandom.bump_list_x[0][1]==y_value)
            or (WorldRandom.bump_list_x[3][0]==x_value and WorldRandom.bump_list_x[3][1]==y_value)
            or (WorldRandom.bump_list_x[12][0]==x_value and WorldRandom.bump_list_x[12][1]==y_value)
            or (WorldRandom.bump_list_x[15][0] == x_value and WorldRandom.bump_list_x[15][1] == y_value)