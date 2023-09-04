"""LoggingManager Management"""
import logging.config

# NOTE: (Aoi Natsuki, blautinte8@gmail.com)  Logger setting for this module
# logging.basicConfig(level=logging.DEBUG)
# test_logger = logging.getLogger('__name__')
# test_logger.setLevel(logging.CRITICAL)
# sh = logging.StreamHandler()
# test_logger.addHandler(sh)
# test_logger.debug('test: 1XXXXX')
# test_logger.propagate = True
# print(test_logger.isEnabledFor(logging.DEBUG))

# NOTE: (Aoi Natsuki, blautinte8@gmail.com) For realization of foolproof
_lv_kinds = {'CRITICAL': logging.CRITICAL,
             'CRI': logging.CRITICAL,
             'FATAL': logging.CRITICAL,
             'ERROR': logging.ERROR,
             'ERO': logging.ERROR,
             'ERR': logging.ERROR,
             'WARNING': logging.WARNING,
             'WARN': logging.WARNING,
             'WAN': logging.WARNING,
             'INFO': logging.INFO,
             'INF': logging.INFO,
             'DEBUG': logging.DEBUG,
             'DEB': logging.DEBUG,
             }


def logfile_initializer(oneline=True, detail=True,
                        online_path='./logging_oneline.log',
                        detail_path='./logging.log'):
    """log_initializer"""
    if oneline:
        with open(online_path, 'w') as logfile_oneline:
            logfile_oneline.write('')
    else:
        print('Initialization toward oneline-logfile is not done')

    if detail:
        with open(detail_path, 'w') as logfile_detail:
            logfile_detail.write('')
    else:
        print('Initialization toward detail-logfile is not done')


class LoggingBaseFilter(logging.Filter):
    """LoggingBaseFilter"""

    def __init__(self, word: str):
        super().__init__()
        self.word = word

    def filter(self, record):
        """
        Filtering word in log massage.
        :param record: LogRecord
        :return: boolean
        """
        log_massage = record.getMessage()
        return self.word not in log_massage


class LoggingManager(object):
    """
    LoggingManager
    """

    def __init__(self, format_ini='logging.ini'):
        self.format_ini = format_ini
        logging.config.fileConfig(self.format_ini)

    def logger_maker(self, log_lv: str = 'INFO', logger_name: str = __name__):
        """logger_maker"""
        logger = logging.getLogger(logger_name)
        logger.setLevel(_lv_kinds[log_lv.upper()])
        return logger


logger = LoggingManager()
logger = logger.logger_maker(log_lv='Debug', logger_name='logger-1.src.main')


def main():
    """
    main()

    Code and Module Test space.

    """

    test_l = LoggingManager().logger_maker(log_lv='deb', logger_name='logger-1.LoggingManager.LoggingManager')

    test_l.debug('Look at Me')
    test_l.error('Daddy')
    test_l.critical('Mommy  %s %s ' % ('Hey?', 'Hello---!'))
    d = {'a': 'AprilFoolProof', 'b': 20240401}
    test_l.info('Screaming will get into illusion in: %(a)s,%(b)s' % d)
    test_l.info(f'Screaming gets into illusion in: {d["a"]},{d["b"]},{        d["b"]=   }')
    # test_logger.info('test: 4XXXXX')

    logger.debug('test')
    a = 15
    x = 10 * a
    logger.info(f"When a={a} and x=10*a, x={x}")


if __name__ == '__main__':
    main()
