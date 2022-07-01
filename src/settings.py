from typing import Optional

from pydantic_settings import BaseSettingsModel

class Settings(BaseSettingsModel):
    grpc_port: Optional[str] = "[::]:5000"
    app_transport_port: Optional[str]

    class Config:
        env_prefix = 'APP'
