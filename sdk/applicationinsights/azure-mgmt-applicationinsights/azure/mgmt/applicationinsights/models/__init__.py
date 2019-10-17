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
    from ._models_py3 import Annotation
    from ._models_py3 import AnnotationError, AnnotationErrorException
    from ._models_py3 import APIKeyRequest
    from ._models_py3 import ApplicationInsightsComponent
    from ._models_py3 import ApplicationInsightsComponentAnalyticsItem
    from ._models_py3 import ApplicationInsightsComponentAnalyticsItemProperties
    from ._models_py3 import ApplicationInsightsComponentAPIKey
    from ._models_py3 import ApplicationInsightsComponentAvailableFeatures
    from ._models_py3 import ApplicationInsightsComponentBillingFeatures
    from ._models_py3 import ApplicationInsightsComponentDataVolumeCap
    from ._models_py3 import ApplicationInsightsComponentExportConfiguration
    from ._models_py3 import ApplicationInsightsComponentExportRequest
    from ._models_py3 import ApplicationInsightsComponentFavorite
    from ._models_py3 import ApplicationInsightsComponentFeature
    from ._models_py3 import ApplicationInsightsComponentFeatureCapabilities
    from ._models_py3 import ApplicationInsightsComponentFeatureCapability
    from ._models_py3 import ApplicationInsightsComponentProactiveDetectionConfiguration
    from ._models_py3 import ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions
    from ._models_py3 import ApplicationInsightsComponentQuotaStatus
    from ._models_py3 import ApplicationInsightsComponentWebTestLocation
    from ._models_py3 import ComponentPurgeBody
    from ._models_py3 import ComponentPurgeBodyFilters
    from ._models_py3 import ComponentPurgeResponse
    from ._models_py3 import ComponentPurgeStatusResponse
    from ._models_py3 import ComponentsResource
    from ._models_py3 import ErrorFieldContract
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import InnerError
    from ._models_py3 import LinkProperties
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import TagsResource
    from ._models_py3 import WebTest
    from ._models_py3 import WebTestGeolocation
    from ._models_py3 import WebTestPropertiesConfiguration
    from ._models_py3 import WebtestsResource
    from ._models_py3 import Workbook
    from ._models_py3 import WorkbookError, WorkbookErrorException
    from ._models_py3 import WorkbookResource
    from ._models_py3 import WorkItemConfiguration
    from ._models_py3 import WorkItemConfigurationError, WorkItemConfigurationErrorException
    from ._models_py3 import WorkItemCreateConfiguration
except (SyntaxError, ImportError):
    from ._models import Annotation
    from ._models import AnnotationError, AnnotationErrorException
    from ._models import APIKeyRequest
    from ._models import ApplicationInsightsComponent
    from ._models import ApplicationInsightsComponentAnalyticsItem
    from ._models import ApplicationInsightsComponentAnalyticsItemProperties
    from ._models import ApplicationInsightsComponentAPIKey
    from ._models import ApplicationInsightsComponentAvailableFeatures
    from ._models import ApplicationInsightsComponentBillingFeatures
    from ._models import ApplicationInsightsComponentDataVolumeCap
    from ._models import ApplicationInsightsComponentExportConfiguration
    from ._models import ApplicationInsightsComponentExportRequest
    from ._models import ApplicationInsightsComponentFavorite
    from ._models import ApplicationInsightsComponentFeature
    from ._models import ApplicationInsightsComponentFeatureCapabilities
    from ._models import ApplicationInsightsComponentFeatureCapability
    from ._models import ApplicationInsightsComponentProactiveDetectionConfiguration
    from ._models import ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions
    from ._models import ApplicationInsightsComponentQuotaStatus
    from ._models import ApplicationInsightsComponentWebTestLocation
    from ._models import ComponentPurgeBody
    from ._models import ComponentPurgeBodyFilters
    from ._models import ComponentPurgeResponse
    from ._models import ComponentPurgeStatusResponse
    from ._models import ComponentsResource
    from ._models import ErrorFieldContract
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import InnerError
    from ._models import LinkProperties
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import TagsResource
    from ._models import WebTest
    from ._models import WebTestGeolocation
    from ._models import WebTestPropertiesConfiguration
    from ._models import WebtestsResource
    from ._models import Workbook
    from ._models import WorkbookError, WorkbookErrorException
    from ._models import WorkbookResource
    from ._models import WorkItemConfiguration
    from ._models import WorkItemConfigurationError, WorkItemConfigurationErrorException
    from ._models import WorkItemCreateConfiguration
