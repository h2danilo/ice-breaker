from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as LinkedinLookupAgent

def ice_break_with(name: str) -> str:
    linkedin_username = LinkedinLookupAgent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data})
    print(res)

if __name__ == "__main__":
    load_dotenv()
    print("Ice breaker enter")
    ice_break_with(name="Danilo Valim")






