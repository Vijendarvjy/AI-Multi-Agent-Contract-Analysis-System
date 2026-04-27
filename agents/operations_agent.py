from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def analyze_operations(clause: str):
    prompt = f"""
    Analyze operational risks and execution challenges.

    Clause:
    {clause}
    """
    return llm.invoke(prompt).content
