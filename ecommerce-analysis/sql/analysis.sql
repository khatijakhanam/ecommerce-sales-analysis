-- Top 5 products by revenue
SELECT product_name, SUM(revenue) AS total_revenue, COUNT(*) AS orders
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC LIMIT 5;

-- Monthly sales trend
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(revenue) AS monthly_revenue,
       COUNT(DISTINCT order_id) AS total_orders
FROM sales
GROUP BY month ORDER BY month;

-- High-value customers (top 10%)
SELECT customer_id, SUM(revenue) AS lifetime_value,
       COUNT(*) AS purchase_count
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 3
ORDER BY lifetime_value DESC LIMIT 50;

-- Repeat purchase rate
SELECT ROUND(
  COUNT(DISTINCT CASE WHEN purchase_count > 1 THEN customer_id END) * 100.0
  / COUNT(DISTINCT customer_id), 2
) AS repeat_purchase_rate_pct
FROM (
  SELECT customer_id, COUNT(*) AS purchase_count FROM sales GROUP BY customer_id
) t;

-- Revenue by category and region
SELECT category, region, SUM(revenue) AS revenue,
       RANK() OVER (PARTITION BY category ORDER BY SUM(revenue) DESC) AS region_rank
FROM sales GROUP BY category, region;