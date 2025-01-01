import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from api import AssistantFnc

load_dotenv()


async def entrypoint(ctx: JobContext):
    # Create instance of AssistantFnc
    nba_functions = AssistantFnc()
    
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are an NBA expert voice assistant created by BK. Your primary focus is providing NBA-related information. "
            "You should be knowledgeable about: "
            "- NBA history, teams, and players "
            "- Current and historical statistics "
            "- Championship history and memorable moments "
            "- NBA rules and regulations "
            "- Player records and achievements "
            "Your responses should be concise and engaging, focusing on interesting NBA facts and insights. "
            "When discussing current NBA information, acknowledge that your knowledge cutoff date is April 2024. "
            "Avoid complex numbers or statistics that would be hard to follow in voice format. "
            "Keep responses conversational and easy to understand. "
            "You have access to real-time NBA data through functions for: "
            "- Team championship history "
            "- Current season records "
            "- Position information "
            "- Team legends and notable players "
            "Use these functions when responding to related queries to provide accurate information."
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        functions=nba_functions  # Register the NBA functions with the assistant
    )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say(
        "Hi, I'm your NBA expert assistant. I can tell you about team records, championships, legends, and more. "
        "What would you like to know?",
        allow_interruptions=True
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))