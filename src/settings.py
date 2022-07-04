from typing import Optional

from pydantic_settings import BaseSettingsModel

class TransportSettings(BaseSettingsModel):
    port: Optional[str] = "[::]:5000"

class AppSettings(BaseSettingsModel):
    transport: TransportSettings
    
    class Config:
        env_prefix = 'APP'
