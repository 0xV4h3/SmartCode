-- 1
SELECT `parent`.`name` `parent category`, COUNT(`parent`.`name`) AS `count` ,
IF(COUNT(`parent`.`name`) % 2 = 0, 'Even', 'Odd') AS `parity`
FROM `good_category` `parent`
JOIN `good_category` `child`
ON `parent`.`id` = `child`.`parent_id`
JOIN `good` g ON `child`.`id` = g.`category_id`
GROUP BY `parent`.`name`;

-- 2
-- 		1 variant
SELECT 
    g.`category_id`, 
    g.`name`, 
    COUNT(g.`category_id`) cnt, 
    IF(gc.`parent_id` <> 1, 
       'NOT TEA', 
       IF(COUNT(g.`category_id`) > 500, 'ENOUGH', 'NOT ENOUGH')
    ) `status`
FROM `good` g
JOIN `good_category` gc ON g.`category_id` = gc.`id`
WHERE g.`count` * g.`price` = 390000
GROUP BY g.`category_id`, g.`name`;

-- 		2 variant
SELECT 
    g.`category_id`, 
    g.`name`, 
    COUNT(g.`category_id`) cnt, 
    CASE 
        WHEN gc.`parent_id` <> 1 THEN 'NOT TEA'
        WHEN COUNT(g.`category_id`) > 500 THEN 'ENOUGH'
        ELSE 'NOT ENOUGH'
    END `status`
FROM `good` g
JOIN `good_category` gc ON g.`category_id` = gc.`id`
WHERE g.`count` * g.`price` = 390000
GROUP BY g.`category_id`, g.`name`;


