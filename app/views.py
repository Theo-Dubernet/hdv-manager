import discord
from discord import Button, Interaction
from .requete_db import get_all_buy
from .modal import FormCreateSales

PAGE_SIZE = 12

class BuyItemPagination(discord.ui.View):
    def __init__(self, buy_item_data, page=0):
        super().__init__(timeout=None)
        self.buy_item_data = buy_item_data
        self.page = page

        # Bouton précédent si pas sur la première page
        if self.page > 0:
            self.add_item(
                discord.ui.Button(
                    label="Précédent",
                    style=discord.ButtonStyle.secondary,
                    custom_id="prev"
                )
            )

        # Bouton suivant si plus de données après
        if (self.page + 1) * PAGE_SIZE < len(self.buy_item_data):
            self.add_item(
                discord.ui.Button(
                    label="Suivant",
                    style=discord.ButtonStyle.secondary,
                    custom_id="suiv"
                )
            )

    def get_content_page(self):
        start = self.page * PAGE_SIZE
        end = start + PAGE_SIZE
        page_items = self.buy_item_data[start:end]

        if not page_items:
            return "Aucun achat sur cette page"

        content = ""
        for i, (id, lot, price, name_item, date_buy) in enumerate(page_items, start=1):
            content += f"#{i} — {name_item} | Lot: {lot} | 💰 {price} | 📅 {date_buy.strftime('%d/%m/%Y %H:%M')}\n\n"
        return content

    async def interaction_check(self, interaction: discord.Interaction):
        custom_id = interaction.data.get("custom_id")
        if custom_id not in ("prev", "suiv"):
            return False

        new_page = self.page - 1 if custom_id == "prev" else self.page + 1
        new_view = BuyItemPagination(self.buy_item_data, page=new_page)
        await interaction.response.edit_message(
            content=new_view.get_content_page(),
            view=new_view
        )
        return True

class ViewBuyItemManager(discord.ui.View):
    @discord.ui.button(label="Ajouter achat", style=discord.ButtonStyle.primary)
    async def add_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(FormCreateSales())

    @discord.ui.button(label="Lister achats", style=discord.ButtonStyle.secondary)
    async def list_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Récupère les données de la BDD
        buy_data = get_all_buy()
        # Envoie la vue de pagination
        view = BuyItemPagination(buy_data, page=0)
        await interaction.response.send_message(
            content=view.get_content_page(),
            view=view,
            ephemeral=True
        )