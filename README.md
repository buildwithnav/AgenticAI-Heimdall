# 🤖 Agentic AI for Testing Automation Workflows

A multi-agent automation framework powered by [AutoGen](https://github.com/microsoft/autogen), [Playwright](https://playwright.dev), and custom Model Coordination Protocols (MCPs), designed to simulate and manage collaborative AI agents that handle end-to-end QA and testing operations intelligently.

---

## 📘 Definitions

### 💡 What is an LLM?

A **Large Language Model (LLM)** is a type of artificial intelligence trained on vast amounts of text data to understand and generate human-like language. Examples include GPT-4, Claude, and PaLM. These models can answer questions, write code, summarize documents, and much more — making them useful as general-purpose AI tools.

---

### 🧠 What is an AI Agent?

An **AI Agent** is an LLM enhanced with tools, memory, goals, and autonomy to perform specific tasks. Unlike a raw LLM that passively responds to prompts, an agent can:

- **Plan** and decide what to do next  
- **Take actions**, such as calling APIs, executing scripts, or saving outputs  
- **Collaborate** with other tools or agents  
- **Adapt** to feedback and maintain context  

In essence, it's an LLM with a purpose.

---

### 🤝 What is Multi-Agent AI / Agentic AI?

**Multi-Agent AI** (also called **Agentic AI**) refers to a system where **multiple AI agents work together**, often with different roles or specialties, to solve complex problems collaboratively.

Instead of one agent doing everything, you get:

- **Modular roles** (e.g., "Test Designer", "Execution Agent", "Debugger")  
- **Distributed reasoning**  
- **More robust task completion** through delegation and feedback  

---

## 🔄 From LLM → AI Agent → Agentic AI

| Phase              | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **LLM**            | Prompt-based responses with limited control or memory                        |
| **Single AI Agent**| Task-oriented, stateful agent powered by an LLM, often enhanced with tools  |
| **Multi-Agent AI** | Teams of agents that coordinate, debate, validate, and execute tasks         |

---

### Why We Transitioned

| Challenge with LLMs / Single Agent    | Why Agentic AI Helps                                           |
|---------------------------------------|----------------------------------------------------------------|
| Prompt brittleness                    | Agents can retry, self-correct, and escalate                   |
| Lack of modularity                    | Each agent owns a responsibility (Test Creator, Runner, Logger)|
| Limited collaboration                 | Multi-agent chat patterns enable debate, review, and refinement|
| Poor long-running workflows           | Agentic frameworks manage turn-taking, memory, and coordination|

---

## 🛠️ Use Case: Automated Testing Workflow

Our Agentic AI system includes:

- `TestPlanningAgent`: interprets requirements, generates test strategies  
- `PlaywrightExecutorAgent`: executes tests using Playwright scripts  
- `LoggerAgent`: aggregates results, uploads logs to S3, triggers alerts  
- `FeedbackAgent`: reviews test failures and suggests improvements  

Each agent operates semi-autonomously but collaborates through a coordinator (e.g., RoundRobin or GroupChat pattern).

---

## 🔋 Technologies Used

- **AutoGen** – for multi-agent coordination and lifecycle  
- **OpenAI GPT-4o** – as the core LLM behind each agent  
- **Playwright** – browser automation framework for UI testing  
- **MCP (Model Coordination Protocols)** – orchestrate agent interactions  
- **Python Asyncio** – asynchronous execution of workflows  
- **.env + Git** – secure secret management and project versioning  

---

