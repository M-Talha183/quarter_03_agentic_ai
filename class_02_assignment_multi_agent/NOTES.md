✅ Class 2 - Topic 1: Running Agents using Runner
In this lesson, we explored how to run agents using the Runner class from the agents module. This is a crucial step when building intelligent applications using Agentic AI frameworks.

🧠 What is Runner?
The Runner is a utility class that provides different methods to execute an agent. It simplifies the process of interacting with the agent and handling outputs.

🔁 Methods to Run an Agent
You can run an agent in three different ways:

Runner.run()

Async method.

Returns a RunResult.

Example use: for awaitable environments like Jupyter Notebooks or async functions.

Runner.run_sync()

Synchronous method.

Internally runs Runner.run() using an event loop.

Good for use in standard Python scripts where async is not available.

Runner.run_streamed()

Async and returns a RunResultStreaming.

The agent is run in streaming mode, providing real-time updates of the response.

✅ Example Code: Using Runner.run()

from agents import Agent, Runner

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant"
    )

    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)

# Expected Output:
# Code within the code,
# Functions calling themselves,
# Infinite loop's dance
📄 Additional Notes:
The RunResult object contains the final output and other details.

For real-time interaction, Runner.run_streamed() is preferred.

For blocking environments, use Runner.run_sync().

:

🌀 The Agent Loop
When using the Runner.run() method in the Agentic AI framework, execution flows through a structured loop. This loop is responsible for handling how agents respond, hand off tasks, and invoke tools.

🔁 Loop Process
Here’s how the agent loop works:

Start the Loop:
You call the run() method with a starting agent and an initial input (either a string message or a structured list of input items from OpenAI Responses API).

Run Agent:
The system sends the current input to the current agent's LLM.

LLM Output:
The agent (via LLM) generates an output.

Check Output Type:

If the output includes final_output, the loop ends and the result is returned.

If the output includes a handoff to another agent, the loop continues with the new agent and new input.

If there are tool calls, the tools are executed, results are appended, and the loop continues.

Max Turns Rule:

If the number of steps exceeds max_turns, a MaxTurnsExceeded exception is raised and execution halts.

✅ Final Output Condition
An output is considered a final output only when:

It contains a valid text result of the desired type.

There are no tool calls present in the response.

.

💬 Sessions – Built-in Memory for Agents
The Sessions API allows you to maintain multi-turn memory across multiple calls to the agent—perfect for chatbots, assistants, or conversational AI agents.

🚀 Why Use Sessions?
Without sessions:

You have to manually track history using .to_input_list() and append previous messages.

With sessions:

The agent automatically remembers previous interactions based on a session ID.

✅ Key Benefits
Stores conversation history automatically.

Works out-of-the-box with runner.run() or await agent.arun() using a session_id.

Supports use cases like:

Chat apps

Customer service bots

Multi-turn workflows

🛠️ Example Usage

output1 = await agent.arun("Hi", session_id="user123")
output2 = await agent.arun("What's the weather?", session_id="user123")
→ Here, agent remembers the first message when processing the second, because both use the same session_id.



Understanding Results in OpenAI Agents SDK
When you run an agent using the Runner class, the result you get contains more than just a final answer. It includes rich metadata, reasoning paths, tool calls, and much more.

🧾 Types of Results
Method Called	Returned Object
Runner.run()	RunResult
Runner.run_sync()	RunResult
Runner.run_streamed()	RunResultStreaming

Both RunResult and RunResultStreaming inherit from RunResultBase, where most useful attributes live.

🔚 final_output – The Final Answer
The most important result is:

result.final_output
Type: Any

Could be:

A str (if no output type was defined for the last agent)

A structured object (if output_type was defined)

⚠️ Due to handoffs, the SDK cannot guarantee a fixed output type statically.

🔁 to_input_list() – Preparing for the Next Turn
This method prepares the input list for continuing a conversation:

next_inputs = result.to_input_list()
Useful when:

You want to carry forward the history to the next agent run.

You're building multi-turn chat loops.

👤 last_agent
Stores the final agent that handled the input:

result.last_agent
Helpful when:

You start with a triage agent that hands off to specialists.

You want to resume conversation with the same agent later.

🆕 new_items – What Happened Internally?
This gives you all new items generated during the agent loop. Types include:

Type	Meaning
MessageOutputItem	An LLM message
HandoffCallItem	The LLM requested a handoff
HandoffOutputItem	Another agent took over
ToolCallItem	A tool was invoked
ToolCallOutputItem	A tool returned a result
ReasoningItem	LLM generated reasoning or thinking process

Each item wraps the raw result, plus useful metadata.

🛡️ Guardrails
Check these for validation results:

input_guardrail_results

output_guardrail_results

These may include warnings, block reasons, or logs for debugging.

⚙️ Other Fields
Field	Purpose
raw_responses	Raw LLM responses, useful for logging
input	The original input provided

: