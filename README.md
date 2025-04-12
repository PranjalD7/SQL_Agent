# SQL_Agent
A  custom SQL agent built using Langgraph that can query a database to perform actions on it and has a human in the loop mechanism which always asks the user for approval or feedback to fix the query before executing it.


## Features

- Natural language to SQL query generation using LLM
- Automatic schema introspection
- Built-in SQL validation (common mistake checks)
- Human approval loop before executing the query
- Error handling and retry mechanism
- Streamlit-based interactive UI

## Tech Stack

- LangGraph
- LangChain
- Streamlit
- PostgreSQL
- OpenAI / Any LLM backend
- Python


##Running the Project

1. Install Requirements
	pip install -r requirements.txt

2. Set your environment variables for database and LLM access

3. Start the streamlit app
	streamlit run streamlit_app.py

	


