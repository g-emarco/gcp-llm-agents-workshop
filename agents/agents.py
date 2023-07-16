from langchain.llms import VertexAI
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.agents import AgentType

from langchain import SerpAPIWrapper


def get_google_search(query: str):
    """Searches on Google."""
    search = SerpAPIWrapper()
    res = search.run(f"{query}")
    return res


def get_search_agent() -> AgentExecutor:
    llm = VertexAI(temperature=0, verbose=True, max_output_tokens=1000)

    tools_for_agent = [
        Tool(
            name="GoogleSearch",
            func=get_google_search,
            description="useful for when you need get a google search result",
        ),
    ]

    agent = initialize_agent(
        tools_for_agent,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    return agent
