# File: app/agent_executor.py
# Purpose: Create and run LangChain Agent using RetrievalQA tool

from langchain.agents import Tool, initialize_agent, AgentType

def build_agent(qa_chain):
    """
    Create a LangChain agent using the QA chain as a tool.
    """
    tools = [
        Tool(
            name="LegalRetriever",
            func=qa_chain.run,
            description="Use this to answer legal and compliance questions from contracts"
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=qa_chain.llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent

def run_agent(agent, query: str):
    """
    Run agent on a user query.
    """
    return agent.run(query)
