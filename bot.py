from pyrogram import filters
from pyrogram import Client 
import os
import logging
logger = logging.getLogger(__name__)

#source_channels = [-1001584640162, -1001681544262]

source_channels = [-1001738403205,-1001644355746,-1001774783341,-1001590166762,-1001955066093,-1001815983445,-1001970203410,-1001841307280,-1001701810776,-1001947542077,-1001794267960,-1001689743078,-1001969547667]
# define the target channel to forward messages to
target_channel = -1001977155617

api_id = 29311671
api_hash = "e54d730e1965cd2c5bf140a4461f9818"
ses = "BQG_QrcAraNc8NTynDoKmb_cSL9CdbmH7CYjWSRyayk5fdp1aBAiMwnvvSNGGG8GCjLbmtxPzYP6d9-VHp1cWcmRG_araBavzHNVsCefojkUziaI-QpmXdvcybXEaQsrSa96cG2GhOuWS7NtkvEsrHkfpgNBizhBBZn9REZiyGBms5hqYUnCQ8zKtBhxoxzRNW7xSKRQ3MumupFOeEboeOEF83sY0UVd3Ha9JR7mEQC76tPiZvYHA4a-ZOB79xDCE3WKA2zJCjrNQhliI5nQth6EDWTxuqhwtZHs7PT4KxD-zcmzULMUQHaCuYtNr0-luVAJM2Nzqt5DuD5YNr6qJ6s0PiuV4QAAAAFrf6yOAA"


app = Client("my_unt", api_id=api_id, api_hash=api_hash, session_string = ses)

#main func
@app.on_message(filters.chat(source_channels) & (filters.regex('TP')|filters.regex('Tp')|filters.regex('tp')|filters.regex('TP1')|filters.regex('Tp1')))
async def copy(_, m):
    # coping the messages to the channel
    try:
        await m.copy(target_channel)

    except:
        f = await app.get_messages(source_channels, m.id)
        downloaded_media = []
        path = await m.download()
            
        await app.send_photo(target_channel,path,caption = f.caption )

        for path in downloaded_media:
            if os.path.isfile(path):
                logger.debug(f"Removing file {path}")
                os.remove(path) 
 

print("I'm Fucking Working Now!")
app.run()