import os

from enum import Enum
from pathlib import Path

from pydantic import BaseModel, DirectoryPath, EmailStr, FilePath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath
    image_jpg_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # если определена переменная окружения ENV_FILE, берём её значение. Иначе .env
        env_file=os.getenv("ENV_FILE", ".test.env"),
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    test_user: TestUser
    test_data: TestData
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> "Settings":
        videos_dir: Path = DirectoryPath("./artifacts/videos")
        tracing_dir: Path = DirectoryPath("./artifacts/tracing")
        allure_results_dir: Path = DirectoryPath("./allure-results")
        browser_state_file: Path = FilePath("browser-state.json")

        # создаём каталоги и файлы если они не существуют
        videos_dir.mkdir(exist_ok=True, parents=True)
        tracing_dir.mkdir(exist_ok=True, parents=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file,
        )  # type: ignore[call-arg] # mypy выдаёт предупреждение :(

    def get_base_url(self) -> str:
        return f"{self.app_url}/"


settings = Settings.initialize()
