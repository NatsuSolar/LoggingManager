"""LoggingManager Management"""
import logging.config

# NOTE: (Aoi, NatusSolar) Logger setting for this module
# logging.basicConfig(level=logging.DEBUG)
# test_logger = logging.getLogger('__name__')
# test_logger.setLevel(logging.CRITICAL)
# sh = logging.StreamHandler()
# test_logger.addHandler(sh)
# test_logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# test_logger.propagate = True
# print(test_logger.isEnabledFor(logging.DEBUG))

# NOTE: (Aoi, NatusSolar) For realization of fool proof
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


def main():
    """main"""

    lll = LoggingManager().logger_maker(log_lv='deb', logger_name='logger-1.d.f')
    lll.debug('mee')
    lll.error('daddy')
    lll.info('mommy  %s %s ' % ('test', 'test2'))
    d = {'aaa': 'dadaddd', 'aaaa': 789}
    lll.critical('fafa: %(aaa)s,%(aaaa)s' % d)
    lll.critical(f'fafa: {d["aaa"]},{d["aaaa"]},{        d["aaaa"]=   }')
    # test_logger.info('4XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


if __name__ == '__main__':
    main()
