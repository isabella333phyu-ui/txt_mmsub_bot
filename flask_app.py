import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from telegram.error import BadRequest

# သင့်ရဲ့ Channel Username နဲ့ Token အသစ်
CHANNEL_USERNAME = "@TXT_to_do_mmsub"
TOKEN = "8859312447:AAHPP4mNU-2e6YUjRT8Wcp4OyeY3jsmi3sQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"),
            InlineKeyboardButton("Confirm ✅", callback_data="confirm")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        'မင်္ဂလာပါ! TxT MMSUB Bot မှကြိုဆိုပါတယ်။\n\nကျေးဇူးပြု၍ Join Channel ကိုနှိပ်ပြီး Channel ကို Join ပေးပါ။ ပြီးလျှင် Confirm ✅ ကိုနှိပ်ပါ။',
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'confirm':
        try:
            member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

            if member.status in ['left', 'kicked']:
                await query.answer()
                keyboard = [
                    [
                        InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"),
                        InlineKeyboardButton("Confirm ✅", callback_data="confirm")
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                try:
                    await query.edit_message_text(
                        text='❌ Channel ကို Join မလုပ်ရသေးပါ။\n\nJoin ပြီးတာ သေချာ‌ကြောင်း Confirm လုပ်ပေးပါ။',
                        reply_markup=reply_markup
                    )
                except BadRequest:
                    pass
            else:
                await query.answer()
                # Main Menu ၁၅ ခုကို ပြင်ဆင်ထားပါသည်
                menu_keyboard = [
                    ['This Week Update', 'Last Week Update'],
                    ['ToDo', 'ToDo Spin-Off', 'Not ToDo'],
                    ['T:Time', 'EPISODE', 'TxT-Log'],
                    ['TxT Dream Week', 'Talk X Today', 'TxT Content'],
                    ['Solo Show', 'Other Show', 'Song MMSUB'],
                    ['Behind', 'Contact Admin']
                ]

                reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

                await query.message.delete()
                await context.bot.send_message(
                    chat_id=query.message.chat_id,
                    text='TxT MMSUB Menu သို့ ကြိုဆိုပါတယ်။ အောက်ပါ Menu များမှ ရွေးချယ်ကြည့်ရှုနိုင်ပါသည်။',
                    reply_markup=reply_markup
                )
        except BadRequest:
            await query.answer('Bot အား Channel ထဲတွင် Admin ပေးထားရန် လိုအပ်ပါသည်။', show_alert=True)
            
    elif query.data.startswith('vid_'):
        await query.answer()
        msg_id = int(query.data.split('_')[1])

        try:
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_USERNAME,
                message_id=msg_id
            )
        except BadRequest:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text="❌ ဗီဒီယို ရှာမတွေ့ပါ။ (Message ID မှားနေခြင်း သို့မဟုတ် Channel တွင် ဖျက်ခံရခြင်း ဖြစ်နိုင်ပါသည်)"
            )

    # Should We Run Away? အတွက် Code
    elif query.data == 'content_ShouldWeRunAway?':
        await query.answer()
        video_ids = [1272, 1279, 1288]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='🏃‍♂️ Should We Run Away ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass
                
    # Summer Diary အတွက် Code
    elif query.data == 'content_Summer Diary':
        await query.answer()
        video_ids = [1242, 1258, 1260, 1264]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='☀️ Summer Diary ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass
                
    # TxT Toob Cast အတွက် Code
    elif query.data == 'content_Toob Cast':
        await query.answer()
        video_ids = [992, 1007]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='🎙️ TxT Toob Cast ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass

    # More အတွက် Code
    elif query.data == 'content_More':
        await query.answer()
        video_ids = [1046, 1128, 302, 777, 918]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='✨ More ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass

    # TxT Dream Week 2024 အတွက် Code
    elif query.data == 'dream_2024':
        await query.answer()
        video_ids = [842]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='📺 Dream Week 2024 ဗီဒီယိုကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass

    # TxT Dream Week 2026 အတွက် Code
    elif query.data == 'dream_2026':
        await query.answer()
        video_ids = [847, 849, 851, 858, 860, 869]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='📺 Dream Week 2026 ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass
                
    # Talk X Today Season 4 အတွက် Code
    elif query.data == 'talk_Season 4':
        await query.answer()
        video_ids = [1318, 1319, 1337, 1340, 1342]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='🎤 Talk X Today Season 4 ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass

    # Talk X Today Season 5 အတွက် Code
    elif query.data == 'talk_Season 5':
        await query.answer()
        video_ids = [1148, 1149, 1167, 1168, 1169, 1171]

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text='🎤 Talk X Today Season 5 ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
        )

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=query.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass
                
    # ToDo Menu အတွက် နှစ်အလိုက် Submenu ခလုတ်များ
    elif query.data.startswith('todo_202'):
        await query.answer()
        year = query.data.split('_')[1] 

        if year == '2021':
            keyboard = [
                [InlineKeyboardButton("S1 Ep.1 to 16", callback_data="todo_s1")],
                [InlineKeyboardButton("S2 Ep.17 to 25", callback_data="todo_s2")],
                [InlineKeyboardButton("S3 Ep.26 to 50", callback_data="todo_s3")],
                [InlineKeyboardButton("S4 Ep.51 to 64", callback_data="todo_s4")]
            ]
        elif year == '2022':
            keyboard = [
                [InlineKeyboardButton("S5 Ep.65 to 79", callback_data="todo_s5")],
                [InlineKeyboardButton("S6 Ep.80 to 98", callback_data="todo_s6")]
            ]
        elif year == '2023':
            keyboard = [
                [InlineKeyboardButton("S7 Ep.99 to 117", callback_data="todo_s7")]
            ]
        elif year == '2024':
            keyboard = [
                [InlineKeyboardButton("S8 Ep.118 to 130", callback_data="todo_s8")],
                [InlineKeyboardButton("S9 Ep.131 to 146", callback_data="todo_s9")]
            ]
        elif year == '2025':
            keyboard = [
                [InlineKeyboardButton("S10 Ep.147 to 159", callback_data="todo_s10")],
                [InlineKeyboardButton("S11 Ep.160 to 164", callback_data="todo_s11")]
            ]
        elif year == '2026':
            keyboard = [
                [InlineKeyboardButton("S12 Ep.165 to 169", callback_data="todo_s12")],
                [InlineKeyboardButton("S13 Ep.170 to 175", callback_data="todo_s13")]
            ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f'🎬 {year} အတွက် ကြည့်ရှုလိုသော Season ကို ရွေးချယ်ပါ -',
            reply_markup=reply_markup
        )
        
    # ToDo ၏ Season (S1 to S13) ခလုတ်များ
    elif query.data.startswith('todo_s'):
        await query.answer()

        season_videos = {
            'todo_s1': [91, 98, 120, 141, 157, 165, 171, 201, 204, 219, 235, 347, 508, 546, 701, 770],
            'todo_s2': [1122, 780, 784, 1004, 1005],
            'todo_s3': [], 
            'todo_s4': [1010, 1008, 1011, 1012, 1019, 1015, 1020, 1022, 913, 916, 923],
            'todo_s5': [], 
            'todo_s6': [1356],
            'todo_s7': [982, 983, 1184, 1185, 1202, 1348, 1350],
            'todo_s8': [794, 811, 1000, 998, 987, 986, 1136, 11140, 1142], 
            'todo_s9': [803, 821, 37, 49, 25, 28, 19, 22, 10, 33, 34, 46, 51, 54],
            'todo_s10': [1363, 1372],
            'todo_s11': [646, 647, 650, 655, 659],
            'todo_s12': [1063, 828],
            'todo_s13': [1300, 1314, 1320, 1325, 1332, 1345]
        }

        video_ids = season_videos.get(query.data, [])

        if not video_ids:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='⏳ ဤ Season အတွက် ဗီဒီယိုများကို မကြာမီ တင်ပေးပါမည်။'
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='🎬 ရွေးချယ်ထားသော Season မှ ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass
                    
    # Other Show ၏ ခလုတ်များ
    elif query.data.startswith('other_'):
        await query.answer()

        if query.data == 'other_more':
            keyboard = [
                [InlineKeyboardButton("Part 1", callback_data="other_more_1"), InlineKeyboardButton("Part 2", callback_data="other_more_2")],
                [InlineKeyboardButton("Part 3", callback_data="other_more_3"), InlineKeyboardButton("Part 4", callback_data="other_more_4")],
                [InlineKeyboardButton("Part 5", callback_data="other_more_5")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                text='🎭 More တွင် ကြည့်ရှုလိုသော အပိုင်းကို ရွေးချယ်ပါ -',
                reply_markup=reply_markup
            )
        else:
            other_shows = {
                'other_idol1n2d': [1074, 1135, 1137, 1068, 1070],
                'other_zipdaesung': [928, 935],
                'other_silence': [708, 716],
                'other_idolhouse': [971, 972, 980],
                'other_humantheater': [956, 968, 989, 993, 1232],
                'other_sumbakkokjil': [1266, 1274],
                'other_parenting': [1048],
                'other_counseling': [1143, 1164],
                'other_snackshop': [1026],
                'other_more_1': [804, 1072, 1110, 1066, 682, 302, 895, 696, 973, 975],
                'other_more_2': [978, 1042, 868, 793, 1310, 1330, 1360, 1364],
                'other_more_3': [],
                'other_more_4': [],
                'other_more_5': []
            }

            video_ids = other_shows.get(query.data, [])

            if not video_ids:
                await context.bot.send_message(
                    chat_id=query.message.chat_id,
                    text='❌ မရှိသေးပါ။'
                )
            else:
                await context.bot.send_message(
                    chat_id=query.message.chat_id,
                    text='🎭 ရွေးချယ်ထားသော Show မှ ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
                )
                for vid_id in video_ids:
                    try:
                        await context.bot.copy_message(
                            chat_id=query.message.chat_id,
                            from_chat_id=CHANNEL_USERNAME,
                            message_id=vid_id
                        )
                        await asyncio.sleep(0.5) 
                    except BadRequest:
                        pass

    # EPISODE ခလုတ်များ
    elif query.data.startswith('ep_'):
        await query.answer()

        ep_videos = {
            'ep_2019': [],
            'ep_2020': [],
            'ep_2021': [],
            'ep_2022': [],
            'ep_2023': [],
            'ep_2024': [],
            'ep_2025': [],
            'ep_2026': [909, 1024, 1028, 1049, 1076, 1112, 1253, 1284, 1309, 1315, 1333]
        }

        video_ids = ep_videos.get(query.data, [])

        if not video_ids:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='❌ ဘာသာပြန်ထားတာ မရှိသေးပါ။'
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='✨ ရွေးချယ်ထားသော နှစ်မှ EPISODE ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass
                    
    # TxT-Log ခလုတ်များ
    elif query.data.startswith('log_'):
        await query.answer()

        log_videos = {
            'log_2022': [],
            'log_2023': [],
            'log_2024': [790, 786],
            'log_2025': [802, 694, 839, 837, 788, 720],
            'log_2026': [775, 805, 893, 1045, 1270, 1291, 1368]
        }

        video_ids = log_videos.get(query.data, [])

        if not video_ids:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='❌ ဘာသာပြန်ထားတာ မရှိသေးပါ။'
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='🔴 ရွေးချယ်ထားသော နှစ်မှ TxT-Log ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass
                    
    # T:Time ခလုတ်များ
    elif query.data.startswith('ttime_'):
        await query.answer()

        ttime_videos = {
            'ttime_2025': [510, 609, 610, 611, 614, 616, 724, 733],
            'ttime_2026': [769, 791, 823, 864, 872, 874, 877, 882, 901, 947, 965, 1147, 1153, 1181, 1207, 1219, 1303, 1317, 1322, 1323],
            'ttime_2027': []
        }

        video_ids = ttime_videos.get(query.data, [])

        if not video_ids:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='❌ Video များမရှိသေးပါ။'
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='📹 ရွေးချယ်ထားသော နှစ်မှ T:Time ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass
                    
    # Solo Show ခလုတ်များ
    elif query.data.startswith('solo_'):
        await query.answer()

        if query.data == 'solo_Yeonjun':
            keyboard = [
                [InlineKeyboardButton("No Labels: Part02", callback_data="solo_yj_nolabels")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                text='🌟 Yeonjun အတွက် ကြည့်ရှုလိုသော အပိုင်းကို ရွေးချယ်ပါ -',
                reply_markup=reply_markup
            )

        elif query.data == 'solo_yj_nolabels':
            video_ids = [1213, 1225, 1228, 1234, 1250, 1255, 1262, 1269, 1281, 1296, 1335]

            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='🌟 Yeonjun (No Labels: Part02) ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass
        else:
            solo_videos = {
                'solo_Soobin': [663, 670, 676, 636],
                'solo_Huening Kai': [687, 1016, 1035, 1061],
                'solo_Taehyun': [385],
                'solo_Beomgyu': []
            }

            if query.data in solo_videos:
                video_ids = solo_videos[query.data]

                if not video_ids:
                    await context.bot.send_message(
                        chat_id=query.message.chat_id,
                        text='❌ မရှိသေးပါ။'
                    )
                else:
                    member_name = query.data.split('_')[1]
                    await context.bot.send_message(
                        chat_id=query.message.chat_id,
                        text=f'🌟 {member_name} ၏ ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
                    )
                    for vid_id in video_ids:
                        try:
                            await context.bot.copy_message(
                                chat_id=query.message.chat_id,
                                from_chat_id=CHANNEL_USERNAME,
                                message_id=vid_id
                            )
                            await asyncio.sleep(0.5)
                        except BadRequest:
                            pass
                            
    # Behind ခလုတ်များ
    elif query.data.startswith('behind_'):
        await query.answer()

        behind_videos = {
            'behind_stick': [903, 951, 970, 981, 1001, 1024, 1028, 1040, 1124],
            'behind_setsuna': [1277, 1283, 1309],
            'behind_more': [781, 963]
        }

        video_ids = behind_videos.get(query.data, [])

        if not video_ids:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='❌ Video များမရှိသေးပါ။'
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text='🎬 Behind ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...'
            )
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=query.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5)
                except BadRequest:
                    pass

    else: 
        await query.answer()
        selection = query.data.split('_', 1)[1] if '_' in query.data else query.data
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=f'✨ "{selection}" အပိုင်း ဗီဒီယိုများကို မကြာမီ တင်ပေးပါမည်။'
        )

