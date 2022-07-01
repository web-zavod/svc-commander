from typing import Optional

from pydantic_settings import BaseSettingsModel

class Settings(BaseSettingsModel):
    app_transport_port: Optional[str] = "[::]:5000"

    class Config:
        env_prefix = 'APP'
