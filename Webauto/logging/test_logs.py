# logging means - capture details , which are useful while debugging
# show the user details about execution of program

# warning to the users
# information to the users
# errors, critical errors user

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    #Intentional Logging to user
    LOGGER.info('This is information Logs')
    LOGGER.warning('This is warning Logs')
    LOGGER.error("This is error logs")
    LOGGER.critical("This is Critical logs")