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


class Resource(Model):
    """The common properties of an ARM resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ARM resource identifier.
    :vartype id: str
    :ivar name: The ARM resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,99}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class App(Resource):
    """The IoT Central application.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ARM resource identifier.
    :vartype id: str
    :ivar name: The ARM resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :ivar application_id: The ID of the application.
    :vartype application_id: str
    :param display_name: The display name of the application.
    :type display_name: str
    :param subdomain: The subdomain of the application.
    :type subdomain: str
    :param template: The ID of the application template, which is a blueprint
     that defines the characteristics and behaviors of an application.
     Optional; if not specified, defaults to a blank blueprint and allows the
     application to be defined from scratch.
    :type template: str
    :param sku: Required. A valid instance SKU.
    :type sku: ~azure.mgmt.iotcentral.models.AppSkuInfo
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,99}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'location': {'required': True},
        'application_id': {'readonly': True},
        'display_name': {'pattern': r'^.{1,200}$'},
        'subdomain': {'pattern': r'^[a-z0-9-]{1,63}$'},
        'sku': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'application_id': {'key': 'properties.applicationId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'subdomain': {'key': 'properties.subdomain', 'type': 'str'},
        'template': {'key': 'properties.template', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'AppSkuInfo'},
    }

    def __init__(self, *, location: str, sku, tags=None, display_name: str=None, subdomain: str=None, template: str=None, **kwargs) -> None:
        super(App, self).__init__(location=location, tags=tags, **kwargs)
        self.application_id = None
        self.display_name = display_name
        self.subdomain = subdomain
        self.template = template
        self.sku = sku


class AppAvailabilityInfo(Model):
    """The properties indicating whether a given IoT Central application name or
    subdomain is available.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: The value which indicates whether the provided name
     is available.
    :vartype name_available: bool
    :ivar reason: The reason for unavailability.
    :vartype reason: str
    :ivar message: The detailed reason message.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AppAvailabilityInfo, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None


class AppPatch(Model):
    """The description of the IoT Central application.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: Instance tags
    :type tags: dict[str, str]
    :ivar application_id: The ID of the application.
    :vartype application_id: str
    :param display_name: The display name of the application.
    :type display_name: str
    :param subdomain: The subdomain of the application.
    :type subdomain: str
    :param template: The ID of the application template, which is a blueprint
     that defines the characteristics and behaviors of an application.
     Optional; if not specified, defaults to a blank blueprint and allows the
     application to be defined from scratch.
    :type template: str
    """

    _validation = {
        'application_id': {'readonly': True},
        'display_name': {'pattern': r'^.{1,200}$'},
        'subdomain': {'pattern': r'^[a-z0-9-]{1,63}$'},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'application_id': {'key': 'properties.applicationId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'subdomain': {'key': 'properties.subdomain', 'type': 'str'},
        'template': {'key': 'properties.template', 'type': 'str'},
    }

    def __init__(self, *, tags=None, display_name: str=None, subdomain: str=None, template: str=None, **kwargs) -> None:
        super(AppPatch, self).__init__(**kwargs)
        self.tags = tags
        self.application_id = None
        self.display_name = display_name
        self.subdomain = subdomain
        self.template = template


class AppSkuInfo(Model):
    """Information about the SKU of the IoT Central application.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include: 'F1',
     'S1', 'ST0', 'ST1', 'ST2'
    :type name: str or ~azure.mgmt.iotcentral.models.AppSku
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name, **kwargs) -> None:
        super(AppSkuInfo, self).__init__(**kwargs)
        self.name = name


class AppTemplate(Model):
    """IoT Central Application Template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar manifest_id: The ID of the template.
    :vartype manifest_id: str
    :ivar manifest_version: The version of the template.
    :vartype manifest_version: str
    :ivar app_template_name: The name of the template.
    :vartype app_template_name: str
    :ivar title: The title of the template.
    :vartype title: str
    :ivar order: The order of the template in the templates list.
    :vartype order: float
    :ivar description: The description of the template.
    :vartype description: str
    """

    _validation = {
        'manifest_id': {'readonly': True},
        'manifest_version': {'readonly': True},
        'app_template_name': {'readonly': True},
        'title': {'readonly': True},
        'order': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'str'},
        'app_template_name': {'key': 'appTemplateName', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'order': {'key': 'order', 'type': 'float'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AppTemplate, self).__init__(**kwargs)
        self.manifest_id = None
        self.manifest_version = None
        self.app_template_name = None
        self.title = None
        self.order = None
        self.description = None


class CloudError(Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.iotcentral.models.ErrorResponseBody]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'error.code', 'type': 'str'},
        'message': {'key': 'error.message', 'type': 'str'},
        'target': {'key': 'error.target', 'type': 'str'},
        'details': {'key': 'error.details', 'type': '[ErrorResponseBody]'},
    }

    def __init__(self, *, details=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = details


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class ErrorResponseBody(Model):
    """Details of error response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.iotcentral.models.ErrorResponseBody]
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
        'details': {'key': 'details', 'type': '[ErrorResponseBody]'},
    }

    def __init__(self, *, details=None, **kwargs) -> None:
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = details


class Operation(Model):
    """IoT Central REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{read | write | action |
     delete}
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.iotcentral.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, *, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class OperationDisplay(Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft IoT Central
    :vartype provider: str
    :ivar resource: Resource Type: IoT Central
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

    def __init__(self, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationInputs(Model):
    """Input values.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the IoT Central application instance to
     check.
    :type name: str
    :param type: The type of the IoT Central resource to query. Default value:
     "IoTApps" .
    :type type: str
    """

    _validation = {
        'name': {'required': True, 'pattern': r'^[a-z0-9-]{1,63}$'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, name: str, type: str="IoTApps", **kwargs) -> None:
        super(OperationInputs, self).__init__(**kwargs)
        self.name = name
        self.type = type
