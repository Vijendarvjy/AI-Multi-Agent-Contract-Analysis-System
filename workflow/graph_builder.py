from typing import TypedDict
from langgraph.graph import StateGraph, END

from modules.classifier import classify_contract
from modules.clause_retriever import split_clauses
from modules.planner import create_review_plan
from modules.report_generator import generate_report

from agents.legal_agent import analyze_legal
from agents.compliance_agent import analyze_compliance
from agents.finance_agent import analyze_finance
from agents.operations_agent import analyze_operations


class ContractState(TypedDict):
    contract_text: str
    contract_type: str
    clauses: list
    results: dict
    final_report: str


def classify_node(state):
    state["contract_type"] = classify_contract(state["contract_text"])
    return state


def retrieve_node(state):
    state["clauses"] = split_clauses(state["contract_text"])
    return state


def analyze_node(state):
    clause_text = "\n".join(state["clauses"][:5])

    state["results"] = {
        "legal": analyze_legal(clause_text),
        "compliance": analyze_compliance(clause_text),
        "finance": analyze_finance(clause_text),
        "operations": analyze_operations(clause_text)
    }
    return state


def report_node(state):
    state["final_report"] = generate_report(state["results"])
    return state


def build_graph():
    workflow = StateGraph(ContractState)

    workflow.add_node("classify_contract", classify_node)
    workflow.add_node("retrieve_clauses", retrieve_node)
    workflow.add_node("analyze_contract", analyze_node)
    workflow.add_node("generate_report", report_node)

    workflow.set_entry_point("classify_contract")

    workflow.add_edge("classify_contract", "retrieve_clauses")
    workflow.add_edge("retrieve_clauses", "analyze_contract")
    return workflow.compile()
