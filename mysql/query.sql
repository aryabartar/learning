SELECT *
FROM (
    SELECT user.user_id, sum(purchase.quantity) AS purchaseQuantity
    FROM ((user NATURAL JOIN purchase) JOIN product 
        ON purchase.product_id=product.product_id) JOIN category
            ON product.category_id=category.category_id
    WHERE category.name="Sport"
    GROUP BY user.user_id
) AS sportBuy
WHERE sportBuy.purchaseQuantity>3
;