from typing import Optional

import discord
from redbot.core import commands
from redbot.core.bot import Red

TITLE = "Dummy Title"
INPUTS = {
    "Favorite Color": {
        "required": True,
        "style": discord.TextStyle.long,
        "placeholder": "magenta",
        "default": None,
        "value": None,
    },
    "Favorite Food": {
        "required": False,
        "style": discord.TextStyle.paragraph,
        "placeholder": "tacos",
        "default": "steak",
        "value": None,
    },
    "Favorite Car": {
        "required": False,
        "style": discord.TextStyle.short,
        "placeholder": "miata",
        "default": None,
        "value": None,
    },
}


class CustomModal(discord.ui.Modal):
    def __init__(self, title: str, inputs: dict, ctx: Optional[commands.Context]):
        self.inputs = inputs
        self.ctx = ctx
        super().__init__(title=title)
        for label, v in inputs.items():
            field = discord.ui.TextInput(
                label=label,
                style=v.get("style", discord.TextStyle.short),
                placeholder=v.get("placeholder"),
                default=v.get("default"),
                required=v.get("required", True),
                min_length=v.get("min_length"),
                max_length=v.get("max_length"),
            )
            self.add_item(field)
            v["value"] = field

    async def on_submit(self, interaction: discord.Interaction):
        if self.ctx:
            if interaction.user.id != self.ctx.author.id:
                return await interaction.response.send_message(
                    content="You are not allowed to interact with this button.",
                    ephemeral=True,
                )

        await interaction.response.send_message(
            "form has been filled.",
            ephemeral=True,
        )
        for k, v in self.inputs.items():
            v["value"] = v["value"].value


class Button(discord.ui.Button):
    def __init__(self, title: str, inputs: dict, ctx: Optional[commands.Context]):
        self.title = title
        self.inputs = inputs
        self.ctx = ctx
        super().__init__(label="open modal")

    async def callback(self, interaction: discord.Interaction):
        m = CustomModal(self.title, self.inputs, self.ctx)
        await interaction.response.send_modal(m)
        await m.wait()
        self.view.stop()


class View(discord.ui.View):
    def __init__(self, title: str, inputs: dict, ctx: Optional[commands.Context]):
        self.title = title
        self.inputs = inputs
        self.ctx = ctx
        super().__init__()
        self.add_item(Button(title, inputs, ctx))


class ModalExample(commands.Cog):
    def __init__(self, bot: Red, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.command(name="mtest")
    @commands.is_owner()
    async def make_modal(self, ctx):
        """Send a test modal"""
        view = View(TITLE, INPUTS, ctx)
        await ctx.send("Test modal message", view=view)
        await view.wait()
        await ctx.send("Modal done")
        inputs = view.inputs
        for k, v in inputs.items():
            answer = v["value"]
            await ctx.send(f"{k}: {answer}")


async def setup(bot: Red):
    await bot.add_cog(ModalExample(bot))
