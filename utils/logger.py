import logging.handlers
import logging

automation_title = "[TEST AUTOMATION]"


class Logger:

    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="logs/GitHubAutomationLog.log",
            format='%(asctime)s-%(message)s',
            datefmt='%d-%b-%y %H:%M:%S',
            filemode='w'
        )
        rotate_file = logging.handlers.RotatingFileHandler(
            "logs/GitHubAutomationLog.log",
            maxBytes=1024*1024*20,
            backupCount=3
        )

        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logMessage(self, message):
        msg = f'\n{automation_title}\n{message}\n'
        logging.info(msg)

    @staticmethod
    def logValidation(self, actual, expected, field_name):
        msg = f'\n{automation_title}\nValidate field: {field_name}\nExpected: {expected}\nActual: {actual}'
        logging.info(msg)
