from hydrogram.handlers.callback_query_handler import CallbackQueryHandler
from hydrogram.handlers.chat_join_request_handler import ChatJoinRequestHandler
from hydrogram.handlers.chat_member_updated_handler import \
    ChatMemberUpdatedHandler
from hydrogram.handlers.chosen_inline_result_handler import \
    ChosenInlineResultHandler
from hydrogram.handlers.deleted_messages_handler import DeletedMessagesHandler
from hydrogram.handlers.disconnect_handler import DisconnectHandler
from hydrogram.handlers.edited_message_handler import EditedMessageHandler
from hydrogram.handlers.inline_query_handler import InlineQueryHandler
from hydrogram.handlers.message_handler import MessageHandler
from hydrogram.handlers.poll_handler import PollHandler
from hydrogram.handlers.raw_update_handler import RawUpdateHandler
from hydrogram.handlers.user_status_handler import UserStatusHandler


class OnUpdateMiddleware:
    """middleware for all"""

    def __eq__(self, other) -> bool:
        return True


class OnEditedMessageMiddleware:
    """middleware for on_edited_message"""

    def __eq__(self, other) -> bool:
        return other == EditedMessageHandler


class OnUserStatusMiddleware:
    """middleware for on_user_status"""

    def __eq__(self, other) -> bool:
        return other == UserStatusHandler


class OnRawUpdateMiddleware:
    """middleware for on_raw_update"""

    def __eq__(self, other) -> bool:
        return other == RawUpdateHandler


class OnChosenInlineResultMiddleware:
    """middleware for on_chosen_inline_result"""

    def __eq__(self, other) -> bool:
        return other == ChosenInlineResultHandler


class OnDeletedMessagesMiddleware:
    """middleware for on_deleted_messages"""

    def __eq__(self, other) -> bool:
        return other == DeletedMessagesHandler


class OnChatMemberUpdatedMiddleware:
    """middleware for on_chat_member_updated"""

    def __eq__(self, other) -> bool:
        return other == ChatMemberUpdatedHandler


class OnChatJoinRequestMiddleware:
    """middleware for on_chat_join_request"""

    def __eq__(self, other) -> bool:
        return other == ChatJoinRequestHandler


class OnCallbackQueryMiddleware:
    """middleware for on_callback_query"""

    def __eq__(self, other) -> bool:
        return other == CallbackQueryHandler


class OnInlineQueryMiddleware:
    """middleware for on_inline_query"""

    def __eq__(self, other) -> bool:
        return other == InlineQueryHandler


class OnDisconnectMiddleware:
    """middleware for on_disconnect"""

    def __eq__(self, other) -> bool:
        return other == DisconnectHandler


class OnMessageMiddleware:
    """middleware for on_message"""

    def __eq__(self, other) -> bool:
        return other == MessageHandler


class OnPoolMiddleware:
    """middleware for on_pool"""

    def __eq__(self, other) -> bool:
        return other == PollHandler


class MixedMiddleware:
    """pass the types of handlers from hydrogram.handlers during initialization that the malware will process

    patch_manager.include_middleware(CheckIgnoreMiddleware((MessageHandler, EditedMessageHandler), False))


    class CheckIgnoreMiddleware(MixedMiddleware):
    def __init__(self, handlers: tuple, ignore: bool) -> None:
        self.ignore = ignore  # it can be any value you want
        super().__init__(handlers)
    """

    def __init__(self, handlers: tuple) -> None:
        self._handlers = handlers

    def __eq__(self, other) -> bool:
        return other in self._handlers
