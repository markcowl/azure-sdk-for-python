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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class FrontendEndpointsOperations(object):
    """FrontendEndpointsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2020-01-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-01-01"

        self.config = config

    def list_by_front_door(
            self, resource_group_name, front_door_name, custom_headers=None, raw=False, **operation_config):
        """Lists all of the frontend endpoints within a Front Door.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally
         unique.
        :type front_door_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of FrontendEndpoint
        :rtype:
         ~azure.mgmt.frontdoor.models.FrontendEndpointPaged[~azure.mgmt.frontdoor.models.FrontendEndpoint]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_front_door.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
                    'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.FrontendEndpointPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_front_door.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints'}

    def get(
            self, resource_group_name, front_door_name, frontend_endpoint_name, custom_headers=None, raw=False, **operation_config):
        """Gets a Frontend endpoint with the specified name within the specified
        Front Door.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally
         unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is
         unique within the Front Door.
        :type frontend_endpoint_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FrontendEndpoint or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.frontdoor.models.FrontendEndpoint or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FrontendEndpoint', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}'}


    def _enable_https_initial(
            self, resource_group_name, front_door_name, frontend_endpoint_name, custom_https_configuration, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.enable_https.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(custom_https_configuration, 'CustomHttpsConfiguration')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def enable_https(
            self, resource_group_name, front_door_name, frontend_endpoint_name, custom_https_configuration, custom_headers=None, raw=False, polling=True, **operation_config):
        """Enables a frontendEndpoint for HTTPS traffic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally
         unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is
         unique within the Front Door.
        :type frontend_endpoint_name: str
        :param custom_https_configuration: The configuration specifying how to
         enable HTTPS
        :type custom_https_configuration:
         ~azure.mgmt.frontdoor.models.CustomHttpsConfiguration
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        raw_result = self._enable_https_initial(
            resource_group_name=resource_group_name,
            front_door_name=front_door_name,
            frontend_endpoint_name=frontend_endpoint_name,
            custom_https_configuration=custom_https_configuration,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    enable_https.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/enableHttps'}


    def _disable_https_initial(
            self, resource_group_name, front_door_name, frontend_endpoint_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.disable_https.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def disable_https(
            self, resource_group_name, front_door_name, frontend_endpoint_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Disables a frontendEndpoint for HTTPS traffic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally
         unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is
         unique within the Front Door.
        :type frontend_endpoint_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        raw_result = self._disable_https_initial(
            resource_group_name=resource_group_name,
            front_door_name=front_door_name,
            frontend_endpoint_name=frontend_endpoint_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    disable_https.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/disableHttps'}
