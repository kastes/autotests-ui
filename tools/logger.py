import logging


_logger: dict[str, logging.Logger] = dict()


def get_logger(name: str) -> logging.Logger:
    if _logger.get(name, None):
        return _logger[name]

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    format_str = "%(levelname)s | %(asctime)s | %(name)s:%(filename)s:%(lineno)d | %(message)s"

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(format_str)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)
    _logger[name] = logger

    return _logger[name]
