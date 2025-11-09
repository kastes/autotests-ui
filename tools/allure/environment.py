import platform
import sys

from config import settings


def create_allure_environment_file() -> None:
    properties: list[str] = [f"os_info={platform.system()}"]
    properties.append(f"os_version={platform.version()}")
    properties.append(f"os_release={platform.release()}")
    properties.append(f"python={sys.version}")
    properties.extend(f"{key}={value}" for key, value in settings.model_dump().items())

    with open(settings.allure_results_dir.joinpath("environment.properties"), mode="w+", encoding="utf-8") as f:
        f.write("\n".join(properties))
