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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CheckNameAvailabilityParameters(Model):
    """Input values.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the service instance to check.
    :type name: str
    :param type: Required. The fully qualified resource type which includes
     provider namespace.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorDetails(Model):
    """Error details.

    :param error: Object containing error details.
    :type error: ~azure.mgmt.healthcareapis.models.ErrorDetailsInternal
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetailsInternal'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetails, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorDetailsException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorDetails'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorDetailsException, self).__init__(deserialize, response, 'ErrorDetails', *args)


class ErrorDetailsInternal(Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetailsInternal, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None


class Operation(Model):
    """Service REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{read | write | action |
     delete}
    :vartype name: str
    :ivar origin: Default value is 'user,system'.
    :vartype origin: str
    :param display: The information displayed about the operation.
    :type display: ~azure.mgmt.healthcareapis.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.origin = None
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft.HealthcareApis
    :vartype provider: str
    :ivar resource: Resource Type: Services
    :vartype resource: str
    :ivar operation: Name of the operation
    :vartype operation: str
    :ivar description: Friendly description for the operation,
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationResultsDescription(Model):
    """The properties indicating the operation result of an operation on a
    service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the operation returned.
    :vartype id: str
    :ivar name: The name of the operation result.
    :vartype name: str
    :ivar status: The status of the operation being performed. Possible values
     include: 'Canceled', 'Succeeded', 'Failed', 'Requested', 'Running'
    :vartype status: str or
     ~azure.mgmt.healthcareapis.models.OperationResultStatus
    :ivar start_time: The time that the operation was started.
    :vartype start_time: str
    :param properties: Additional properties of the operation result.
    :type properties: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'status': {'readonly': True},
        'start_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(OperationResultsDescription, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.status = None
        self.start_time = None
        self.properties = kwargs.get('properties', None)


class Resource(Model):
    """The common properties of a service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param kind: Required. The kind of the service. Possible values include:
     'fhir', 'fhir-Stu3', 'fhir-R4'
    :type kind: str or ~azure.mgmt.healthcareapis.models.Kind
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param etag: An etag associated with the resource, used for optimistic
     concurrency when editing it.
    :type etag: str
    :param identity: Setting indicating whether the service has a managed
     identity associated with it.
    :type identity: ~azure.mgmt.healthcareapis.models.ResourceIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^[a-z0-9][a-z0-9-]{1,21}[a-z0-9]$'},
        'type': {'readonly': True},
        'kind': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'Kind'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.kind = kwargs.get('kind', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.etag = kwargs.get('etag', None)
        self.identity = kwargs.get('identity', None)


class ResourceIdentity(Model):
    """Setting indicating whether the service has a managed identity associated
    with it.

    :param type: Type of identity being specified, currently SystemAssigned
     and None are allowed. Possible values include: 'SystemAssigned', 'None'
    :type type: str or
     ~azure.mgmt.healthcareapis.models.ManagedServiceIdentityType
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceIdentity, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)


class ServiceAccessPolicyEntry(Model):
    """An access policy entry.

    All required parameters must be populated in order to send to Azure.

    :param object_id: Required. An Azure AD object ID (User or Apps) that is
     allowed access to the FHIR service.
    :type object_id: str
    """

    _validation = {
        'object_id': {'required': True, 'pattern': r'^(([0-9A-Fa-f]{8}[-]?(?:[0-9A-Fa-f]{4}[-]?){3}[0-9A-Fa-f]{12}){1})+$'},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceAccessPolicyEntry, self).__init__(**kwargs)
        self.object_id = kwargs.get('object_id', None)


