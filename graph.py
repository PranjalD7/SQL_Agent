from langgraph.graph import END, StateGraph, START
from nodes import *
from tools import list_tables_tool
from langgraph.checkpoint.memory import MemorySaver


# Define a new graph
workflow = StateGraph(State)

#register the nodes to the workflow graph
workflow.add_node("first_tool_call", first_tool_call)
workflow.add_node("list_tables_tool", create_tool_node_with_fallback([list_tables_tool]))
workflow.add_node("get_schema_tool", create_tool_node_with_fallback([get_schema_tool]))
workflow.add_node("model_get_schema",lambda state: {"messages": [model_get_schema.invoke(state["messages"])],},)
workflow.add_node("query_gen", query_gen_node)
workflow.add_node("human_approval", human_approval)
workflow.add_node("correct_query", model_check_query)
workflow.add_node("output_gen_node", output_gen_node)

#define the graph edges to create the graph flow
workflow.add_edge(START, "first_tool_call")
workflow.add_edge("first_tool_call", "list_tables_tool")
workflow.add_edge("list_tables_tool", "model_get_schema")
workflow.add_edge("model_get_schema", "get_schema_tool")
workflow.add_edge("get_schema_tool", "query_gen")
workflow.add_edge("query_gen", "correct_query")
workflow.add_edge("correct_query", "human_approval")
workflow.add_edge("output_gen_node", END)

#initialize thread level memory persistence for the whole flow
checkpointer = MemorySaver()

#compile the graph
app = workflow.compile(checkpointer=checkpointer)




