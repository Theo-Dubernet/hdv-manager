import discord
from .requete_db import *

class FormCreateSales(discord.ui.Modal, title="Ajout d'un achat"):
    nom_item = discord.ui.TextInput(
        label="Nom de l'item acheter",
        placeholder="Scapula de harebourg",
        required=True,
        max_length=50
    )

    lot = discord.ui.TextInput(
        label="Lots",
        placeholder="1, 10, 100, 1000",
        required=True,
        max_length=4,
    )

    price = discord.ui.TextInput(
        label="Prix",
        placeholder="94556649",
        required=True,
        max_length=15,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        insert_sale(self.nom_item, self.lot, self.price)
        msg = await interaction.followup.send(f"L'achat a bien été créer !", ephemeral=True)
        await msg.delete(delay=5)