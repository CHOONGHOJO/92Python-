# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")
# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# debug < info < warning < error < critical
# logging.debug("아, 이거 누가 짠거야~~")
# logging.info("자동화 수행준비")
# logging.warning("이 스크립트는 오래되어 실행상 문제가 될 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는 ...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다...")

# 테미날과 파일에 함께 log 남기기
import logging
from datetime import datetime

# 시간 [로그래벨] 메세지 형태로 로그 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# 로그 레밸 설정
logger.setLevel(logging.DEBUG)

# stream terminal
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# file
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20211225155901.log
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")
