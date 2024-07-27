from dataclasses import dataclass
from typing import Union
from HydroPatch.fsm import BaseStorage
from contextlib import suppress


@dataclass()
class PatchDataPool:
    update_pool: dict
    hydrogram_patch_middlewares: list
    hydrogram_patch_outer_middlewares: list
    hydrogram_patch_fsm_storage: Union[BaseStorage, None]

    @staticmethod
    def include_helper_to_pool(update, patch_helper) -> None:
        PatchDataPool.update_pool[id(update)] = patch_helper

    @staticmethod
    def exclude_helper_from_pool(update) -> None:
        with suppress(KeyError):
            PatchDataPool.update_pool.pop(id(update))

    @staticmethod
    def get_helper_from_pool(update) -> Union[object, None]:
        return PatchDataPool.update_pool[id(update)]


PatchDataPool.update_pool = {}
PatchDataPool.hydrogram_patch_middlewares = []
PatchDataPool.hydrogram_patch_outer_middlewares = []
PatchDataPool.hydrogram_patch_fsm_storage = None

