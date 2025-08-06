import asyncio

from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart, MessageCompletedEvent, GenericEvent


async def client() -> None:
    async with Client(base_url="http://localhost:8000") as client:
        async for event in client.run_stream(
            agent="lang_graph_greeting_agent", input=[Message(parts=[MessagePart(content="John Doe")])]
        ):
            match event:
                case MessageCompletedEvent():
                    print("\n✅ Final response:", event.message)
                case GenericEvent():
                    print("ℹ️ ", event.generic.update)


if __name__ == "__main__":
    asyncio.run(client())