async def handle_menu_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # This Week Update 
    if text == 'This Week Update':
        video_ids = []  

        if not video_ids:
            await update.message.reply_text('❌ ယခုအပတ်အတွက် Update ဗီဒီယို မရှိသေးပါ။')
        else:
            await update.message.reply_text('📅 This Week Update ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...')
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=update.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5) 
                except BadRequest:
                    pass

    # Last Week Update 
    elif text == 'Last Week Update':
        video_ids = [1379]

        if not video_ids:
            await update.message.reply_text('❌ ပြီးခဲ့သောအပတ်က Update ဗီဒီယို မရှိပါ။')
        else:
            await update.message.reply_text('📅 Last Week Update ဗီဒီယိုကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...')
            for vid_id in video_ids:
                try:
                    await context.bot.copy_message(
                        chat_id=update.message.chat_id,
                        from_chat_id=CHANNEL_USERNAME,
                        message_id=vid_id
                    )
                    await asyncio.sleep(0.5) 
                except BadRequest:
                    pass

    # Not ToDo 
    elif text == 'Not ToDo':
        video_ids = [749, 753, 757, 761, 1161, 1174, 1182, 1192]

        await update.message.reply_text('🎬 Not ToDo ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...')

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=update.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass
                
    elif text == 'ToDo Spin-Off':
        video_ids = [1050, 1051, 1052, 1053]

        await update.message.reply_text('🎬 ToDo Spin-Off ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...')

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=update.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
                await asyncio.sleep(0.5)
            except BadRequest:
                pass

    elif text == 'Song MMSUB':
        video_ids = [70, 140, 907, 148, 152, 908, 384, 876, 948, 964]

        await update.message.reply_text('🎵 Song MMSUB ဗီဒီယိုများကို ပို့ဆောင်ပေးနေပါသည် ခဏစောင့်ပေးပါ...')

        for vid_id in video_ids:
            try:
                await context.bot.copy_message(
                    chat_id=update.message.chat_id,
                    from_chat_id=CHANNEL_USERNAME,
                    message_id=vid_id
                )
            except BadRequest:
                pass

    elif text == 'ToDo':
        keyboard = [
            [InlineKeyboardButton("2021", callback_data="todo_2021"), InlineKeyboardButton("2022", callback_data="todo_2022")],
            [InlineKeyboardButton("2023", callback_data="todo_2023"), InlineKeyboardButton("2024", callback_data="todo_2024")],
            [InlineKeyboardButton("2025", callback_data="todo_2025"), InlineKeyboardButton("2026", callback_data="todo_2026")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🎬 ကြည့်ရှုလိုသော ToDo နှစ်ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'T:Time':
        keyboard = [
            [InlineKeyboardButton("2025", callback_data="ttime_2025"), InlineKeyboardButton("2026", callback_data="ttime_2026")],
            [InlineKeyboardButton("2027", callback_data="ttime_2027")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('📹 ကြည့်ရှုလိုသော T:Time နှစ်ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'EPISODE':
        keyboard = [
            [InlineKeyboardButton("2019", callback_data="ep_2019"), InlineKeyboardButton("2020", callback_data="ep_2020")],
            [InlineKeyboardButton("2021", callback_data="ep_2021"), InlineKeyboardButton("2022", callback_data="ep_2022")],
            [InlineKeyboardButton("2023", callback_data="ep_2023"), InlineKeyboardButton("2024", callback_data="ep_2024")],
            [InlineKeyboardButton("2025", callback_data="ep_2025"), InlineKeyboardButton("2026", callback_data="ep_2026")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('✨ ကြည့်ရှုလိုသော EPISODE နှစ်ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'TxT-Log':
        keyboard = [
            [InlineKeyboardButton("2022", callback_data="log_2022"), InlineKeyboardButton("2023", callback_data="log_2023")],
            [InlineKeyboardButton("2024", callback_data="log_2024"), InlineKeyboardButton("2025", callback_data="log_2025")],
            [InlineKeyboardButton("2026", callback_data="log_2026")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🔴 ကြည့်ရှုလိုသော TxT-Log နှစ်ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'TxT Dream Week':
        keyboard = [
            [InlineKeyboardButton("2020", callback_data="dream_2020"), InlineKeyboardButton("2021", callback_data="dream_2021")],
            [InlineKeyboardButton("2022", callback_data="dream_2022"), InlineKeyboardButton("2023", callback_data="dream_2023")],
            [InlineKeyboardButton("2024", callback_data="dream_2024"), InlineKeyboardButton("2025", callback_data="dream_2025")],
            [InlineKeyboardButton("2026", callback_data="dream_2026")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('📺 ကြည့်ရှုလိုသော Dream Week နှစ်ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'Talk X Today':
        keyboard = [
            [InlineKeyboardButton("Season Zero", callback_data="talk_Season Zero"), InlineKeyboardButton("Season 1", callback_data="talk_Season 1")],
            [InlineKeyboardButton("Season 2", callback_data="talk_Season 2"), InlineKeyboardButton("Season 3", callback_data="talk_Season 3")],
            [InlineKeyboardButton("Season 4", callback_data="talk_Season 4"), InlineKeyboardButton("Season 5", callback_data="talk_Season 5")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🎤 ကြည့်ရှုလိုသော Season ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'TxT Content':
        keyboard = [
            [InlineKeyboardButton("ShouldWeRunAway?", callback_data="content_ShouldWeRunAway?")],
            [InlineKeyboardButton("Summer Diary", callback_data="content_Summer Diary")],
            [InlineKeyboardButton("Toob Cast 🎙️", callback_data="content_Toob Cast"), InlineKeyboardButton("More", callback_data="content_More")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('📺 ကြည့်ရှုလိုသော TxT Content ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'Behind':
        keyboard = [
            [InlineKeyboardButton("Stick with you", callback_data="behind_stick")],
            [InlineKeyboardButton("Setsuna Hanabi", callback_data="behind_setsuna")],
            [InlineKeyboardButton("More", callback_data="behind_more")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🎬 ကြည့်ရှုလိုသော Behind အပိုင်းကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'Solo Show':
        keyboard = [
            [InlineKeyboardButton("Yeonjun", callback_data="solo_Yeonjun"), InlineKeyboardButton("Soobin", callback_data="solo_Soobin")],
            [InlineKeyboardButton("Beomgyu", callback_data="solo_Beomgyu"), InlineKeyboardButton("Taehyun", callback_data="solo_Taehyun")],
            [InlineKeyboardButton("Huening Kai", callback_data="solo_Huening Kai")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🌟 ကြည့်ရှုလိုသော Member ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'Other Show':
        keyboard = [
            [InlineKeyboardButton("Idol 1N2D", callback_data="other_idol1n2d"), InlineKeyboardButton("Zip DaeSung", callback_data="other_zipdaesung")],
            [InlineKeyboardButton("Silence of Idol", callback_data="other_silence"), InlineKeyboardButton("Idol House", callback_data="other_idolhouse")],
            [InlineKeyboardButton("Idol Human Theater", callback_data="other_humantheater"), InlineKeyboardButton("Sumbakkokjil", callback_data="other_sumbakkokjil")],
            [InlineKeyboardButton("TXT Parenting Diary", callback_data="other_parenting"), InlineKeyboardButton("Secret Counseling", callback_data="other_counseling")],
            [InlineKeyboardButton("GoToTheSnackShopAfterInkigayo", callback_data="other_snackshop"), InlineKeyboardButton("More", callback_data="other_more")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('🎭 ကြည့်ရှုလိုသော Other Show ကို ရွေးချယ်ပါ -', reply_markup=reply_markup)

    elif text == 'Contact Admin':
        await update.message.reply_text('Admin များကို ဆက်သွယ်ရန် -\n@Hwang_hay_won (or) @Cordelia_Jju')

# ==============================================================
# WEBHOOK SETUP FOR PYTHONANYWHERE
# ==============================================================

app = Flask(__name__)

ptb_app = Application.builder().token(TOKEN).build()
ptb_app.add_handler(CommandHandler("start", start))
ptb_app.add_handler(CallbackQueryHandler(button_click))
ptb_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_click))

# (အရေးကြီး - Webhook ကို ပုံမှန်အတိုင်းချိတ်နိုင်ရန် route ကို '/' ဟု ပြင်ဆင်ထားပါသည်)
@app.route('/', methods=['POST', 'GET'])
def tg_webhook():
    if request.method == 'GET':
        return "TxT MMSUB Bot is running 24/7!"

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    json_str = request.get_json(force=True)
    update = Update.de_json(json_str, ptb_app.bot)

    async def process():
        if not ptb_app._initialized:
            await ptb_app.initialize()
        await ptb_app.process_update(update)

    loop.run_until_complete(process())

    return 'OK', 200


