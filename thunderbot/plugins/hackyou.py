# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}hack`
    Do a Prank With Replied user.

"""

import asyncio
import random

from . import *


@ultroid_cmd(pattern="hack")
async def _(event):
    animation_interval = 0.8
    animation_ttl = range(0, 11)
    xx = await event.eor("`Installing...`")
    animation_chars = [
        "`Installing files to compromised private server...`",
        "`Target Selected.`",
        "`Installing..   0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..   4%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..   8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..  20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..  36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..  52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Installing..  84%\n█████████████████████▒▒▒▒`",
        "`Installing.. 100%\n███████ INSTALLED ███████`",
        "`Target files uploading...\n\n Directing To Remote server...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 14])
    await asyncio.sleep(2)
    animation_interval = 0.8
    animation_ttl = range(0, 10)
    await xx.edit("`Connecting and getting combined token from my.telegram.org`")
    await asyncio.sleep(1)
    animation_chars = [
        "`root@anon:~#`",
        "`root@anon:~# ls`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~#`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~#`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~# touch setup.py`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~# touch setup.py\n setup.py deployed ...`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~# touch setup.py\n setup.py deployed ...\n Auto CMD deployed ...\n root@anon:~# trap whoami\n\ nwhoami=user`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~# touch setup.py\n setup.py deployed ...\n Auto CMD deployed ...\n root@anon:~# trap whoami\n\ nwhoami=user\n boost_trap on force ...\n victim detected in ghost ...\n\n All Done!`",
        "`root@anon:~# ls\n  usr  ghost  codes  \n root@aono:~# # EXPLOITING ...\n root@DumpServer:~# touch setup.py\n setup.py deployed ...\n Auto CMD deployed ...\n root@anon:~# trap whoami\n\ nwhoami=user\n boost_trap on force ...\n victim detected in ghost ...\n\n All Done!\n Installing Token!\n Token= DJ65gulO90P90nlkm65dRfc8I`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 14])
    await asyncio.sleep(1)
    await xx.edit("`starting tg-exploit`")
    await asyncio.sleep(1)
    await xx.edit(
        "`▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n   0% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3) kB`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n   4% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3) kB\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n   9% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3) kB\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n  14% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n  26% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh installing`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n  32% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index`"
    )
    await asyncio.sleep(3)
    await xx.edit(
        "`██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒\n  48% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n Bruteforce still up and running...`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`████████████████▒▒▒▒▒▒▒▒▒▒▒\n  60% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n BRUTEFORCE FOUND PASSWORD`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`████████████████████▒▒▒▒▒▒▒\n  73% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n BRUTEFORCE FOUND PASSWORD\n done with status 36748hdeg`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`████████████████████████▒▒▒\n  88% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n =========================\n =========================\n scraping data from user account\n =========================\n =========================`"
    )
    await asyncio.sleep(5)
    await xx.edit(
        "`████████  D O N E  ████████\n  100% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n =========================\n =========================\n scraping data from user account\n =========================\n =========================\n\n\n TERMINAL:\n tg-exploit log files stored in directory:\n emulated/0/android/apps/tg-exploit/log`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`████████  D O N E  ████████\n  100% completed\n\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n =========================\n =========================\n scraping data from user account\n =========================\n =========================\n\n\n TERMINAL:\n\n devices drives were cloned to database`"
    )
