from typing import Any, Dict, Optional, Awaitable
from openai.types.chat import ChatCompletion
from .context import UserSessionContext
import logging
from datetime import datetime
import asyncio

logger = logging.getLogger(__name__)

class RunHooks:
    """
    Global lifecycle hooks for tracking agent and tool execution
    """
    
    @staticmethod
    async def on_agent_start(agent_name: str, input: str, context: UserSessionContext) -> Awaitable[None]:
        """Log when an agent starts processing (async)"""
        await asyncio.sleep(0)  # Yield control to event loop
        logger.info("Agent %s started processing", agent_name)
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "agent_start",
            "agent": agent_name
        })

    @staticmethod
    async def on_agent_end(agent_name: str, context: UserSessionContext) -> Awaitable[None]:
        """Log when an agent finishes processing (async)"""
        await asyncio.sleep(0)
        logger.info("Agent %s completed processing", agent_name)
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "agent_end",
            "agent": agent_name
        })

    @staticmethod
    async def on_tool_start(tool_name: str, context: UserSessionContext) -> Awaitable[None]:
        """Log when a tool starts execution (async)"""
        await asyncio.sleep(0)
        logger.info("Tool %s started", tool_name)
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "tool_start",
            "tool": tool_name
        })

    @staticmethod
    async def on_tool_end(tool_name: str, context: UserSessionContext) -> Awaitable[None]:
        """Log when a tool completes execution (async)"""
        await asyncio.sleep(0)
        logger.info("Tool %s completed execution", tool_name)
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "tool_end",
            "tool": tool_name
        })

    @staticmethod
    async def on_handoff(source_agent: str, target_agent: str, context: UserSessionContext) -> Awaitable[None]:
        """Log when handoff occurs between agents (async)"""
        await asyncio.sleep(0)
        logger.info("Handoff from %s to %s", source_agent, target_agent)
        context.handoff_logs.append({
            "timestamp": datetime.now().isoformat(),
            "from": source_agent,
            "to": target_agent
        })

class AgentHooks:
    """
    Agent-specific lifecycle hooks with proper async implementation
    """
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name

    async def on_start(self, context: UserSessionContext) -> Awaitable[None]:
        """Agent-specific startup logic (async)"""
        await asyncio.sleep(0)
        logger.debug("%s starting", self.agent_name)

    async def on_end(self, context: UserSessionContext) -> Awaitable[None]:
        """Agent-specific cleanup logic (async)"""
        await asyncio.sleep(0)
        logger.debug("%s ending", self.agent_name)

    async def on_tool_start(self, tool_name: str, context: UserSessionContext) -> Awaitable[None]:
        """Agent-specific tool start logic (async)"""
        await asyncio.sleep(0)
        logger.debug("%s starting tool %s", self.agent_name, tool_name)

    async def on_tool_end(self, tool_name: str, context: UserSessionContext) -> Awaitable[None]:
        """Agent-specific tool end logic (async)"""
        await asyncio.sleep(0)
        logger.debug("%s completed tool %s", self.agent_name, tool_name)

    async def on_handoff(self, target_agent: str, context: UserSessionContext) -> Awaitable[None]:
        """Agent-specific handoff logic (async)"""
        await asyncio.sleep(0)
        logger.info("%s handing off to %s", self.agent_name, target_agent)

class StreamingHooks:
    """
    Hooks for handling streaming responses with proper async
    """
    
    @staticmethod
    async def on_stream_start(context: UserSessionContext) -> Awaitable[None]:
        """Initialize streaming session (async)"""
        await asyncio.sleep(0)
        logger.debug("Starting response streaming")
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "stream_start"
        })

    @staticmethod
    async def on_stream_chunk(content: str, context: UserSessionContext) -> Awaitable[None]:
        """Process each streaming chunk (async)"""
        await asyncio.sleep(0)
        logger.debug("Received stream chunk: %s", content)

    @staticmethod
    async def on_stream_end(context: UserSessionContext) -> Awaitable[None]:
        """Finalize streaming session (async)"""
        await asyncio.sleep(0)
        logger.debug("Ending response streaming")
        context.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "stream_end"
        })