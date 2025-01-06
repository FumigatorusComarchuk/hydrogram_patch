from hydrogram import Client

from hydrogram_patch.fsm import BaseStorage
from .patch_data_pool import PatchDataPool

from .dispatcher import PatchedDispatcher
from .router import Router


class PatchManager:
    def __init__(self, client: Client):
        self.client = client
        self.dispatcher = client.dispatcher

    def include_middleware(self, middleware: "PatchMiddleware") -> None:
        PatchDataPool.hydrogram_patch_middlewares.append(middleware)

    def include_outer_middleware(self, middleware: "PatchMiddleware") -> None:
        PatchDataPool.hydrogram_patch_outer_middlewares.append(middleware)

    def set_storage(self, storage: BaseStorage) -> None:
        PatchDataPool.hydrogram_patch_fsm_storage = storage

    def include_router(self, router: Router) -> None:
        router.set_client(self.client)


def patch(app: Client) -> PatchManager:
    """app - instance of your hydrogram client
    returns
    MiddlewarePatchManager instance with methods:
    include_middleware and include_outer_middleware
    """
    app.__delattr__("dispatcher")
    app.dispatcher = PatchedDispatcher(app)
    return PatchManager(app)
