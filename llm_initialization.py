from langchain_openai import ChatOpenAI

#initialize the llm to be used by the agents
#you can use any llm provider here, you just have to change the initialization function accordingly
llm=ChatOpenAI(model="gpt-4o-mini",api_key="")