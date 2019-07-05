from configparser import ConfigParser

from pyrogram import Client


class PyroTemplate(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        config_file = f"{name}.ini"

        config = ConfigParser()
        config.read(config_file)

        super().__init__(
            name,
            bot_token=config.get(name, "bot_token"),
            workers=8,
            plugins=dict(root=f"{name}/plugins"),
            workdir="."
        )

    async def start(self):
        await super().start()
        print("PyroTemplate started")

    async def stop(self):
        await super().stop()
        print("PyroTemplate stopped")
