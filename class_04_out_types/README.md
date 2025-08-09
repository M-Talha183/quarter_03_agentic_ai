# Class 04 — Output Types & Tools

## Overview
In this class, we covered two major topics in the Agents SDK:

### 1. Output Types
By default, agents return a **string** (`str`) as their output.  
With the `output_type` parameter, you can define structured outputs using:
- Dataclasses
- Pydantic models
- Lists
- TypedDict  
This ensures consistent, validated, and easily parsed responses.

### 2. Tools
Tools let agents **take actions** such as:
- Fetching data
- Running code
- Calling APIs
- Even controlling a computer

We explored **function tools**, where a Python function is exposed to the agent for use during conversation.

**Example:**  
We built a **Math Teacher** agent with an `add()` tool that calculates sums on demand.
