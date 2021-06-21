import logging

from requests import HTTPError

from pajbot.models.command import Command
from pajbot.models.command import CommandExample
from pajbot.modules import BaseModule
from pajbot.modules import ModuleSetting
from pajbot.modules.basic import BasicCommandsModule
from pajbot.streamhelper import StreamHelper

log = logging.getLogger("pajbot")


class StreamScheduleModule(BaseModule):
    ID = __name__.split(".")[-1]
    NAME = "Stream Schedule"
    DESCRIPTION = "Enables the usage of the !schedule command"
    CATEGORY = "Feature"
    PARENT_MODULE = BasicCommandsModule
    SETTINGS = [
        ModuleSetting(
            key="utc_offset",
            label = "A timezone offset for the requester specified in minutes. For example, a timezone that is +4 hours from GMT would be “240.” If not specified, “0” is used for GMT.",
            type="number",
            required=False,
            placeholder="",
            default=0,
            constraints={"min_value": -726, "max_value": 840} # -726 = UTC-11, 840 = UTC+14
        ),
        ModuleSetting(
            key="global_cd",
            label="Global cooldown (seconds)",
            type="number",
            required=True,
            placeholder="",
            default=5,
            constraints={"min_value": 0, "max_value": 120},
        ),
        ModuleSetting(
            key="user_cd",
            label="Per-user cooldown (seconds)",
            type="number",
            required=True,
            placeholder="",
            default=15,
            constraints={"min_value": 0, "max_value": 240},
        ),
        ModuleSetting(
            key="level",
            label="Level required to use the command",
            type="number",
            required=True,
            placeholder="",
            default=100,
            constraints={"min_value": 100, "max_value": 2000},
        ),
        ModuleSetting(
            key="normal_response",
            label="Standard response containing the stream schedule | Available arguments: {source}, {streamer}, {start_time}, {title}, {category}, {time_until_start}",
            type="text",
            required=True,
            placeholder="",
            default="{source}, {streamer} is going to stream {category} in {time_until_start}",
            constraints={"max_str_len": 400},
        ),
        ModuleSetting(
            key="vacation_response",
            label="Vacation response containting the finish vacation time | Available arguments: {source}, {streamer}, {start_time}, {title}, {category}, {time_until_start}, {vacation_start_time}, {vacation_end_time}",
            type="text",
            required=True,
            placeholder="",
            default="{source}, {streamer} is currently on vacation and is due to return {vacation_end_time}.",
            constraints={"max_str_len": 400},
        ),
        ModuleSetting(
            key="midstream_response",
            label="Midstreeam response containing the finish stream time | Available arguments: {source}, {streamer}, {end_time}, {time_until_end}",
            type="text",
            required=True,
            placeholder="",
            default="{source}, {streamer} is due to end stream in {time_until_end}.",
            constraints={"max_str_len": 400},
        )
    ]
