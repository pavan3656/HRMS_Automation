import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        log_dir = "/Users/pavankumat/PycharmProjects/NOPEcommerceAPP/Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Ensure Logs folder exists

        log_file = os.path.join(log_dir, "automation2.log")
        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
