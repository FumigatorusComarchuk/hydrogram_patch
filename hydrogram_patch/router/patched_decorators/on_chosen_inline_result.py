#  hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of hydrogram.
#
#  hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Callable

import hydrogram

import hydrogram_patch


class OnChosenInlineResult:
    def chosen_inline_result(self=None, filters=None, group: int = 0) -> Callable:
        """Decorator for handling chosen inline results.

        This does the same thing as :meth:`~hydrogram.Client.add_handler` using the
        :obj:`~hydrogram.handlers.ChosenInlineResultHandler`.

        Parameters:
            filters (:obj:`~hydrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of chosen inline results to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, HydroPatch.router.Router):
                if self._app is not None:
                    self._app.add_handler(
                        hydrogram.handlers.ChosenInlineResultHandler(
                            func, filters), group
                    )
                else:
                    self._decorators_storage.append(
                        (hydrogram.handlers.ChosenInlineResultHandler(func, filters), group))
            else:
                raise RuntimeError(
                    "you should only use this in routers, and only as a decorator"
                )

            return func

        return decorator
