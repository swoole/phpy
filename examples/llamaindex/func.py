import asyncio


def multiply(a: float, b: float = 3.13) -> float:
    """Useful for multiplying two numbers."""
    return a * b


async def main(agent, prompt):
    return await agent.run(prompt)


def run(agent, prompt):
    return asyncio.run(main(agent, prompt))
