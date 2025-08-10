
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


from agents import function_tool

@function_tool
def add(n1: int, n2: int) -> str:
    """
    Adds two integers together.
    """
    print("====> Tool is called <====")
    return f"Your Answer is: {n1 + n2}"

@function_tool
def subtract(n1: int, n2: int) -> str:
    """
    Subtracts the second integer from the first.
    """
    print("====> Tool is called <====")
    return f"Your Answer is: {n1 - n2}"

@function_tool
def multiply(n1: int, n2: int) -> str:
    """
    Multiplies two integers together.
    """
    print("====> Tool is called <====")
    return f"Your Answer is: {n1 * n2}"