from ._paged_models import AnnotationPaged
from ._paged_models import ApplicationInsightsComponentAPIKeyPaged
from ._paged_models import ApplicationInsightsComponentPaged
from ._paged_models import ApplicationInsightsComponentWebTestLocationPaged
from ._paged_models import OperationPaged
from ._paged_models import WebTestPaged
from ._paged_models import WorkbookPaged
from ._paged_models import WorkItemConfigurationPaged
from ._application_insights_management_client_enums import (
    ItemScope,
    ItemType,
    ApplicationType,
    FlowType,
    RequestSource,
    PurgeState,
    FavoriteType,
    WebTestKind,
    SharedTypeKind,
    ItemScopePath,
    ItemTypeParameter,
    FavoriteSourceType,
    CategoryType,
)

__all__ = [
    'Annotation',
    'AnnotationError', 'AnnotationErrorException',
    'APIKeyRequest',
    'ApplicationInsightsComponent',
    'ApplicationInsightsComponentAnalyticsItem',
    'ApplicationInsightsComponentAnalyticsItemProperties',
    'ApplicationInsightsComponentAPIKey',
    'ApplicationInsightsComponentAvailableFeatures',
    'ApplicationInsightsComponentBillingFeatures',
    'ApplicationInsightsComponentDataVolumeCap',
    'ApplicationInsightsComponentExportConfiguration',
    'ApplicationInsightsComponentExportRequest',
    'ApplicationInsightsComponentFavorite',
    'ApplicationInsightsComponentFeature',
    'ApplicationInsightsComponentFeatureCapabilities',
    'ApplicationInsightsComponentFeatureCapability',
    'ApplicationInsightsComponentProactiveDetectionConfiguration',
    'ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions',
    'ApplicationInsightsComponentQuotaStatus',
    'ApplicationInsightsComponentWebTestLocation',
    'ComponentPurgeBody',
    'ComponentPurgeBodyFilters',
    'ComponentPurgeResponse',
    'ComponentPurgeStatusResponse',
    'ComponentsResource',
    'ErrorFieldContract',
    'ErrorResponse', 'ErrorResponseException',
    'InnerError',
    'LinkProperties',
    'Operation',
    'OperationDisplay',
    'TagsResource',
    'WebTest',
    'WebTestGeolocation',
    'WebTestPropertiesConfiguration',
    'WebtestsResource',
    'Workbook',
    'WorkbookError', 'WorkbookErrorException',
    'WorkbookResource',
    'WorkItemConfiguration',
    'WorkItemConfigurationError', 'WorkItemConfigurationErrorException',
    'WorkItemCreateConfiguration',
    'OperationPaged',
    'AnnotationPaged',
    'ApplicationInsightsComponentAPIKeyPaged',
    'WorkItemConfigurationPaged',
    'ApplicationInsightsComponentPaged',
    'ApplicationInsightsComponentWebTestLocationPaged',
    'WebTestPaged',
    'WorkbookPaged',
    'ItemScope',
    'ItemType',
    'ApplicationType',
    'FlowType',
    'RequestSource',
    'PurgeState',
    'FavoriteType',
    'WebTestKind',
    'SharedTypeKind',
    'ItemScopePath',
    'ItemTypeParameter',
    'FavoriteSourceType',
    'CategoryType',
]
