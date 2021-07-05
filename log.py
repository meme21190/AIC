import logging
import sys

# creation du logger
logging.basicConfig(filename='projet6.log',format='%(asctime)s - %(name)s - %(levelname)s >>>> %(message)s',level=logging.DEBUG)
logger = logging.getLogger('script python admin')
logger.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
  try:
     logger.info('Action 1 [OK]')
  except:
     logger.warning('Action 1 [KO]')
