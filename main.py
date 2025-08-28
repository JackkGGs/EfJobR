import discord
from discord.ext import commands
import google.generativeai as genai
import random
from config import *

# --------------------------------------------------------------------------------
# AI and Discord Bot Configuration
# --------------------------------------------------------------------------------

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Bot intents
intents = discord.Intents.default()
intents.message_content = True

# Bot Initialization
bot = commands.Bot(command_prefix='!', intents=intents)

# --------------------------------------------------------------------------------
# Classses
# --------------------------------------------------------------------------------

class FeedbackView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300) # Timeout after 5 menit

    @discord.ui.button(label="👍 This Helps!", style=discord.ButtonStyle.green)
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Callback for 'Helpful'."""
        await interaction.response.send_message("Thank you for the response! Happy to help. Anything else I could help you with?", ephemeral=True)
        # Disables all the buttons upon clicking one.
        for child in self.children:
            child.disabled = True
        await interaction.message.edit(view=self)

    @discord.ui.button(label="👎 Not So Helpful..", style=discord.ButtonStyle.red)
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Callback for 'Not Helpful'."""
        await interaction.response.send_message("I am sorry if that wasn't very pleasing. Anything else I could help you with?", ephemeral=True)
        # Disables all the buttons upon clicking one.
        for child in self.children:
            child.disabled = True
        await interaction.message.edit(view=self)

# --------------------------------------------------------------------------------
# Event Listeners
# --------------------------------------------------------------------------------

@bot.event
async def on_ready():
    """Prints logs when the bot is ready."""
    print(f'Bot {bot.user} is online!')
    print('-------------------------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message is a DM
    if isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                random_temp = round(random.uniform(0.1, 1.0), 1)

                prompt = f"""
                Your name is EfJobR. Your task is to give humans recommendations on jobs and possible open recruitments.
                
                Your message musn't exceed 499 characters!
                You're allowed to embed links here.
                Keep an eye on "User's message" by the way. Adjust your response by translating it to the language the user used on the user's message.
                On the end of the message, add "Did this help?" or similar messages depending on the language the user used

                Keep this format and ONLY this format (Translate for multilingual cases EXCEPT the words before ":"):
                Hmm..
                Alright,
            
                - Career: [Career Name]
                - Description: [A simple description of the career]
                - Required Skills: [A list of required skills, use comas]
                - Demo Projects: [A simple demo project to hone the skills]
                - Resources: [Embed 1-2 links here]

                User's message: {message.content}
                """

                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=random_temp,
                        max_output_tokens=499
                    )
                )

                await message.channel.send(response.text, view=FeedbackView())

            except Exception as e:
                await message.channel.send(f"Sorry, there seems to be an error handling this request. Error: {e}")
    else:
        # If the message is not a DM, process commands
        await bot.process_commands(message)

@bot.command(name='job_recommendations', help='Helping you get personalized recruitments.')
async def job_recommendations(ctx, *, query: str):
    """
    Recommends careers based on user inputs
    How to use: !job_recommendations [message]
    """
    # Sends a temporary message upon command message input
    await ctx.send(f"{ctx.author.mention}, I've sent a Direct Message (DM) to you!")

    async with ctx.typing():
        try:
            # Randomizes the creativity of Gemini's responses
            random_temp = round(random.uniform(0.1, 1.0), 1)

            prompt = f"""
            Your name is EfJobR. Your task is to give humans recommendations on jobs and possible open recruitments.
                
            Your message musn't exceed 499 characters!
            You're allowed to embed links here.
            Keep an eye on "User's message" by the way. Adjust your response by translating it to the language the user used on the user's message.
            On the end of the message, add "Did this help?" or similar messages depending on the language the user used

            Keep this format and ONLY this format (Translate for multilingual cases EXCEPT the words before ":"):
            Hmm..
            Alright,
        
            - Career: [Career Name]
            - Description: [A simple description of the career]
            - Required Skills: [A list of required skills, use comas]
            - Demo Projects: [A simple demo project to hone the skills]
            - Resources: [Embed 1-2 links here]

            User's message: {query}
            """

            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=random_temp,
                    max_output_tokens=499
                )
            )

            # Send responses to user's DMs directly
            await ctx.author.send(response.text, view=FeedbackView())

        except Exception as e:
            await ctx.author.send(f"Sorry, there seems to be an error handling this request. Error: {e}")

# --------------------------------------------------------------------------------
# Bot execution
# --------------------------------------------------------------------------------

bot.run(token=DISCORD_TOKEN)