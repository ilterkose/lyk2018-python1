import logging

logging.basicConfig(filename="hata.log",level=logging.INFO)

logging.warning('Watch out!') # will print a message to the console
logging.info('I told u')
logging.critical('Dalek! Dalek!')
logging.error('hacked by ilter')
