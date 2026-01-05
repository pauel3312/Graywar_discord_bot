import discord
from discord.ext import commands

TOKEN = open("TOKEN", "r").read().strip()

GUILD_ID = 989821370747719731

ROLEID_ADMIN = 1419708521053818974
ROLEID_MOD = 1420006950707658783
ROLEID_DEV = 1419708388421406801


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")

    await bot.tree.sync()
    print("Commands synced!")

# ------------------------------------------------------------------
@bot.tree.command(name="teamkill", description="Sends a message about team‑killing policy")
@discord.app_commands.checks.has_any_role(ROLEID_DEV, ROLEID_MOD, ROLEID_ADMIN)
async def teamkill(interaction: discord.Interaction):
    await interaction.response.send_message(
        """Thank you for contacting us, but we do not ban players for teamkilling if it has only happened 1–2 times. We will monitor the situation, and if we detect further violations, we will take action.
Sincerely, the GrayWar server staff"""
    )

@bot.tree.command(name="new_staff", description="Sends a message with important info for new staff")
@discord.app_commands.checks.has_any_role(ROLEID_DEV, ROLEID_MOD, ROLEID_ADMIN)
async def staff_new(interaction: discord.Interaction):
    await interaction.response.send_message(
        """Please read <#1425228942301724764> when you have time and let <@243508870419316736> know whe you are in game, so he can add you to the staff permissions on the game servers.
        We're happy to have you in our staff!"""
    )


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    """Handle all slash‑command errors in one place."""

    if isinstance(error, discord.app_commands.CheckFailure):
        if not interaction.response.is_done():
            await interaction.response.send_message(
                "You don’t have permission to use that command.",
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                "You don’t have permission to use that command.",
                ephemeral=True
            )

        return

    raise error

# ------------------------------------------------------------------
bot.run(TOKEN)
