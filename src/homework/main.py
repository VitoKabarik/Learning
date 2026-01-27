import logging
import os
from homework.logger import return_path


root_logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                    filename=os.path.join(return_path(), 'general.log'),
                    filemode='w', encoding='utf-8')
