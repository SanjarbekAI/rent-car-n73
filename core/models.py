"""
All tables queries
"""

users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id         BIGSERIAL PRIMARY KEY,
            username   VARCHAR(255) NOT NULL,
            password   VARCHAR(128) NOT NULL,
            is_login   BOOLEAN   DEFAULT FALSE,
            is_active  BOOLEAN   DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """

