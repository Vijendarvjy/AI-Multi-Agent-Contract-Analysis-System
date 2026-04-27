from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def classify_contract(text: str):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        Classify the following contract into one of these categories:
        NDA, Employment, Vendor, Lease, Service, Partnership.

        Contract:
        {text}

        Return only the category.
        """
    )

    chain = prompt | llm
    return chain.invoke({"text": text[:4000]}).content.strip()
