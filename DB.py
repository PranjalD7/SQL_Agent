from langchain_community.utilities import SQLDatabase

#connection details dictionary
conndetails={
                'db_type':'postgresql',
                'driver':'psycopg2',
                'username':'postgres',
                'host':'',
                'password': '',
                'port': '',
                'database': 'postgres',
              
            }

#uri for the database
postgres_uri = (
                    f"postgresql+{conndetails['driver']}://"
                    f"{conndetails['username']}:{conndetails['password']}@"
                    f"{conndetails['host']}:{conndetails['port']}/"
                    f"{conndetails['database']}"
                )




#creating a database object to be used by the agents to interact with the postgres database
db_object= SQLDatabase.from_uri(postgres_uri)