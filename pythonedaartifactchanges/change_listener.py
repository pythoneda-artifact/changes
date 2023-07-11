"""
pythonedaartifactchanges/change_listener.py

This file declares the ChangeListener class.

Copyright (C) 2023-today rydnr's pythoneda-artifact/changes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.event_emitter import EventEmitter
from pythoneda.event_listener import EventListener
from pythoneda.ports import Ports
from pythonedaartifacteventchanges.change_staged import ChangeStaged
from pythonedaartifacteventchanges.change_staging_requested import ChangeStagingRequested
from pythonedasharedgit.git_repo import GitRepo
from typing import List, Type

class ChangeListener(EventListener):
    """
    Reacts to change-related events.

    Class name: ChangeListener

    Responsibilities:
        - Reacts to ChangeStagingRequested.
        - Reacts to ChangeStaged.

    Collaborators:
        - ChangeStagingRequested: The event that triggers the staging process.
        - ChangeStaged: The notification of a change been staged.
    """

    @classmethod
    def supported_events(cls) -> List[Type[Event]]:
        """
        Retrieves the list of supported event classes.
        :return: Such list.
        :rtype: List[Type[Event]]
        """
        return [ ChangeStagingRequested ]


    @classmethod
    async def listen_ChangeStagingRequested(cls, event: ChangeStagingRequested) -> ChangeStaged:
        """
        Gets notified of a new tag.
        :param event: The ChangeStagingRequested event.
        :type event: pythonedaartifacteventchanges.change_staging_requested.ChangeStagingRequested
        :return: The event of the change been staged.
        :rtype: pythonedaartifacteventchanges.change_staged.ChangeStaged
        """
        return None
