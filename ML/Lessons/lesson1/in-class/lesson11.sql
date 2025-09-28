SELECT `id`, `name`
FROM `good`
WHERE `count` > 518;

SELECT `id`, `name`, `price`
FROM `good`
WHERE `count` = 0 AND 'price' >= 300;

SELECT `id`, `name`
FROM `good`
WHERE `name` LIKE "%таежный%";

SELECT `id`, `name`
FROM `good`
WHERE `name` LIKE "%манго%" AND `name` NOT LIKE "айс";

SELECT `id`, `name`,  `reg_date`
FROM `user`
WHERE YEAR(`reg_date`) = 2017 AND MONTH(`reg_date`) BETWEEN 3 AND 11; 

