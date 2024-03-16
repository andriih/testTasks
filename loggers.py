import logging

class Loggers:

    @staticmethod
    def log_message(application, msg, level):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            f_handler = logging.FileHandler(application)
            f_format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(msg)s', 
                                         datefmt='%Y-%m-%d %H:%M:%S')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)

        if level == "INFO":
             logger.info(msg)
        elif level == "WARNING":
             logger.warning(msg)
        elif level == "ERROR":
            logger.error(msg)
        else:
            raise ValueError("Invalid log level")



Loggers.log_message("application.log", "User logged in", "INFO")
Loggers.log_message("application.log", "Failed login attempt", "WARNING")

