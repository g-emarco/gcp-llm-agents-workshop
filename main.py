from agents.agents import get_search_agent
from dotenv import load_dotenv
from agents.utils.output_parsers import parser

load_dotenv()

if __name__ == "__main__":
    format_instructions = parser.get_format_instructions()
    prompt = f"Find Torq's Learning center and asnwer what is a torq step? \n {format_instructions}"

    agent = get_search_agent()
    res = agent.run(prompt)
    response_object = parser.parse(res)
    print(response_object)
