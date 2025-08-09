
---

## **class04/notes.md**
```markdown
# Class 04 — Detailed Notes

## 1. Topic: Output Types (`output_type` Parameter)

### What is it?
By default, an agent's output is just a string (plain text).  
If we need structured, typed output, we can define a Python type and set it as the `output_type` in our `Agent` definition.

### Supported Output Types
- **Dataclasses** (Python's built-in)
- **Pydantic models** (v2+)
- **Lists** and `TypedDict`
- Any type that works with `pydantic.TypeAdapter`

---

## 2. Why Use Output Types?
- **Validation**: Ensures the output matches the required format.
- **Parsing**: Makes it easier to consume results in applications.
- **Integration**: Ideal when the AI result needs to be stored in a database or passed to another system.

---

## 3. How It Works
1. Define your output type (e.g., dataclass).
2. Pass it to the `output_type` parameter of `Agent`.
3. The agent will return the response in that structured form.

---

## 4. Code Example

------> teacher.py
