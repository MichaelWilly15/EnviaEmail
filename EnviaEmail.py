import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Cabecalho do email
msg = MIMEMultipart()
msg['To'] = 'destino@gmail.com'
msg['From'] = 'seuemail@gmai.com'
msg['Subject'] = 'Enviando email com python'

# Colocando o texto do email
texto = MIMEText('Email com python.')
msg.attach(texto)

# Anexando um arquivo no email
arquivo = open(r'arquivo','rb')

anexo = MIMEApplication(arquivo.read(), _subtype='.extensao')
msg.attach(anexo)

# Enviando email
server = smtplib.SMTP('smtp.gmail.com', '587')
server.starttls()
server.login('seuemail@gmail.com', 'suasenha')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()