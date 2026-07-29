from pathlib import Path
from typing import Self

from pydantic import FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    base_url: str
    headless: bool
    standard_user: str
    locked_user: str
    performance_user: str
    password: str
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f"{self.base_url}/"

    @classmethod
    def initialize(cls) -> Self:
        browser_state_file = Path("browser-state.json")
        browser_state_file.touch(exist_ok=True)

        return Settings(browser_state_file=browser_state_file)


settings = Settings.initialize()
