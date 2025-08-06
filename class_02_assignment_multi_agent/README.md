

🤖 Multi-Agent System with Handoff
This project implements a modular multi-agent architecture using the OpenAI Agents SDK and Runner. It uses a Task Manager Agent to intelligently route user input to the correct expert agent based on the task category.

🧠 Overview
The system consists of 4 agents:

Agent	Responsibility
🧩 Task Manager Agent	Receives all user inputs and classifies the task. Delegates it to the appropriate specialist agent using handoffs.
🌐 Web Developer Agent	Handles tasks related to web development including frontend/backend, deployment, and responsive design.
📱 App Developer Agent	Takes on mobile and desktop app tasks including UI/UX, performance, and cross-platform tools.
📈 Marketing Manager Agent	Manages marketing-related queries such as SEO, branding, campaigns, and analytics.

🔁 How It Works
User submits a prompt (e.g., "Build me a portfolio website").

Task Manager Agent analyzes the request.

Based on the topic, it performs a handoff to:

Web Developer Agent

App Developer Agent

Marketing Manager Agent

The selected agent processes the task and returns the final result.

✅ Example Use Case

response = await my_agent("I need an iOS and Android app for a travel blog.")
print(response.final_output)
➡️ The Task Manager detects this is an app development task and hands it off to the App Developer Agent.

🧩 Benefits
🔄 Clean separation of concerns between task routing and solving.

🎯 Domain-specific expertise embedded in each agent.

🚀 Scalable and extendable to more specialized agents.






