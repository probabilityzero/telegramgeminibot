 Telegram API sends an Update object. It can contain many optional fields.

Update (top-level)

update_id
Message-like fields (each optional; only one per update usually)

message (normal Message)
edited_message
channel_post
edited_channel_post
business_message (Message with business_connection_id)
inline_query
chosen_inline_result
callback_query
shipping_query
pre_checkout_query
poll
poll_answer
my_chat_member
chat_member
chat_join_request
(plus future/less common fields)
Message object (fields you commonly get)

message_id, date
from (User) — sender of the message
chat (Chat) — chat metadata (id, type, title, username, first_name, last_name)
text, entities, caption
reply_to_message
forward_from, forward_from_chat, forward_date, is_automatic_forward
edit_date
media fields: photo, audio, document, video, voice, animation, sticker, video_note
location, venue, contact
poll, dice
new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo
pinned_message
invoice, successful_payment
reply_markup (inline keyboard etc.)
media_group_id, author_signature, sender_chat
Business-specific

business_message.business_connection_id
business_message.chat (user chat object)
business_message.from / text / date / message_id (same shape as Message)
User object

id, is_bot, first_name, last_name, username, language_code, is_premium, added_to_attachment_menu, etc.
Chat object

id, type (private/group/supergroup/channel), title, username, first_name, last_name, permissions, photo, bio, linked_chat_id, etc.
CallbackQuery / InlineQuery / Poll / ChatMember / PreCheckout etc.

each has its own fields (id, from, chat_instance, data for callbacks; id, from, query for inline queries; poll id/results for polls; update-specific data for payments/chat member changes)
Where to see canonical docs

Telegram Bot API: https://core.telegram.org/bots/api#update
python-telegram-bot types: https://docs.python-telegram-bot.org/ (classes mirror the API)