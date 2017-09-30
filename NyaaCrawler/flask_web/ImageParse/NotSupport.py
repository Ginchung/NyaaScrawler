import logging

class NotSupport(object):
    logging.basicConfig(
        level=logging.WARNING,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a,%Y %b %d  %H:%M:%S',
        handlers=[logging.FileHandler('Logs/NoSupportImageUrl.log', 'a', 'utf-8'), ])
    logging.getLogger("ImageHandler").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING

    def __init__(self, url):
        self.url = url

    def get(self):
        logging.warning("not Support url: " + self.url)
        return None