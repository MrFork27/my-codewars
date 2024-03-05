SELECT SPLIT_PART(path, '/', 5) AS subdirectory
FROM directories
WHERE SUBSTRING(path, 1, LENGTH('/home/user/pictures/')) = '/home/user/pictures/'
GROUP BY subdirectory
HAVING SPLIT_PART(path, '/', 5) != ''
ORDER BY subdirectory ASC;