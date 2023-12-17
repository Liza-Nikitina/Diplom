#Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT c.login,
COUNT(o.*) AS order_quantity
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."inDelivery"= true
GROUP BY c.login;
#Для этого: выведи все трекеры заказов и их статусы.
SELECT track,
CASE
WHEN finished=true then '2'
WHEN cancelled=true then '-1'
WHEN "inDelivery"=true then '1'
ELSE '0'
END
FROM "Orders";