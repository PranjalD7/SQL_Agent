
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from llm_initialization import llm
from DB import db_object

#initializing sql database toolkit
toolkit = SQLDatabaseToolkit(db=db_object, llm=llm)

#getting tools for performing actions on the db
tools = toolkit.get_tools()

# tool find the tables present in the database
list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")

#tool finding the schema of the tables
get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")

# tool for executing sql queries on the database
dbtool=([next(tool for tool in tools if tool.name == "sql_db_query")])
