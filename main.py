import os
from asyncio import TimeoutError

import discord

from models.LawBot import LawBot

dataFilePath = 'data.json'
bot = LawBot(dataFilePath)

TOKEN = os.environ["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    """
    Event handler for when the bot is ready and has connected to Discord.

    This function prints a message to the console indicating that the bot has connected.
    """
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    """
    Event handler for when a message is sent in a channel the bot has access to.

    If the message starts with '!consultation', the bot initiates a consultation request process by asking the user
    to enter the case type and details required for the case. The bot then responds with available law firms and 
    necessary documents for the consultation.

    Parameters
    ----------
    message : discord.Message
        The message object that triggered the event.
    """
    if message.content.startswith('!consultation'):
        await message.channel.send("Enter case type:")

        def check(m):
            """
            Check function to ensure the response is from the same author and channel as the original message.

            Parameters
            ----------
            m : discord.Message
                The message object to check.

            Returns
            -------
            bool
                True if the message author and channel match the original message, False otherwise.
            """
            return m.author == message.author and m.channel == message.channel

        try:
            case_type_msg = await client.wait_for('message', check=check, timeout=60.0)
            case_type = case_type_msg.content.strip()

            case_type_info = next(
                (item for item in bot.court_case_types if case_type.lower() in item["case_type"].lower()), None)
            if not case_type_info:
                await message.channel.send("Case type not found. Try again later.")
                return

            details = {}
            for detail in case_type_info["required_details"]:
                await message.channel.send(f"Enter {detail}:")
                detail_msg = await client.wait_for('message', check=check, timeout=60.0)
                details[detail] = detail_msg.content.strip()

            result = bot.request_consultation(case_type, details)

            if isinstance(result, str):
                await message.channel.send(result)
            else:
                firms = "\n".join(result["firms"])
                documents = "\n".join(result["required_documents"])
                response = (f"**Available law firms:**\n{firms}\n\n"
                            f"**Necessary documents:**\n{documents}")
                await message.channel.send(response)
        except TimeoutError:
            await message.channel.send("Time out. Try again later.")

client.run(TOKEN)