import sys

sys.setrecursionlimit(30005)

commands = [input().split(' ') for _ in range(int(input()))]

n = 30003
# we don't use 0 index of disk_height
disk_height = [0] * (n+1)
# we don't use 0 index of col_height
col_height = [1] * (n+1)
# we don't use 0 index of parents
parents = [i for i in range(0, n + 1)]


def find_root(disk_x: int, parents: list, disk_height: list) -> int:
    if parents[disk_x] == disk_x:
        return disk_x
    tmp = parents[disk_x]
    parents[disk_x] = find_root(parents[disk_x], parents, disk_height)
    disk_height[disk_x] += disk_height[tmp]
    return parents[disk_x]


def merge(disk_x: int, disk_y: int, parents: list, col_height: list, disk_height: list):
    disk_x_root = find_root(disk_x, parents, disk_height)
    disk_y_root = find_root(disk_y, parents, disk_height)
    if disk_x_root == disk_y_root:
        return

    parents[disk_x_root] = disk_y_root

    disk_height[disk_x_root] += col_height[disk_y_root]

    col_height[disk_y_root] += col_height[disk_x_root]
    col_height[disk_x_root] = 0


for command in commands:
    if command[0] == 'Merge':
        disk_x, disk_y = int(command[1]), int(command[2])
        merge(disk_x, disk_y, parents, col_height, disk_height)
    else:
        disk_x = int(command[1])
        find_root(disk_x, parents, disk_height)
        print(disk_height[disk_x] + 1)
