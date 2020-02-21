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


class PeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Peering <azure.mgmt.peering.models.Peering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Peering]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.peering.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PeerAsnPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeerAsn <azure.mgmt.peering.models.PeerAsn>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeerAsn]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeerAsnPaged, self).__init__(*args, **kwargs)
class PeeringLocationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringLocation <azure.mgmt.peering.models.PeeringLocation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringLocation]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringLocationPaged, self).__init__(*args, **kwargs)
class PeeringRegisteredAsnPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringRegisteredAsn <azure.mgmt.peering.models.PeeringRegisteredAsn>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringRegisteredAsn]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringRegisteredAsnPaged, self).__init__(*args, **kwargs)
class PeeringRegisteredPrefixPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringRegisteredPrefix <azure.mgmt.peering.models.PeeringRegisteredPrefix>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringRegisteredPrefix]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringRegisteredPrefixPaged, self).__init__(*args, **kwargs)
class PeeringServiceCountryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringServiceCountry <azure.mgmt.peering.models.PeeringServiceCountry>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringServiceCountry]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringServiceCountryPaged, self).__init__(*args, **kwargs)
class PeeringServiceLocationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringServiceLocation <azure.mgmt.peering.models.PeeringServiceLocation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringServiceLocation]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringServiceLocationPaged, self).__init__(*args, **kwargs)
class PeeringServicePrefixPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringServicePrefix <azure.mgmt.peering.models.PeeringServicePrefix>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringServicePrefix]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringServicePrefixPaged, self).__init__(*args, **kwargs)
class PeeringServiceProviderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringServiceProvider <azure.mgmt.peering.models.PeeringServiceProvider>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringServiceProvider]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringServiceProviderPaged, self).__init__(*args, **kwargs)
class PeeringServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeeringService <azure.mgmt.peering.models.PeeringService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeeringService]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeeringServicePaged, self).__init__(*args, **kwargs)
