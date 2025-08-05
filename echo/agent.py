import asyncio
from collections.abc import AsyncGenerator

from acp_sdk.models import Message
from acp_sdk.server import Context, RunYield, RunYieldResume, Server

server = Server()

@server.agent()
async def echo(
    input: list[Message], context: Context
) -> AsyncGenerator[RunYield, RunYieldResume]:
    """Echoes everything"""
    for message in input:
        # Simulate internal thought process
        await asyncio.sleep(0.5)
        yield {"thought": "Echoing back the message..."}
        await asyncio.sleep(0.5)
        # Echo the incoming message
        yield message

server.run(port=8000)

# uv run agent.py 