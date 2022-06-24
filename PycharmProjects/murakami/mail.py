


SERVER = "pop.gmail.com"
USER  = ""
PASSWORD = ""

import imaplib
import base64
email_user =""
email_pass = ""

M = imaplib.IMAP4_SSL(SERVER, 993)
M.login(email_user, email_pass)
M.select()




typ, message_numbers = M.search(None, 'ALL')  # change variable name, and use new name in for loop

num =  message_numbers[0].split()[0]
typ, data = M.fetch(num, '(RFC822)')
# num1 = base64.b64decode(num)
print(data[0][1])


M.close()
M.logout()
