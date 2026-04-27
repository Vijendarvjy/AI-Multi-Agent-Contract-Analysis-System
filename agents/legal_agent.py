from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def analyze_legal(clause: str):
    prompt = f"""
    Analyze this contract clause from a legal perspective.

    Clause:
    {clause}

    Provide:
    - Legal Risks
    - Missing Protections
    - Recommendations
    """
    return llm.invoke(prompt).content
