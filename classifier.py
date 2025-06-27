def classify_ticket(ticket):
    ticket_lower = ticket.lower()
    if "crash" in ticket_lower or "error" in ticket_lower:
        return "technical"
    elif "bill" in ticket_lower or "charge" in ticket_lower:
        return "billing"
    elif "feature" in ticket_lower or "price" in ticket_lower:
        return "product"
    elif "angry" in ticket_lower or "unresolved" in ticket_lower:
        return "escalation"
    return "product"
