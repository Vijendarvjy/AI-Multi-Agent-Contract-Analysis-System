from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def analyze_finance(clause: str):
    prompt = f"""
    Analyze financial obligations, liabilities, and payment risks.

    Clause:
    {clause}
    """
    return llm.invoke(prompt).content
