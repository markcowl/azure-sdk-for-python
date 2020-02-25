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

from msrest.paging import Paged


class RegistryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Registry <azure.mgmt.containerregistry.v2019_12_01_preview.models.Registry>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Registry]'}
    }

    def __init__(self, *args, **kwargs):

        super(RegistryPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.containerregistry.v2019_12_01_preview.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class OperationDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`OperationDefinition <azure.mgmt.containerregistry.v2019_12_01_preview.models.OperationDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OperationDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationDefinitionPaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.containerregistry.v2019_12_01_preview.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class ReplicationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Replication <azure.mgmt.containerregistry.v2019_12_01_preview.models.Replication>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Replication]'}
    }

    def __init__(self, *args, **kwargs):

        super(ReplicationPaged, self).__init__(*args, **kwargs)
class WebhookPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Webhook <azure.mgmt.containerregistry.v2019_12_01_preview.models.Webhook>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Webhook]'}
    }

    def __init__(self, *args, **kwargs):

        super(WebhookPaged, self).__init__(*args, **kwargs)
class EventPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Event <azure.mgmt.containerregistry.v2019_12_01_preview.models.Event>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Event]'}
    }

    def __init__(self, *args, **kwargs):

        super(EventPaged, self).__init__(*args, **kwargs)
