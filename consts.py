from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
    welcome_msg = '''<b>Bot'a Hoş Geldiniz</b>👋
    <i>DP'lerini almak için bana herhangi birinin instagram kullanıcı adını veya profil URL'sini gönderin</i>
    ör: <b>goturkiye</b> , <b>acunilicali</b> vb.'''

    return welcome_msg


def acc_type(val):
    if(val):
        return "🔒Gizli🔒"
    else:
        return "🔓Açık🔓"

def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            try:
                data = data.split("?")
                return data[0]
            except Exception:
                return "incorrect format"
        return data
    except Exception:
        return "incorrect format"


def create_caption(user):
    caption_msg = f'''⭐*İsim*⭐: {es(user.full_name,version=2)} \n⭐*Takipçi*⭐: {es(str(user.followers),version=2)} \n⭐*Takip Edilen*⭐: {es(str(user.followees),version=2)}\
        \n⭐*Hesap Tipi*⭐: {acc_type(user.is_private)} \n\nBotu kullandığınız için teşekkürler!'''

    return caption_msg




ratingkey = [[InlineKeyboardButton(
    "Android Uygulamasını İndir", url="https://play.google.com/store/apps/details?id=com.mobuyg.ararim"
    )]]
