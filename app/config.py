import os
import random
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


# 6 digits random secrets are secure enough,
# I don't believe someone could brute-force them
def generate_random_secret():
    return "".join(random.choices("1234567890", k=6))


class Settings:
    """
    Retrieves environment variables and sets default values if not provided,
    defining various settings such as JWT secret key, PostgreSQL connection details
    (user, password, server, port, database), and a constructed DATABASE_URL string.

    Attributes:
        JWT_SECRET_KEY (str|bytes): Generated as a default value when not provided
            by environment variable `JWT_SECRET_KEY`.
        CHEF_USERNAME (str): Assigned a default value of "chef" if no environment
            variable named "CHEF_USERNAME" is set.
        JWT_VERIFY_SIGNATURE (str|None): Set to the value obtained from the
            environment variable `JWT_VERIFY_SIGNATURE`. If not present, it defaults
            to None. This variable likely determines whether or not to verify the
            signature in JSON Web Tokens (JWTs).
        POSTGRES_USER (str): Set to a default value of "admin" if the environment
            variable "POSTGRES_USER" is not provided, otherwise it takes the value
            of the provided environment variable.
        POSTGRES_PASSWORD (str): Set by default to a hardcoded string "password".
            It can be overridden by setting the environment variable `POSTGRES_PASSWORD`.
        POSTGRES_SERVER (str): Set to the value of the environment variable
            `POSTGRES_SERVER`. If this variable is not defined, it defaults to "localhost".
        POSTGRES_PORT (str): Used to store the port number for PostgreSQL database
            connection. It defaults to 5432 if not provided as environment variable.
        POSTGRES_DB (str): Assigned a value that is retrieved from an environment
            variable named "POSTGRES_DB". If this variable is not set, it defaults
            to the string "restaurant".
        DATABASE_URL (str): Generated based on environment variables. It represents
            a PostgreSQL connection string, formatted as "postgresql://user:password@host:port/dbname",
            with default values for user, password, host, port, and database name
            if environment variables are not provided.

    """
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", generate_random_secret())
    CHEF_USERNAME = os.getenv("CHEF_USERNAME", "chef")

    # someone needs to remember to set this variable to True in env variables
    JWT_VERIFY_SIGNATURE = os.getenv("JWT_VERIFY_SIGNATURE")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "restaurant")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
