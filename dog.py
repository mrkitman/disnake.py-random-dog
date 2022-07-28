import aiohttp

@bot.slash_command (description='Рандомная картинка собаки')
async def dog(self, inter):
    async with aiohttp.ClientSession () as cs:
        async with cs.get ( "https://random.dog/woof.json" ) as r:
            data = await r.json ()
            embed = disnake.Embed (title="Собака барабака",colour=0x2f3136)
            embed.set_image ( url=data['url'] )
            await inter.send ( embed=embed )