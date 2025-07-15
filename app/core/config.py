from typing import Literal, Annotated
from pydantic import (
    Field,
    computed_field,
    AnyUrl,
    PostgresDsn,
    BeforeValidator
)
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl

# Auxiliary function
from app.core.validators import parse_cors

# Environment Configuration
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = '.env',
        env_file_encoding = 'utf-8',
        extra = 'ignore',
        env_ignore_empty = True
    )
    
    # Attributes
    DOMAIN: str = 'localhost'
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # CORS
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = Field(default_factory = list)
    
    # PostgreSQL
    POSTGRESQL_USERNAME: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_SERVER: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DATABASE: str
    
    # Computed fields
    @computed_field
    @property
    def server_host(self) -> str:
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"
        
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRESQL_USERNAME,
            password=self.POSTGRESQL_PASSWORD,
            host=self.POSTGRESQL_SERVER,
            port=self.POSTGRESQL_PORT,
            path=self.POSTGRESQL_DATABASE
        )