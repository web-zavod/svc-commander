from typing import Optional

from pydantic import BaseSettings, Field

class RepositorySettings(BaseSettings):
    user: str = "postgres"
    password: str = "passeord"
    database: str = "pgdb"

class Settings(BaseSettings):
    app_transport_port: Optional[str] = Field(..., env='APP_TRANSPORT_PORT')

    class Config:
        env_prefix = ''
        env_file = '.env'
        env_file_encoding = 'utf-8'