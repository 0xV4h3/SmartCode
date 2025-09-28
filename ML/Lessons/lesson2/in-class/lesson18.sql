-- 1
SELECT u.`name`, u.`email`
FROM `user` u
JOIN `order` o ON u.`id` = o.`user_id`
JOIN `order2good` og ON o.`id` = og.`order_id`
JOIN `good` g ON og.`good_id` = g.`id`
WHERE g.`name` LIKE "Гватемала%" ;

-- 2
SELECT u.`name`, u.`email`
FROM `user` u
JOIN `order` o ON u.`id` = o.`user_id`
JOIN `order_status` os ON o.`status_id` = os.`id`
WHERE u.`email` NOT LIKE "%.ru" AND u.`email` NOT LIKE "%.su" AND os.`name` LIKE "Упакован";

-- 3
SELECT u.`name`, u.`email`
FROM `user` u
JOIN `order` o ON u.`id` = o.`user_id`
JOIN `order2good` og ON o.`id` = og.`order_id`
JOIN `good` g ON og.`good_id` = g.`id`
JOIN `good_category` gc ON g.`category_id` = gc.`id`
WHERE gc.`name` LIKE "Кофе без кофеина" ;
