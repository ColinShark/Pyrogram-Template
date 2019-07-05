# Pyrogram-Template

<img src="https://i.imgur.com/JyxrStE.png" width="160" align="right">

This repository is a Template to use as a Telegram Bot built with [Pyrogram](https:////github.com/pyrogram/pyrogram).
It features [**Pyrogram Asyncio**](https://github.com/pyrogram/pyrogram/issues/181) and [**Smart Plugins**](https://docs.pyrogram.org/topics/smart-plugins);
feel free to read through the linked [documentation](https://pyrogram.org) pages to learn more about those topics.

## Requirements

* Python 3.6 or higher.
* A [Telegram API Key pair](https://docs.pyrogram.org/intro/setup#api-keys).
* A [Telegram bot token](https://t.me/BotFather).

## Run

1. `git clone https://github.com/ColinTheShark/Pyrogram-Template`, to download the source-code.
2. `cd Pyrogram-Template`, to enter the directory.
3. `pip3 install -r requirements.txt`, to install the requirements.
4. Create a new `pyrotemplate.ini` file, copy-paste the following and replace the values with your own:

    ```ini
    [pyrogram]
    api_id = 123456
    api_hash = 0123456789abcdef0123456789abcdef

    [pyrotemplate]
    bot_token = 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
    ```

5. Run with `python3 -m pyrotemplate`, stop with <kbd>CTRL + C</kbd>

## License

* Pyrogram is MIT © [Dan](https://github.com/delivrance)
* Template is WTFPL © [Colin](https://github.com/ColinTheShark)
