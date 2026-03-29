import configparser
from pathlib import Path
from typing import Dict, Optional

TITLES: Dict[str, str] = {
    "msg-interval": "Интервал уведомлений [минуты]"
}

class UserSettings:
    
    def __init__(self, user_id: int | str, base_dir: str = "config") -> None:
        self.user_id = str(user_id)
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

        self.path = self.base_dir / f"{self.user_id}.ini"
        self.config = configparser.ConfigParser()

        if self.path.exists():
            self.config.read(self.path, encoding="utf-8")
        else:
            self.config["Settings"] = {
                "msg-interval": "30"
            }
            self._save()

    def _save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            self.config.write(f)

    def reload(self) -> None:
        self.config.read(self.path, encoding="utf-8")


    def get(self, section: str, key: str, fallback: Optional[str] = None) -> Optional[str]:
        return self.config.get(section, key, fallback=fallback)

    def get_int(self, section: str, key: str, fallback: Optional[int] = None) -> Optional[int]:
        try:
            return self.config.getint(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return fallback


    def set(self, section: str, key: str, value: str) -> None:
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        self._save()


    def get_msg_interval(self, fallback: Optional[int] = None) -> Optional[int]:
        return self.get_int("Settings", "msg-interval", fallback=fallback)

    def set_msg_interval(self, minutes: int) -> None:
        self.set("Settings", "msg-interval", str(minutes))


    def all(self, use_titles: bool = True) -> Dict[str, str]:
        result: Dict[str, str] = {}
        for section in self.config.sections():
            for key, value in self.config[section].items():
                name = TITLES.get(key, key) if use_titles else key
                result[name] = value
        return result
