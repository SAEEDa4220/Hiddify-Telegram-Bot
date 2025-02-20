# Description: This file contains all the reply and inline keyboard markups used in the bot.
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from AdminBot.buttons import KEY_MARKUP
from AdminBot.messages import MESSAGES
from config import CLIENT_TOKEN


# Main Menu Reply Keyboard Markup
def main_menu_keyboard_markup():
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['USERS_LIST']))
    markup.add(KeyboardButton(KEY_MARKUP['USERS_SEARCH']), KeyboardButton(KEY_MARKUP['ADD_USER']))
    if CLIENT_TOKEN:
        markup.add(KeyboardButton(KEY_MARKUP['USERS_BOT_MANAGEMENT']))
    markup.add()
    markup.add(KeyboardButton(KEY_MARKUP['SERVER_STATUS']), KeyboardButton(KEY_MARKUP['ABOUT_BOT']),
               KeyboardButton(KEY_MARKUP['SERVER_BACKUP']))

    return markup


# Users List Inline Keyboard Markup
def users_list_markup(users, page=1):
    markup = InlineKeyboardMarkup(row_width=3)
    USER_PER_PAGE = 20
    start = (page - 1) * USER_PER_PAGE
    end = start + USER_PER_PAGE
    keys = []
    for user in users[start:end]:
        keys.append(InlineKeyboardButton(user['name'], callback_data=f"info:{user['uuid']}"))
    markup.add(*keys)
    if page < len(users) / USER_PER_PAGE:
        markup.add(InlineKeyboardButton(KEY_MARKUP['NEXT_PAGE'], callback_data=f"next:{page + 1}"), row_width=2)
    if page > 1:
        markup.add(InlineKeyboardButton(KEY_MARKUP['PREV_PAGE'], callback_data=f"next:{page - 1}"), row_width=1)
    return markup


# Single User Inline Keyboard Markup
def user_info_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_USER'], callback_data=f"user_config:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_USER'], callback_data=f"user_edit:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['DELETE_USER'], callback_data=f"user_delete:{uuid}"))
    return markup


# Single User Edit Inline Keyboard Markup
def edit_user_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_NAME'], callback_data=f"user_edit_name:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_USAGE'], callback_data=f"user_edit_usage:{uuid}"),
               InlineKeyboardButton(KEY_MARKUP['RESET_USAGE'], callback_data=f"user_edit_reset_usage:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_DAYS'], callback_data=f"user_edit_days:{uuid}"),
               InlineKeyboardButton(KEY_MARKUP['RESET_DAYS'], callback_data=f"user_edit_reset_days:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['EDIT_COMMENT'], callback_data=f"user_edit_comment:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['UPDATE_MESSAGE'], callback_data=f"user_edit_update:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_user_panel:{uuid}"))
    return markup


# Add User Reply Keyboard Markup
def while_add_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Edit User Reply Keyboard Markup
def while_edit_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Confirm Add User Reply Keyboard Markup
def confirm_add_user_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(KEY_MARKUP['CONFIRM']))
    markup.add(KeyboardButton(KEY_MARKUP['CANCEL']))
    return markup


# Subscription URL Inline Keyboard Markup
def sub_url_user_list_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_DIR'], callback_data=f"conf_dir:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SUB'], callback_data=f"conf_sub_url:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_SUB_B64'], callback_data=f"conf_sub_url_b64:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_CLASH'], callback_data=f"conf_clash:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['CONFIGS_HIDDIFY'], callback_data=f"conf_hiddify:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_user_panel:{uuid}"))

    return markup


# Subscription Configs Inline Keyboard Markup
def sub_user_list_markup(uuid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Vless', callback_data=f"conf_dir_vless:{uuid}"))
    markup.add(InlineKeyboardButton('Vmess', callback_data=f"conf_dir_vmess:{uuid}"))
    markup.add(InlineKeyboardButton('Trojan', callback_data=f"conf_dir_trojan:{uuid}"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['BACK'], callback_data=f"back_to_user_panel:{uuid}"))
    return markup


# Search User Inline Keyboard Markup
def search_user_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_NAME'], callback_data=f"search_name:name"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_UUID'], callback_data=f"search_uuid:uuid"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_USER_CONFIG'], callback_data=f"search_config:config"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['SEARCH_EXPIRED_USERS'], callback_data=f"search_expired:expired"))
    return markup


# Users Bot Management - Inline Keyboard Markup
def users_bot_management_markup(value=None):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton(KEY_MARKUP['USERS_BOT_ORDERS_STATUS'], callback_data=f"users_bot_orders_status:None"),
        InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SUB_STATUS'], callback_data=f"users_bot_sub_status:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_ADD_PLAN'], callback_data=f"users_bot_add_plan:None"),
               InlineKeyboardButton(KEY_MARKUP['USERS_BOT_DEL_PLAN'], callback_data=f"users_bot_list_plans:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SEND_MESSAGE_TO_USERS'],
                                    callback_data=f"users_bot_send_msg_users:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO'], callback_data=f"users_bot_owner_info:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_SETTINGS'], callback_data=f"users_bot_settings:None"))
    return markup


# Users Bot Management - Settings - Inline Keyboard Markup
def users_bot_management_settings_markup(settings):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    status_hyperlink = "✅" if settings['visible_hiddify_hyperlink'] else "❌"
    markup.add(InlineKeyboardButton(f"{KEY_MARKUP['USERS_BOT_SETTINGS_SHOW_HIDI_LINK']} | {status_hyperlink}",
                                    callback_data=f"users_bot_settings_hyperlink:{settings['visible_hiddify_hyperlink']}"))
    return markup


# Users Bot Management - Edit Owner Info - Inline Keyboard Markup
def users_bot_edit_owner_info_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_USERNAME'],
                                    callback_data=f"users_bot_owner_info_edit_username:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_CARD_NUMBER'],
                                    callback_data=f"users_bot_owner_info_edit_card_number:None"))
    markup.add(InlineKeyboardButton(KEY_MARKUP['USERS_BOT_OWNER_INFO_EDIT_CARD_NAME'],
                                    callback_data=f"users_bot_owner_info_edit_card_name:None"))
    return markup


# Users Bot Management - Plans List - Inline Keyboard Markup
def plans_list_markup(plans):
    markup = InlineKeyboardMarkup(row_width=1)
    keys = []
    for plan in plans:
        if plan['status']:
            keys.append(InlineKeyboardButton(
                f"{plan['size_gb']}{MESSAGES['GB']} | {plan['days']}{MESSAGES['DAY']} | {plan['price']}{MESSAGES['TOMAN']}",
                callback_data=f"users_bot_del_plan:{plan['id']}"))
    if len(keys) == 0:
        return None
    markup.add(*keys)
    return markup
