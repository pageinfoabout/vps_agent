
from telethon.sync import TelegramClient, events
from config import api_id, api_hash

with TelegramClient( 'anon', api_id, api_hash) as client:

    @client.on (events.NewMessage(pattern=r"^hi"))
    async def hi (event):
        await event. reply("hi how can i help you")
    @client.on(events.NewMessage(pattern=r"^\.info"))
    async def reg(event) :

        me = await client.get_me()
        await event. reply(me.stringify())
    @client.on(events.NewMessage(pattern=r"\.conversations"))
    async def infoconv (event) :
        async for dailog in client.iter_dialogs():
            print(dailog.name + " has id " + str(dailog.id) )
    @client.on(events.NewMessage(pattern=r"\.text •"))
    async def texting (event):
        text = event.message. raw_text
        await client.send_message("+79853941837", text )
    @client.on(events.NewMessage(pattern=r"\.send" ) )
    async def sending (event):
        await client.send_message("79853941837", "hi me is sended" )
    # await event. reply(text)
    client. run_until_disconnected ()