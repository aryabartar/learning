SELECT distinct user.*
FROM (((user JOIN purchase USING (user_id)) JOIN product USING (product_id)) JOIN category ON product.category_id=category.category_id)
WHERE category.name="Sport"
;

SELECT *
FROM user
WHERE user_id IN 
(
    SELECT purchase.user_id
    FROM purchase NATURAL JOIN product
    WHERE product.product_id IN (
        SELECT DISTINCT product.product_id 
        FROM product JOIN category USING (category_id)
        WHERE category.name="Sport"
    )
)
;