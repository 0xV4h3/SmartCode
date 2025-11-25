-- 1
SELECT 
  SUBSTRING_INDEX(SUBSTR(email, INSTR(email, '@') + 1),'.',1) AS `domain`
FROM `user`
WHERE CHAR_LENGTH(SUBSTRING_INDEX(SUBSTR(email, INSTR(email, '@') + 1),'.',1)) = 3
GROUP BY `domain`
HAVING COUNT(*) = 1;

-- 2
SELECT `parent`.`name` `parent category`, COUNT(`parent`.`name`) AS `count`
FROM `good_category` `parent`
JOIN `good_category` `child`
ON `parent`.`id` = `child`.`parent_id`
JOIN `good` g ON `child`.`id` = g.`category_id`
GROUP BY `parent`.`name`;

-- 3
SELECT 
  CONCAT(
    'Статус заказа номер ', o.`id`, 
    ' пользователя \"', u.`name`, 
    '\" изменился ', DATE(osc.`time`), 
    ' с ', src.`code`, 
    ' на ', dst.`code`
  ) AS result
FROM `order_status_change` osc
JOIN `order` o ON osc.`order_id` = o.`id`
JOIN `user` u ON o.`user_id` = u.`id`
JOIN `order_status` src ON osc.`src_status_id` = src.`id`
JOIN `order_status` dst ON osc.`dst_status_id` = dst.`id`
WHERE src.`name` = 'Доставлен'
  AND dst.`name` = 'Оплачен'
  AND DATE(o.`creation_date`) = '2015-05-25';
