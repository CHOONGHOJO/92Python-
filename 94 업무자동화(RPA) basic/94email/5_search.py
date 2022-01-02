from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).lologin(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:

  # 잔체 메일 다 가져오기
  # for msg in mailbox.fetch(limit=5, reverse=True):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 읽지 않은 메일  가져오기
  # for msg in mailbox.fetch('(UNSEEN)'):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 특정인이 보낸  메일  가져오기
  # for msg in mailbox.fetch('(FROM nadocoding@gmail.com, limit=3, reverse=True)'):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 어떤 글자를 포함하는 메일 (제목, 본문)  가져오기
    # 작은 따옴표로 먼저 감싸고, 실제 text(test, mail) 부분은 큰 따옴표로 감싸 준다
  # for msg in mailbox.fetch('(TEXT "test mail")'):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 어떤 글자를 포함하는 메일 (제목만)  가져오기
  # for msg in mailbox.fetch('(SUBJECT "test mail")'):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 읽지 않은 메일 (한글포함) 모두 가져와서
  # for msg in mailbox.fetch(limit=5, reverse=True):
  #   if "테스트" in msg.suject: # 제목이 '테스트' 인것 가져오기
  #     print("[{}] {}".format(msg.from_, msg.subject))

  # 특정 날자 이후의 메일  가져오기
  # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 특정 날자 이후에 온 메일  가져오기
  # for msg in mailbox.fetch('(ON 07-Nov-2020)', reverse=True, limit=5):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 2 가지 이상의 조건을 모두 만족하는 메일 ( and 조건)
  # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail" UNSEEN)', reverse=True, limit=5):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 2 가지 이상의 조건중 하나라도 모두 만족하는 메일 (or 조건)
  for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail" UNSEEN)', reverse=True, limit=5):
    print("[{}] {}".format(msg.from_, msg.subject))