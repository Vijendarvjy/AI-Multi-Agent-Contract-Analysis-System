from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def analyze_compliance(clause: str):
    prompt = f"""
    Review this clause for regulatory and compliance risks.

    Clause:
    {clause}
    """
    return llm.invoke(prompt).content
