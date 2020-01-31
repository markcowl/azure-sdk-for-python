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

try:
    from ._models_py3 import AttachedDatabaseConfiguration
    from ._models_py3 import AzureCapacity
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import AzureResourceSku
    from ._models_py3 import AzureSku
    from ._models_py3 import CheckNameRequest
    from ._models_py3 import CheckNameResult
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterCheckNameRequest
    from ._models_py3 import ClusterPrincipalAssignment
    from ._models_py3 import ClusterPrincipalAssignmentCheckNameRequest
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import Database
    from ._models_py3 import DatabasePrincipal
    from ._models_py3 import DatabasePrincipalAssignment
    from ._models_py3 import DatabasePrincipalAssignmentCheckNameRequest
    from ._models_py3 import DatabasePrincipalListRequest
    from ._models_py3 import DatabasePrincipalListResult
    from ._models_py3 import DatabaseStatistics
    from ._models_py3 import DataConnection
    from ._models_py3 import DataConnectionCheckNameRequest
    from ._models_py3 import DataConnectionValidation
    from ._models_py3 import DataConnectionValidationListResult
    from ._models_py3 import DataConnectionValidationResult
    from ._models_py3 import DiagnoseVirtualNetworkResult
    from ._models_py3 import EventGridDataConnection
    from ._models_py3 import EventHubDataConnection
    from ._models_py3 import FollowerDatabaseDefinition
    from ._models_py3 import Identity
    from ._models_py3 import IdentityUserAssignedIdentitiesValue
    from ._models_py3 import IotHubDataConnection
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import LanguageExtension
    from ._models_py3 import LanguageExtensionsList
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OptimizedAutoscale
    from ._models_py3 import ProxyResource
    from ._models_py3 import ReadOnlyFollowingDatabase
    from ._models_py3 import ReadWriteDatabase
    from ._models_py3 import Resource
    from ._models_py3 import SkuDescription
    from ._models_py3 import SkuLocationInfoItem
    from ._models_py3 import TrackedResource
    from ._models_py3 import TrustedExternalTenant
    from ._models_py3 import VirtualNetworkConfiguration
except (SyntaxError, ImportError):
    from ._models import AttachedDatabaseConfiguration
    from ._models import AzureCapacity
    from ._models import AzureEntityResource
    from ._models import AzureResourceSku
    from ._models import AzureSku
    from ._models import CheckNameRequest
    from ._models import CheckNameResult
    from ._models import Cluster
    from ._models import ClusterCheckNameRequest
    from ._models import ClusterPrincipalAssignment
    from ._models import ClusterPrincipalAssignmentCheckNameRequest
    from ._models import ClusterUpdate
    from ._models import Database
    from ._models import DatabasePrincipal
    from ._models import DatabasePrincipalAssignment
    from ._models import DatabasePrincipalAssignmentCheckNameRequest
    from ._models import DatabasePrincipalListRequest
    from ._models import DatabasePrincipalListResult
    from ._models import DatabaseStatistics
    from ._models import DataConnection
    from ._models import DataConnectionCheckNameRequest
    from ._models import DataConnectionValidation
    from ._models import DataConnectionValidationListResult
    from ._models import DataConnectionValidationResult
    from ._models import DiagnoseVirtualNetworkResult
    from ._models import EventGridDataConnection
    from ._models import EventHubDataConnection
    from ._models import FollowerDatabaseDefinition
    from ._models import Identity
    from ._models import IdentityUserAssignedIdentitiesValue
    from ._models import IotHubDataConnection
    from ._models import KeyVaultProperties
    from ._models import LanguageExtension
    from ._models import LanguageExtensionsList
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OptimizedAutoscale
    from ._models import ProxyResource
    from ._models import ReadOnlyFollowingDatabase
    from ._models import ReadWriteDatabase
    from ._models import Resource
    from ._models import SkuDescription
    from ._models import SkuLocationInfoItem
    from ._models import TrackedResource
    from ._models import TrustedExternalTenant
    from ._models import VirtualNetworkConfiguration
