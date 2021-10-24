'''
Prepared by: Renjith Paul
Prepared on: 17-01-2021
Purpose : This SQL file contains the assumptions and the optimzation steps and the optimized query

Assumptions:
1) This dataset cannot be accessed in the google big query instance and hence I cannot execute this.
2) There seems to be a comma missing between transactions subquery and amount subquery in payments subquery.
3) There can be multiple records for a same transaction_id like its state (completed,cancelled etc) in the source tables
4) For each transaction_id, the amount is available only for the completed transaction. All other reords of same transaction is null.

Optimization steps:
1) We can apply the filter for gopay_id and transaction time in transaction subquery itself to avoid full table scan.
2) Pull only required columns from the source tables ride,bills etc instead of using * 
3) Remove the DISTINCT on amonut as it may result in long result if there are multiple transactions with same amount.
2) There is no need of a seperate payments subquery as we can get the result directly.

Optimized query is as below: 
'''

WITH transaction AS (
  SELECT gopay_id,transaction_id,amount FROM ride
  WHERE DATE(transaction_time) = '2020-10-01' AND gopay_id = '1234' 
  UNION DISTINCT
  SELECT gopay_id,transaction_id,amount FROM bills
  WHERE DATE(transaction_time) = '2020-10-01' AND gopay_id = '1234'
  UNION DISTINCT
  SELECT gopay_id,transaction_id,amount FROM food
  WHERE DATE(transaction_time) = '2020-10-01' AND gopay_id = '1234' 
  UNION DISTINCT
  SELECT gopay_id,transaction_id,amount FROM pulsa
  WHERE DATE(transaction_time) = '2020-10-01' AND gopay_id = '1234' 
)
  SELECT
    gopay_id,
    DATE(creation_time) AS creation_date,
    (SELECT
     COUNT( DISTINCT transaction_id)
     FROM
     transaction) AS transactions,
    (SELECT
     SUM( amount) 
     FROM
     transaction) AS amount
  FROM
  gopay
  where 
  gopay_id = '1234'; 