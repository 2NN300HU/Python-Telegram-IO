import telegram
import time

class TelegramIO:
    def __init__(self, chat_id, token):
        self.my_token = token
        self.chatid = chat_id
        self.offset = self.set_offset()

    def input(self, msg=None):
        if msg is None:
            pass
        else:
            self.print(msg)
        bot = telegram.Bot(token=self.my_token)
        while True:
            try:
                message = bot.getUpdates(offset=self.offset + 1)
                if not message:
                    time.sleep(3)
                else:
                    reply = message[-1].message.text
                    self.offset = message[-1].update_id
                    return reply
            except:
                pass

    def print(self, reply):
        bot = telegram.Bot(token=self.my_token)
        bot.sendMessage(chat_id=self.chatid, text=reply)

    def picture(self, url):
        bot = telegram.Bot(token=self.my_token)
        bot.send_photo(chat_id=self.chatid, photo=open(url, 'rb'))

    def set_offset(self):
        bot = telegram.Bot(token=self.my_token)
        message = bot.getUpdates()
        if not message:
            offset = 0
        else:
            offset = message[-1].update_id
        return offset
