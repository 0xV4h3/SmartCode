-- 1
SELECT o.`id`
FROM  `order_status` os
JOIN `order` o ON os.`id` = o.`id` ;

-- 2
SELECT g.`id`, og.`count`
FROM `good` g
JOIN `order2good` og ON g.`id` = og.`good_id`
LIMIT 5;

-- 3
SELECT DISTINCT osc.`src_status_id` `source`, osc.`dst_status_id` `destination`
FROM `order_status_change` osc
JOIN `order` o ON osc.`order_id` = o.`id`;

-- 4
SELECT os.`name`, COUNT(*) `order_count`
FROM `order_status` os
JOIN `order` o ON os.`id` = o.`status_id`
GROUP BY os.`name`
ORDER BY COUNT(*);

-- 5
SELECT u.`name`
FROM `user` U
JOIN `order` o ON u.`id` = o.`user_id`
JOIN `order2good` og ON o.`id` = og.`order_id`
JOIN `good` g ON og.`good_id` = g.`id`
WHERE g.`name` = "пуэр с молоком" ;

-- 6
--   1 variant
SELECT 	g.`id`, g.`name`
FROM `good` g
LEFT JOIN `order2good` og ON g.`id` = og.`good_id`
WHERE og.`good_id` is NULL;

--   2 variant
SELECT DISTINCT g.`id`, g.`name`
FROM `good` g
JOIN `order2good` og ON g.`id` != og.`good_id`;