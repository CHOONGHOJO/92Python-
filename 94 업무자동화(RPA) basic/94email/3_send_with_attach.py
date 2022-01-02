import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg['From'] = EMAIL_ADDRESS # 보내는 사람
msg['To'] = 'cjoe731@gmail.com' # 받는 사람
msg.set_content("다운로드 하세요")

# 첨부 파일 등록
# msg.add_attachment()
with open("../chapter.png", "rb") as f:
  msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("../pandas 1.3.5 documentation.pdf", "rb") as f:
  msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("../score.xlsx", "rb") as f:
  msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
  smtp.ehlo() # 연결이 잘 수립되는지 확인
  smtp.starttls() # 모든 내용이 암호화 되어 전송
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
  smtp.send_message(msg)
