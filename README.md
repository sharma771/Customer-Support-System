# Customer-Support-System
customer_support_system/
│
├── agents/
│   ├── __init__.py
│   ├── billing_agent.py
│   ├── technical_support_agent.py
│   ├── product_info_agent.py
│   └── escalation_manager.py
│
├── core/
│   ├── __init__.py
│   ├── classifier.py
│   ├── dispatcher.py
│   ├── knowledge_base.py
│   └── ticket.py
│
├── interfaces/
│   ├── __init__.py
│   ├── email_handler.py
│   ├── chat_interface.py
│   ├── ticket_system.py
│   └── analytics.py
│
├── data/
│   ├── knowledge_base.json
│   ├── tickets.db
│   └── logs/
│       └── responses.log
│
├── config/
│   ├── agent_config.yaml
│   └── settings.yaml
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── sentiment.py  # (optional feature)
│   └── language_utils.py  # (optional multi-language)
│
├── tests/
│   ├── test_routing.py
│   └── test_agents.py
│
├── main.py
├── README.md
└── requirements.txt

# Customer Support System (CrewAI-based)

## Features
- Ticket classification via NLP
- Specialized support agents
- Escalation manager logic
- Email/chat/ticket system integration
- Optional sentiment analysis, multilingual support

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
