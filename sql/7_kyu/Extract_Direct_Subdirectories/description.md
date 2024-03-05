# Extract Direct Subdirectories (7 kyu)

- [Exercise link](https://www.codewars.com/kata/653bd2c1355c3a1309f407f2)

DESCRIPTION:
Given a table containing directory paths, write a SQL query to extract all direct subdirectories of a specified base directory. The results should be in alphabetical order.

We have directories table

- `id` (integer): primary key
- `path` (varchar): column containing directory paths.

Task Requirements:

1. Your query should extract direct subdirectories of the base path /home/user/pictures/.
2. The result should not contain the full path, but only the direct subdirectory name.
3. The result should not have duplicates.
4. The result should be sorted in alphabetical order.
5. The result should contain single subdirectory column

For this sample data:

```
| id |                   path                      |
+----+---------------------------------------------+
| 1  | /home/user/pictures/books/2022              |
| 2  | /home/user/pictures/vacation                |
| 3  | /home/user/pictures/work/2023/important     |
| 4  | /home/user/pictures/vacation/2023           |
```

query needs to return

```
| subdirectory |
+--------------+
| books        |
| vacation     |
| work         |
```

GLHF!
