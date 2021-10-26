from dataclasses import dataclass

from dotenv import dotenv_values


@dataclass
class TgBot:
    token: str


def load_config():
    config = dotenv_values('.env')
    return TgBot(
        token=config.get('TOKEN')
    )