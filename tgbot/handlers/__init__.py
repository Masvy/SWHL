from .start import start_router
from .new_command import command_router
# from .new_player import player_router
from .admin import admin_router

routers_list = [
    start_router,
    command_router,
    # player_router,
    admin_router,
]

__all__ = [
    'routers_list',
]
