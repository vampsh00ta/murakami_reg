


SERVER = "pop.gmail.com"
USER  = "lilpenisp@gmail.com"
PASSWORD = "Terminator2020"

import imaplib
import base64
email_user ="lilpenisp@gmail.com"
email_pass = "Terminator2020"

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