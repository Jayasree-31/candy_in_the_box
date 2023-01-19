Problem to solve:
```
You have N boxes numbered 1 through N and K candies numbered 1 through K. You put the candies in the boxes in the following order:
first candy in the first box,
second candy in the second box,
.......
........
so up to N-th candy in the Nth box,
the next candy in (N - 1)-th box,
the next candy in (N - 2)-th box
........
.......
and so on up to the first box,
then the next candy in the second box
...... and so on until there is no candy left.
So you put the candies in the boxes in the following order:
1,2,3....N,N-1,N-2,
Find the index of the box where you put the K-th candy.
```
example:

| box1      | box2 | box3     | box4      | box5 | box6     |box7     | box8 | box9     | box10     |
| :---:        |    :----:   |:----:   |:----:   |:----:   |:----:   |:----:   |:----:   |:----:   |          :---: |
| 1      | 2       | 3   | 4   |5   |6   |7   |8   |9  |10|
| 19     | 18  | 17   |16   |15  |14  |13   |12  |11| |
| | 20     | 21  | 22   |23   |24  |25  |26   |27  |28| 29|
| 39     | 38  | 37   |36   |35  |34  |33   |32 |31  |30| |


Execute the task by running the below command
> python get_candy_box_number.py