class ServiceAuthenticationConfigurationInfo(Model):
    """Authentication configuration information.

    :param authority: The authority url for the service
    :type authority: str
    :param audience: The audience url for the service
    :type audience: str
    :param smart_proxy_enabled: If the SMART on FHIR proxy is enabled
    :type smart_proxy_enabled: bool
    """

    _attribute_map = {
        'authority': {'key': 'authority', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
        'smart_proxy_enabled': {'key': 'smartProxyEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ServiceAuthenticationConfigurationInfo, self).__init__(**kwargs)
        self.authority = kwargs.get('authority', None)
        self.audience = kwargs.get('audience', None)
        self.smart_proxy_enabled = kwargs.get('smart_proxy_enabled', None)


class ServiceCorsConfigurationInfo(Model):
    """The settings for the CORS configuration of the service instance.

    :param origins: The origins to be allowed via CORS.
    :type origins: list[str]
    :param headers: The headers to be allowed via CORS.
    :type headers: list[str]
    :param methods: The methods to be allowed via CORS.
    :type methods: list[str]
    :param max_age: The max age to be allowed via CORS.
    :type max_age: int
    :param allow_credentials: If credentials are allowed via CORS.
    :type allow_credentials: bool
    """

    _validation = {
        'max_age': {'maximum': 99999, 'minimum': 0},
    }

    _attribute_map = {
        'origins': {'key': 'origins', 'type': '[str]'},
        'headers': {'key': 'headers', 'type': '[str]'},
        'methods': {'key': 'methods', 'type': '[str]'},
        'max_age': {'key': 'maxAge', 'type': 'int'},
        'allow_credentials': {'key': 'allowCredentials', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ServiceCorsConfigurationInfo, self).__init__(**kwargs)
        self.origins = kwargs.get('origins', None)
        self.headers = kwargs.get('headers', None)
        self.methods = kwargs.get('methods', None)
        self.max_age = kwargs.get('max_age', None)
        self.allow_credentials = kwargs.get('allow_credentials', None)


class ServiceCosmosDbConfigurationInfo(Model):
    """The settings for the Cosmos DB database backing the service.

    :param offer_throughput: The provisioned throughput for the backing
     database.
    :type offer_throughput: int
    """

    _validation = {
        'offer_throughput': {'maximum': 10000, 'minimum': 400},
    }

    _attribute_map = {
        'offer_throughput': {'key': 'offerThroughput', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ServiceCosmosDbConfigurationInfo, self).__init__(**kwargs)
        self.offer_throughput = kwargs.get('offer_throughput', None)


class ServicesDescription(Resource):
    """The description of the service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param kind: Required. The kind of the service. Possible values include:
     'fhir', 'fhir-Stu3', 'fhir-R4'
    :type kind: str or ~azure.mgmt.healthcareapis.models.Kind
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param etag: An etag associated with the resource, used for optimistic
     concurrency when editing it.
    :type etag: str
    :param identity: Setting indicating whether the service has a managed
     identity associated with it.
    :type identity: ~azure.mgmt.healthcareapis.models.ResourceIdentity
    :param properties: The common properties of a service.
    :type properties: ~azure.mgmt.healthcareapis.models.ServicesProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^[a-z0-9][a-z0-9-]{1,21}[a-z0-9]$'},
        'type': {'readonly': True},
        'kind': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'Kind'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
        'properties': {'key': 'properties', 'type': 'ServicesProperties'},
    }

    def __init__(self, **kwargs):
        super(ServicesDescription, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ServicesNameAvailabilityInfo(Model):
    """The properties indicating whether a given service name is available.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: The value which indicates whether the provided name
     is available.
    :vartype name_available: bool
    :ivar reason: The reason for unavailability. Possible values include:
     'Invalid', 'AlreadyExists'
    :vartype reason: str or
     ~azure.mgmt.healthcareapis.models.ServiceNameUnavailabilityReason
    :param message: The detailed reason message.
    :type message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'ServiceNameUnavailabilityReason'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServicesNameAvailabilityInfo, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = kwargs.get('message', None)


class ServicesPatchDescription(Model):
    """The description of the service.

    :param tags: Instance tags
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ServicesPatchDescription, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class ServicesProperties(Model):
    """The properties of a service instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Deleting', 'Succeeded', 'Creating', 'Accepted', 'Verifying', 'Updating',
     'Failed', 'Canceled', 'Deprovisioned'
    :vartype provisioning_state: str or
     ~azure.mgmt.healthcareapis.models.ProvisioningState
    :param access_policies: Required. The access policies of the service
     instance.
    :type access_policies:
     list[~azure.mgmt.healthcareapis.models.ServiceAccessPolicyEntry]
    :param cosmos_db_configuration: The settings for the Cosmos DB database
     backing the service.
    :type cosmos_db_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceCosmosDbConfigurationInfo
    :param authentication_configuration: The authentication configuration for
     the service instance.
    :type authentication_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceAuthenticationConfigurationInfo
    :param cors_configuration: The settings for the CORS configuration of the
     service instance.
    :type cors_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceCorsConfigurationInfo
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'access_policies': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'access_policies': {'key': 'accessPolicies', 'type': '[ServiceAccessPolicyEntry]'},
        'cosmos_db_configuration': {'key': 'cosmosDbConfiguration', 'type': 'ServiceCosmosDbConfigurationInfo'},
        'authentication_configuration': {'key': 'authenticationConfiguration', 'type': 'ServiceAuthenticationConfigurationInfo'},
        'cors_configuration': {'key': 'corsConfiguration', 'type': 'ServiceCorsConfigurationInfo'},
    }

    def __init__(self, **kwargs):
        super(ServicesProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.access_policies = kwargs.get('access_policies', None)
        self.cosmos_db_configuration = kwargs.get('cosmos_db_configuration', None)
        self.authentication_configuration = kwargs.get('authentication_configuration', None)
        self.cors_configuration = kwargs.get('cors_configuration', None)
