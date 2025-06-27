from core.classifier import classify_ticket
from agents.technical_support_agent import TechnicalSupportAgent
from agents.billing_agent import BillingAgent
from agents.product_info_agent import ProductInfoAgent
from agents.escalation_manager import EscalationManager

class Dispatcher:
    def __init__(self):
        self.agents = {
            "technical": TechnicalSupportAgent(),
            "billing": BillingAgent(),
            "product": ProductInfoAgent(),
            "escalation": EscalationManager()
        }

    def handle_ticket(self, ticket):
        category = classify_ticket(ticket)
        agent = self.agents.get(category)
        return agent.handle(ticket)
