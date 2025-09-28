USE `shopdb`;

SELECT *
FROM `good`
WHERE `price` > 800;

SELECT *
FROM `good`
WHERE `count` = 0;

SELECT `id`, `user_id`
FROM `order`
WHERE YEAR(`creation_date`) = 2016 AND MONTH(`creation_date`) = 4 AND DAYOFMONTH(`creation_date`) = 1 AND `status_id` = 7;