from ._paged_models import AttachedDatabaseConfigurationPaged
from ._paged_models import AzureResourceSkuPaged
from ._paged_models import ClusterPaged
from ._paged_models import ClusterPrincipalAssignmentPaged
from ._paged_models import DatabasePaged
from ._paged_models import DatabasePrincipalAssignmentPaged
from ._paged_models import DatabasePrincipalPaged
from ._paged_models import DataConnectionPaged
from ._paged_models import FollowerDatabaseDefinitionPaged
from ._paged_models import LanguageExtensionPaged
from ._paged_models import OperationPaged
from ._paged_models import SkuDescriptionPaged
from ._kusto_management_client_enums import (
    State,
    ProvisioningState,
    AzureSkuName,
    AzureSkuTier,
    AzureScaleType,
    DefaultPrincipalsModificationKind,
    PrincipalsModificationKind,
    EventHubDataFormat,
    Compression,
    IotHubDataFormat,
    EventGridDataFormat,
    IdentityType,
    DatabasePrincipalRole,
    DatabasePrincipalType,
    PrincipalType,
    ClusterPrincipalRole,
    Type,
    Reason,
    LanguageExtensionName,
)

__all__ = [
    'AttachedDatabaseConfiguration',
    'AzureCapacity',
    'AzureEntityResource',
    'AzureResourceSku',
    'AzureSku',
    'CheckNameRequest',
    'CheckNameResult',
    'Cluster',
    'ClusterCheckNameRequest',
    'ClusterPrincipalAssignment',
    'ClusterPrincipalAssignmentCheckNameRequest',
    'ClusterUpdate',
    'Database',
    'DatabasePrincipal',
    'DatabasePrincipalAssignment',
    'DatabasePrincipalAssignmentCheckNameRequest',
    'DatabasePrincipalListRequest',
    'DatabasePrincipalListResult',
    'DatabaseStatistics',
    'DataConnection',
    'DataConnectionCheckNameRequest',
    'DataConnectionValidation',
    'DataConnectionValidationListResult',
    'DataConnectionValidationResult',
    'DiagnoseVirtualNetworkResult',
    'EventGridDataConnection',
    'EventHubDataConnection',
    'FollowerDatabaseDefinition',
    'Identity',
    'IdentityUserAssignedIdentitiesValue',
    'IotHubDataConnection',
    'KeyVaultProperties',
    'LanguageExtension',
    'LanguageExtensionsList',
    'Operation',
    'OperationDisplay',
    'OptimizedAutoscale',
    'ProxyResource',
    'ReadOnlyFollowingDatabase',
    'ReadWriteDatabase',
    'Resource',
    'SkuDescription',
    'SkuLocationInfoItem',
    'TrackedResource',
    'TrustedExternalTenant',
    'VirtualNetworkConfiguration',
    'FollowerDatabaseDefinitionPaged',
    'ClusterPaged',
    'SkuDescriptionPaged',
    'AzureResourceSkuPaged',
    'LanguageExtensionPaged',
    'ClusterPrincipalAssignmentPaged',
    'DatabasePaged',
    'DatabasePrincipalPaged',
    'DatabasePrincipalAssignmentPaged',
    'AttachedDatabaseConfigurationPaged',
    'DataConnectionPaged',
    'OperationPaged',
    'State',
    'ProvisioningState',
    'AzureSkuName',
    'AzureSkuTier',
    'AzureScaleType',
    'DefaultPrincipalsModificationKind',
    'PrincipalsModificationKind',
    'EventHubDataFormat',
    'Compression',
    'IotHubDataFormat',
    'EventGridDataFormat',
    'IdentityType',
    'DatabasePrincipalRole',
    'DatabasePrincipalType',
    'PrincipalType',
    'ClusterPrincipalRole',
    'Type',
    'Reason',
    'LanguageExtensionName',
]
