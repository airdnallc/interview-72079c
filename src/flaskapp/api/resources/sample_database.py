from flask_restful import Resource
from flaskapp.extensions import db # db is sqlalchemy db management
from sqlalchemy.sql import text # for text queries.  We're not doing much with the ORM for microservices, we use
# liquibase instead of (sqlalchemy ORM + alembic)

class SampleDatabaseResource(Resource):
    """Sample database access resource"""

    def get(self): # generally, name this after the type of rest call.
        """gets database info"""
        return db_count()

def db_count():
    main_result = (
        db.get_engine()
            .execute(
                text('''select count(*) from city as city_count''')
            )
            .fetchone()
    )

    return f'there are {main_result[0]} cities in main db'