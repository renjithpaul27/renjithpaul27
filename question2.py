'''
Prepared by: Renjith Paul
Prepared on: 17-01-2021
Purpose : This python program is to run the go-jek SQL analysis query and returns the result as list.
          It prompts for the inputs while execution.
'''

from google.cloud import bigquery
from datetime import date,timedelta,datetime
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def gojek_service_analysis(start_date = date.today() - timedelta(1),end_date = date.today()):
  
  # Intializes the client to bigquery db
  BigQuery_client = bigquery.Client()
  try:
    logging.info('Executing the query to fetch data between {} and {}'.format(start_date,end_date))
    customer_query = """
            select 
                order_date,
                count(customer_no) as customer_cnt,
                orders,
                order_payment
            from (
                select 
                    customer_no,
                    STRING_AGG(distinct order_type ORDER BY order_type) AS orders,
                    STRING_AGG(distinct order_payment ORDER BY order_payment) AS order_payment,
                    EXTRACT(DATE FROM order_time) order_date 
                from `bi-dwhdev-01.source.daily_order`
                where EXTRACT(DATE FROM order_time) between '{}' and '{}'
                    and order_status='Completed'
                group by customer_no,order_date
                )
            group by order_date,orders,order_payment
            order by order_date,orders,order_payment
          """.format(start_date,end_date)

    logging.info('Query execution started at {}'.format(datetime.today()))
    customer_query_result = BigQuery_client.query(customer_query)
    logging.info('Query execution completed at {}'.format(datetime.today()))
    # Converts the google bigquery object result to list
    result_list = [each for each in customer_query_result]
    logging.info('Number of records returned :  {}'.format(len(result_list)))
    return result_list
  except Exception as err:
    logging.info('Error in loading the gojek service analysis : {}'.format(err))
    raise
  finally:
    logging.info('Database connection closed at :  {}'.format(datetime.today()))
    BigQuery_client.close()
    


if __name__ == "__main__":
  type_of_execution = input("Enter the type of execution : 1) Normal execution 2) Backfill execution: ")
  if type_of_execution == '1':
    logging.info("Normal exectuion")
    gojek_service_analysis()
  elif type_of_execution == '2':
    start_date = input("Enter the start date of backfill (YYYY-MM-DD) : ")
    end_date = input("Enter the end date of backfill (YYYY-MM-DD) : ")
    logging.info("Backfill exectuion")
    gojek_service_analysis(start_date,end_date)
  else:
    logging.info("Wrong entry! Please try again")


    
  