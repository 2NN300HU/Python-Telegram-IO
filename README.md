# Python Telegram IO
* Python module for using Telegram as native IO
* Requires little effort to change your project's IO
* Just Create TelegramIO object ( e.g. teleio ) and add `"your-TelegramIO-object-name".` to your code's print() and input() ( e.g. `teleio.print("message what you want")` )
* It works same as python native IO does

# Required modules
* python-telegram-bot

# How to use
* First, you have to Create TelegramIO object
`teleio = TelegramIO(chatid,token)`

* To send message
`teleio.print("message")`

* To get input from Telegram. It just works as python native input() does
`teleio.input("message")`

* To send picture
`teleio.picture("url")`
