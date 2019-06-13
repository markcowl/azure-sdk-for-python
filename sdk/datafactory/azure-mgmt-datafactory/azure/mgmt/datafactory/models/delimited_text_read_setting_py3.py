# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .format_read_setting_py3 import FormatReadSetting


class DelimitedTextReadSetting(FormatReadSetting):
    """Delimited text read settings.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Required. The read setting type.
    :type type: str
    :param skip_line_count: Indicates the number of non-empty rows to skip
     when reading data from input files. Type: integer (or Expression with
     resultType integer).
    :type skip_line_count: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'skip_line_count': {'key': 'skipLineCount', 'type': 'object'},
    }

    def __init__(self, *, type: str, additional_properties=None, skip_line_count=None, **kwargs) -> None:
        super(DelimitedTextReadSetting, self).__init__(additional_properties=additional_properties, type=type, **kwargs)
        self.skip_line_count = skip_line_count
