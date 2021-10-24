'''
Prepared by: Renjith Paul
Prepared on: 17-01-2021
Purpose : This python program is read the csv and to reformat the data to JSON.
'''

import pandas as pd 
from datetime import date,timedelta,datetime
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def driver_registration(input_url):
  try:
    url_process='https://drive.google.com/uc?id=' + input_url.split('/')[-2]
    # list of column names which needs to be string
    str_cols = ['phone']
    dict_dtypes = {each : 'str'  for each in str_cols}
    # list of column names which needs to be timestamp format with 
    ts_cols = ['date_created','date_last_modified','active_date']

    logging.info('Reading the csv at {}'.format(datetime.today()))
    data_df = pd.read_csv(url_process,names=["id", "date_created", "date_last_modified", "active_date","name", "phone", "resign_date", "resign_reason",
                                  "status", "tipe", "area", "CONCAT('operator_',id)","modified_by", "vehicle_type", "helmet_qty", "jacket_qty",
                                  "vehicle_brand", "vehicle_year", "bike_type", "first_ride_bonus_awarded","is_doc_completed"],dtype=dict_dtypes)
    logging.info('CSV read completed at {}'.format(datetime.today()))

    for each in ts_cols:
      data_df[each] = pd.to_datetime(data_df[each]).dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    json_output = data_df.to_json(orient = 'records')
    logging.info('Reformating to JSON completed at {}'.format(datetime.today()))
    return json_output
  except Exception as err:
    logging.info('Error in reformating CSV to JSON : {}'.format(err))
    raise 

if __name__ == "__main__":
  driver_registration('https://drive.google.com/file/d/1hX87raudhsK-cihF2Xg9GOgxqswqJNTf/views')