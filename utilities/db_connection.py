import yaml
from sqlalchemy import create_engine

_engine = None

def get_engine():
    global _engine

    if _engine is None:

        with open("config/db_config.yaml") as file:
            config = yaml.safe_load(file)

        db = config["database"]

        connection_string = (
            f"mysql+pymysql://"
            f"{db['user']}:{db['password']}"
            f"@{db['host']}:{db['port']}"
            f"/{db['database']}"
        )

        _engine = create_engine(
            connection_string
        )

    return _engine
