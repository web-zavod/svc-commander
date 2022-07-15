from typing import Optional

from pydantic_settings import BaseSettingsModel, load_settings


class TransportSettings(BaseSettingsModel):
    port: Optional[str] = "[::]:5000"

class RepositorySettings(BaseSettingsModel):
    user: Optional[str] = "postgres"
    password: Optional[str] = "password"
    host: Optional[str] = "localhost"
    database: Optional[str] = "pgdb"

class AppSettings(BaseSettingsModel):
    transport: TransportSettings
    repository: RepositorySettings = RepositorySettings()

    class Config:
        env_prefix = 'APP'

    @classmethod
    def load(cls):
        return load_settings(cls=cls, load_env=True)