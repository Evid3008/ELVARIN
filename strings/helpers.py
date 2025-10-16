HELP_1 = """
<b><u>🎵 𝐏𝐋𝐀𝐘 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 :</b></u>

<b>🎵 𝐏𝐋𝐀𝐘 :</b>
/play or /vplay : Start streaming
/vvplay : Convert & play movie files (reply to video)
/playforce or /vplayforce : Force play

<b>📺 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 :</b>
/cplay or /cvplay : Channel play
/cplayforce or /cvplayforce : Force channel play

<b>🔄 𝐋𝐎𝐎𝐏 :</b>
/loop [enable/disable] : Loop stream
/loop [1-10] : Loop count

<b>🔀 𝐒𝐇𝐔𝐅𝐅𝐋𝐄 :</b>
/shuffle : Shuffle queue
/queue : Show queue

<b>⏩ 𝐒𝐄𝐄𝐊 :</b>
/seek [seconds] : Seek forward
/seekback [seconds] : Seek backward

<b>🎶 𝐒𝐎𝐍𝐆 :</b>
/song [name/url] : Download song
"""

HELP_2 = """
<b><u>⚙️ 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 :</b></u>

ᴊᴜsᴛ ᴀᴅᴅ <b>ᴄ</b> ɪɴ ᴛʜᴇ sᴛᴀʀᴛɪɴɢ ᴏғ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜsᴇ ᴛʜᴇᴍ ғᴏʀ ᴄʜᴀɴɴᴇʟ.

/pause : ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
/resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.
/skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.
/end ᴏʀ /stop : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
/player : ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ.
/queue : sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.
/lyrics [sᴏɴɢ ɴᴀᴍᴇ] : sᴇᴀʀᴄʜ ʟʏʀɪᴄs ғᴏʀ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴀɴᴅ sᴇɴᴅ ᴛʜᴇ ʀᴇsᴜʟᴛs.
"""

HELP_3 = """
<b><u>🔐 𝐀𝐔𝐓𝐇 𝐔𝐒𝐄𝐑𝐒 :</b></u>

ᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

/auth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] : ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.
/unauth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴀᴜᴛʜ ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ.
/authusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.
"""

HELP_4 = """
<b><u>📢 𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓 𝐅𝐄𝐀𝐓𝐔𝐑𝐄 :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs :</u>
<b>-pin</b> : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.
<b>-pinloud</b> : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs.
<b>-user</b> : ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.
<b>-assistant</b> : ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.
<b>-nobot</b> : ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ..

<b>ᴇxᴀᴍᴩʟᴇ:</b> <code>/broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ</code>
"""

HELP_5 = """
<b><u>🚫 𝐁𝐋𝐎𝐂𝐊 𝐔𝐒𝐄𝐑𝐒 :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

sᴛᴀʀᴛs ɪɢɴᴏʀɪɴɢ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴜsᴇʀ, sᴏ ᴛʜᴀᴛ ʜᴇ ᴄᴀɴ'ᴛ ᴜsᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.

/block [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʙʟᴏᴄᴋ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴏᴜʀ ʙᴏᴛ.
/unblock [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴜɴʙʟᴏᴄᴋs ᴛʜᴇ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀ.
/blockedusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs.

<u><b>ᴄʜᴀᴛ ʙʟᴀᴄᴋʟɪsᴛ ғᴇᴀᴛᴜʀᴇ :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

ʀᴇsᴛʀɪᴄᴛ sʜɪᴛ ᴄʜᴀᴛs ᴛᴏ ᴜsᴇ ᴏᴜʀ ᴘʀᴇᴄɪᴏᴜs ʙᴏᴛ.

/blacklistchat [ᴄʜᴀᴛ ɪᴅ] : ʙʟᴀᴄᴋʟɪsᴛ ᴀ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ.
/whitelistchat [ᴄʜᴀᴛ ɪᴅ] : ᴡʜɪᴛᴇʟɪsᴛ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ.
/blacklistedchat : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs.
"""

HELP_6 = """
<b><u>🔄 𝐒𝐓𝐑𝐄𝐀𝐌 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 :</b></u>

<b>🎵 𝐏𝐋𝐀𝐘 :</b>
/play or /vplay : Start streaming
/vvplay : Convert & play movie files (reply to video)
/playforce or /vplayforce : Force play

<b>📺 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 :</b>
/cplay or /cvplay : Channel play
/cplayforce or /cvplayforce : Force channel play

<b>🔄 𝐋𝐎𝐎𝐏 :</b>
/loop [enable/disable] : Loop stream
/loop [1-10] : Loop count

<b>🔀 𝐒𝐇𝐔𝐅𝐅𝐋𝐄 :</b>
/shuffle : Shuffle queue
/queue : Show queue

<b>⏩ 𝐒𝐄𝐄𝐊 :</b>
/seek [seconds] : Seek forward
/seekback [seconds] : Seek backward

<b>🎶 𝐒𝐎𝐍𝐆 :</b>
/song [name/url] : Download song

<b>⚡ 𝐒𝐏𝐄𝐄𝐃 :</b>
/speed or /playback : Adjust speed
/cspeed or /cplayback : Channel speed
"""

HELP_7 = """
<b><u>⚡ 𝐒𝐏𝐄𝐄𝐃 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 :</b></u>

» ᴏɴʟʏ ʏᴏᴜᴛᴜʙᴇ sᴛʀᴇᴀᴍ's sᴘᴇᴇᴅ ᴄᴀɴ ʙᴇ ᴄᴏɴᴛʀᴏʟʟᴇᴅ ᴄᴜʀʀᴇɴᴛʟʏ.

<b><u>{0} sᴘᴇᴇᴅ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ</b></u>

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.

/speed or /playback : ᴀᴅᴊᴜsᴛ sᴘᴇᴇᴅ
/cspeed or /cplayback : ᴄʜᴀɴɴᴇʟ sᴘᴇᴇᴅ
"""

HELP_8 = """
<b><u>📊 𝐒𝐓𝐀𝐓𝐒 & 𝐈𝐍𝐅𝐎 :</b></u>

/ping : ᴄʜᴇᴄᴋ ʙᴏᴛ's ᴘɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs.
/stats : sʜᴏᴡ ʙᴏᴛ's sᴛᴀᴛɪsᴛɪᴄs ᴀɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
/gstats : sʜᴏᴡ ɢʟᴏʙᴀʟ sᴛᴀᴛɪsᴛɪᴄs.
/sudolist : sʜᴏᴡ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.

<b><u>🤖 𝐂𝐇𝐀𝐓𝐁𝐎𝐓 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 :</b></u>

/chatbot : sʜᴏᴡ ᴄʜᴀᴛʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
/chatbot_stats : sʜᴏᴡ ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs.
/shivali_stats : sʜᴏᴡ ʟᴇᴀʀɴɪɴɢ sʏsᴛᴇᴍ sᴛᴀᴛs.

<b><u>ɢʟᴏʙᴀʟ ʙᴀɴ ғᴇᴀᴛᴜʀᴇ :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

/gban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ɢʟᴏʙᴀʟʟʏ ʙᴀɴ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ ʙʟᴀᴄᴋʟɪsᴛ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ.
/ungban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ ɢʟᴏʙᴀʟ ʙᴀɴ ʟɪsᴛ.
/gbannedusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs.
"""