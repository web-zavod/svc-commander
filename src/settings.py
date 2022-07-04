from typing import Optional

from pydantic_settings import BaseSettingsModel, load_settings


class TransportSettings(BaseSettingsModel):
    port: Optional[str] = "[::]:5000"

class AppSettings(BaseSettingsModel):
    transport: TransportSettings

    class Config:
        env_prefix = 'APP'

    @classmethod
    def load(cls):
        return load_settings(cls=cls, load_env=True)