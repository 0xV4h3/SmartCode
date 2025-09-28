SELECT `id`, `name`, `count`
FROM `good`
ORDER BY `count` DESC
LIMIT 5;

SELECT `id`, `name`, `email`, `reg_date`
FROM `user`
ORDER BY `reg_date` DESC
LIMIT 3;

SELECT `name`, `count`, `price`
FROM `good`
ORDER BY `count` DESC, `price` 
LIMIT 10, 6;