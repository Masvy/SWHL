from .start import start_router
from .new_command import command_router
from .new_player import player_router

routers_list = [
    command_router,
    start_router,
    player_router,
]

__all__ = [
    'routers_list',
]
