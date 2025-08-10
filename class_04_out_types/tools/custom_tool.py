
# from agents import function_tool

# @function_tool
# def add(n1: int, n2: int) -> str:
#     """
#     Description:
#         Adds two integers together.

#     Args:
#         n1 (int): The first integer to add.
#         n2 (int): The second integer to add.

#     Returns:
#         str: A message containing the sum of n1 and n2.
#     """
#     print("====> Tool is called <====")
#     return f"Your Answer is: {n1 + n2}"


# @function_tool
# def subtract(n1: int, n2: int) -> str:
#     """
#     Description:
#         Subtracts the second integer from the first.

#     Args:
#         n1 (int): The number from which n2 will be subtracted.
#         n2 (int): The number to subtract from n1.

#     Returns:
#         str: A message containing the difference of n1 and n2.
#     """
#     print("====> Tool is called <====")
#     return f"Your Answer is: {n1 - n2}"


# @function_tool
# def multiply(n1: int, n2: int) -> str:
#     """
#     Description:
#         Multiplies two integers together.

#     Args:
#         n1 (int): The first integer to multiply.
#         n2 (int): The second integer to multiply.

#     Returns:
#         str: A message containing the product of n1 and n2.
#     """
#     print("====> Tool is called <====")
#     return f"Your Answer is: {n1 * n2}"


from agents import function_tool , FunctionTool , RunContextWrapper
from pydantic import BaseModel

class MyTool(BaseModel):
    n1: int
    n2: int

async def add_function(ctx: RunContextWrapper, args):
    obj = MyTool.model_validate_json(args)
    return f"your answer is: {obj.n1 + obj.n2}"

add = FunctionTool(
    name="add",
    description="Adds two numbers",
    params_json_schema=MyTool.model_json_schema(),
    on_invoke_tool= add_function
)


@function_tool
async def add(n1: int, n2: int):
    """
    Adds two integers together.
    args: 
        n1: int
        n2: int
    returns:
        AddResult
    """
    print("====> Tool is called <====")
    return f"your answer is: {n1 + n2}"

@function_tool
async def subtract(n1: int, n2: int):
    """
    Subtracts the second integer from the first.
    args: 
        n1: int
        n2: int
    returns:
        SubtractResult
    """
    print("====> Tool is called <====")
    return f"your answer is: {n1 - n2}"

@function_tool
async def multiply(n1: int, n2: int) :
    """
    Multiplies two integers together.
    args: 
        n1: int
        n2: int
    returns:
        MultiplyResult
    """
    print("====> Tool is called <====")
    return f"your answer is: {n1 * n2}"
