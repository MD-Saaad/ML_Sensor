from sensor.exception import SensorException
import sys

from sensor.logger import logging

def test_exception():
    try:
        logging.info("test divide by zero error message")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)    
    

if __name__ == "__main__": # Module control kismodule ko ham run karrah hai  name ko main.py sai replace
                            ##karenge file yaha pai run hogi prevent execution on import
    try:
        test_exception()
    except Exception as e:
        print(e)