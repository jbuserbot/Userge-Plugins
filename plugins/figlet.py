# by Alone and krishna

from pyfiglet import Figlet

from userge import userge, Message


@userge.on_cmd("figlet", about={
    'header': "Figlet",
    'description': "Make Fancy Style text using Figlet",
    'usage': "{tr}figlet font_name | [text | reply]",
    'Fonts': "<code>Check this</code> "
             "<a href='https://telegra.ph/Figlet-List-Of-Fonts-07-03'>link</a>"
             " <code>to know available fonts</code>"})
async def figlet_(message: Message):
    args = message.input_or_reply_str
    if not args:
        await message.edit(
            "**Do You think this is Funny?**\n\n"
            "__Try this Blek Mejik:__\n\n"
            "```.help .figlet```")
        await message.reply_sticker(sticker="CAADBAAD1AIAAnV4kzMWpUTkTJ9JwRYE")
        return
    if "|" in message.input_or_reply_str:
        style, text = message.input_str.split('|')
        custom_fig = Figlet(font=style.strip())
        await message.edit(f"```{custom_fig.renderText(text.strip())}```")
        return
    str_ = ' '.join(args)
    custom_fig = Figlet(font='threepoint')
    await message.edit(f"```{custom_fig.renderText(str_)}```")
