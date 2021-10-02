import pathlib

from pydantic import BaseSettings, Field


# https://pydantic-docs.helpmanual.io/usage/settings/#dotenv-env-support
class Settings(BaseSettings):
    telegram_token: str = Field()

    root_path: pathlib.Path = Field(default=pathlib.Path(__file__).parents[1])

    class Config:
        env_file = '.env'
