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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import RecoveryServicesBackupClientConfiguration
from .operations import BackupResourceVaultConfigsOperations
from .operations import ProtectedItemsOperations
from .operations import ProtectedItemOperationResultsOperations
from .operations import RecoveryPointsOperations
from .operations import RestoresOperations
from .operations import BackupPoliciesOperations
from .operations import ProtectionPoliciesOperations
from .operations import ProtectionPolicyOperationResultsOperations
from .operations import BackupJobsOperations
from .operations import JobDetailsOperations
from .operations import JobCancellationsOperations
from .operations import JobOperationResultsOperations
from .operations import ExportJobsOperationResultsOperations
from .operations import JobsOperations
from .operations import BackupProtectedItemsOperations
from .operations import OperationOperations
from .operations import AadPropertiesOperations
from .operations import CrossRegionRestoreOperations
from .operations import BackupCrrJobDetailsOperations
from .operations import BackupCrrJobsOperations
from .operations import CrrOperationResultsOperations
from .operations import CrrOperationStatusOperations
from .operations import RecoveryPointsCrrOperations
from .operations import BackupProtectedItemsCrrOperations
from .operations import ProtectionIntentOperations
from .operations import BackupStatusOperations
from .operations import FeatureSupportOperations
from .operations import BackupProtectionIntentOperations
from .operations import BackupUsageSummariesOperations
from .operations import BackupEnginesOperations
from .operations import ProtectionContainerRefreshOperationResultsOperations
from .operations import ProtectableContainersOperations
from .operations import ProtectionContainersOperations
from .operations import BackupWorkloadItemsOperations
from .operations import ProtectionContainerOperationResultsOperations
from .operations import BackupsOperations
from .operations import ProtectedItemOperationStatusesOperations
from .operations import ItemLevelRecoveryConnectionsOperations
from .operations import BackupOperationResultsOperations
from .operations import BackupOperationStatusesOperations
from .operations import ProtectionPolicyOperationStatusesOperations
from .operations import BackupProtectableItemsOperations
from .operations import BackupProtectionContainersOperations
from .operations import SecurityPINsOperations
from .operations import BackupResourceStorageConfigsOperations
from .operations import Operations
from . import models


class RecoveryServicesBackupClient(SDKClient):
    """Open API 2.0 Specs for Azure RecoveryServices Backup service

    :ivar config: Configuration for client.
    :vartype config: RecoveryServicesBackupClientConfiguration

    :ivar backup_resource_vault_configs: BackupResourceVaultConfigs operations
    :vartype backup_resource_vault_configs: azure.mgmt.recoveryservicesbackup.operations.BackupResourceVaultConfigsOperations
    :ivar protected_items: ProtectedItems operations
    :vartype protected_items: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemsOperations
    :ivar protected_item_operation_results: ProtectedItemOperationResults operations
    :vartype protected_item_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemOperationResultsOperations
    :ivar recovery_points: RecoveryPoints operations
    :vartype recovery_points: azure.mgmt.recoveryservicesbackup.operations.RecoveryPointsOperations
    :ivar restores: Restores operations
    :vartype restores: azure.mgmt.recoveryservicesbackup.operations.RestoresOperations
    :ivar backup_policies: BackupPolicies operations
    :vartype backup_policies: azure.mgmt.recoveryservicesbackup.operations.BackupPoliciesOperations
    :ivar protection_policies: ProtectionPolicies operations
    :vartype protection_policies: azure.mgmt.recoveryservicesbackup.operations.ProtectionPoliciesOperations
    :ivar protection_policy_operation_results: ProtectionPolicyOperationResults operations
    :vartype protection_policy_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionPolicyOperationResultsOperations
    :ivar backup_jobs: BackupJobs operations
    :vartype backup_jobs: azure.mgmt.recoveryservicesbackup.operations.BackupJobsOperations
    :ivar job_details: JobDetails operations
    :vartype job_details: azure.mgmt.recoveryservicesbackup.operations.JobDetailsOperations
    :ivar job_cancellations: JobCancellations operations
    :vartype job_cancellations: azure.mgmt.recoveryservicesbackup.operations.JobCancellationsOperations
    :ivar job_operation_results: JobOperationResults operations
    :vartype job_operation_results: azure.mgmt.recoveryservicesbackup.operations.JobOperationResultsOperations
    :ivar export_jobs_operation_results: ExportJobsOperationResults operations
    :vartype export_jobs_operation_results: azure.mgmt.recoveryservicesbackup.operations.ExportJobsOperationResultsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.recoveryservicesbackup.operations.JobsOperations
    :ivar backup_protected_items: BackupProtectedItems operations
    :vartype backup_protected_items: azure.mgmt.recoveryservicesbackup.operations.BackupProtectedItemsOperations
    :ivar operation: Operation operations
    :vartype operation: azure.mgmt.recoveryservicesbackup.operations.OperationOperations
    :ivar aad_properties: AadProperties operations
    :vartype aad_properties: azure.mgmt.recoveryservicesbackup.operations.AadPropertiesOperations
    :ivar cross_region_restore: CrossRegionRestore operations
    :vartype cross_region_restore: azure.mgmt.recoveryservicesbackup.operations.CrossRegionRestoreOperations
    :ivar backup_crr_job_details: BackupCrrJobDetails operations
    :vartype backup_crr_job_details: azure.mgmt.recoveryservicesbackup.operations.BackupCrrJobDetailsOperations
    :ivar backup_crr_jobs: BackupCrrJobs operations
    :vartype backup_crr_jobs: azure.mgmt.recoveryservicesbackup.operations.BackupCrrJobsOperations
    :ivar crr_operation_results: CrrOperationResults operations
    :vartype crr_operation_results: azure.mgmt.recoveryservicesbackup.operations.CrrOperationResultsOperations
    :ivar crr_operation_status: CrrOperationStatus operations
    :vartype crr_operation_status: azure.mgmt.recoveryservicesbackup.operations.CrrOperationStatusOperations
    :ivar recovery_points_crr: RecoveryPointsCrr operations
    :vartype recovery_points_crr: azure.mgmt.recoveryservicesbackup.operations.RecoveryPointsCrrOperations
    :ivar backup_protected_items_crr: BackupProtectedItemsCrr operations
    :vartype backup_protected_items_crr: azure.mgmt.recoveryservicesbackup.operations.BackupProtectedItemsCrrOperations
    :ivar protection_intent: ProtectionIntent operations
    :vartype protection_intent: azure.mgmt.recoveryservicesbackup.operations.ProtectionIntentOperations
    :ivar backup_status: BackupStatus operations
    :vartype backup_status: azure.mgmt.recoveryservicesbackup.operations.BackupStatusOperations
    :ivar feature_support: FeatureSupport operations
    :vartype feature_support: azure.mgmt.recoveryservicesbackup.operations.FeatureSupportOperations
    :ivar backup_protection_intent: BackupProtectionIntent operations
    :vartype backup_protection_intent: azure.mgmt.recoveryservicesbackup.operations.BackupProtectionIntentOperations
    :ivar backup_usage_summaries: BackupUsageSummaries operations
    :vartype backup_usage_summaries: azure.mgmt.recoveryservicesbackup.operations.BackupUsageSummariesOperations
    :ivar backup_engines: BackupEngines operations
    :vartype backup_engines: azure.mgmt.recoveryservicesbackup.operations.BackupEnginesOperations
    :ivar protection_container_refresh_operation_results: ProtectionContainerRefreshOperationResults operations
    :vartype protection_container_refresh_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainerRefreshOperationResultsOperations
    :ivar protectable_containers: ProtectableContainers operations
    :vartype protectable_containers: azure.mgmt.recoveryservicesbackup.operations.ProtectableContainersOperations
    :ivar protection_containers: ProtectionContainers operations
    :vartype protection_containers: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainersOperations
    :ivar backup_workload_items: BackupWorkloadItems operations
    :vartype backup_workload_items: azure.mgmt.recoveryservicesbackup.operations.BackupWorkloadItemsOperations
    :ivar protection_container_operation_results: ProtectionContainerOperationResults operations
    :vartype protection_container_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainerOperationResultsOperations
    :ivar backups: Backups operations
    :vartype backups: azure.mgmt.recoveryservicesbackup.operations.BackupsOperations
    :ivar protected_item_operation_statuses: ProtectedItemOperationStatuses operations
    :vartype protected_item_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemOperationStatusesOperations
    :ivar item_level_recovery_connections: ItemLevelRecoveryConnections operations
    :vartype item_level_recovery_connections: azure.mgmt.recoveryservicesbackup.operations.ItemLevelRecoveryConnectionsOperations
    :ivar backup_operation_results: BackupOperationResults operations
    :vartype backup_operation_results: azure.mgmt.recoveryservicesbackup.operations.BackupOperationResultsOperations
    :ivar backup_operation_statuses: BackupOperationStatuses operations
    :vartype backup_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.BackupOperationStatusesOperations
    :ivar protection_policy_operation_statuses: ProtectionPolicyOperationStatuses operations
    :vartype protection_policy_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.ProtectionPolicyOperationStatusesOperations
    :ivar backup_protectable_items: BackupProtectableItems operations
    :vartype backup_protectable_items: azure.mgmt.recoveryservicesbackup.operations.BackupProtectableItemsOperations
    :ivar backup_protection_containers: BackupProtectionContainers operations
    :vartype backup_protection_containers: azure.mgmt.recoveryservicesbackup.operations.BackupProtectionContainersOperations
    :ivar security_pi_ns: SecurityPINs operations
    :vartype security_pi_ns: azure.mgmt.recoveryservicesbackup.operations.SecurityPINsOperations
    :ivar backup_resource_storage_configs: BackupResourceStorageConfigs operations
    :vartype backup_resource_storage_configs: azure.mgmt.recoveryservicesbackup.operations.BackupResourceStorageConfigsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservicesbackup.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = RecoveryServicesBackupClientConfiguration(credentials, subscription_id, base_url)
        super(RecoveryServicesBackupClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.backup_resource_vault_configs = BackupResourceVaultConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_items = ProtectedItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_item_operation_results = ProtectedItemOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recovery_points = RecoveryPointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restores = RestoresOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_policies = BackupPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policies = ProtectionPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policy_operation_results = ProtectionPolicyOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_jobs = BackupJobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_details = JobDetailsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_cancellations = JobCancellationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_operation_results = JobOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.export_jobs_operation_results = ExportJobsOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protected_items = BackupProtectedItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.aad_properties = AadPropertiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cross_region_restore = CrossRegionRestoreOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_crr_job_details = BackupCrrJobDetailsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_crr_jobs = BackupCrrJobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.crr_operation_results = CrrOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.crr_operation_status = CrrOperationStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recovery_points_crr = RecoveryPointsCrrOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protected_items_crr = BackupProtectedItemsCrrOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_intent = ProtectionIntentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_status = BackupStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.feature_support = FeatureSupportOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protection_intent = BackupProtectionIntentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_usage_summaries = BackupUsageSummariesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_engines = BackupEnginesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_container_refresh_operation_results = ProtectionContainerRefreshOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protectable_containers = ProtectableContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_containers = ProtectionContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_workload_items = BackupWorkloadItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_container_operation_results = ProtectionContainerOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backups = BackupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_item_operation_statuses = ProtectedItemOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.item_level_recovery_connections = ItemLevelRecoveryConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_operation_results = BackupOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_operation_statuses = BackupOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policy_operation_statuses = ProtectionPolicyOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protectable_items = BackupProtectableItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protection_containers = BackupProtectionContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.security_pi_ns = SecurityPINsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_resource_storage_configs = BackupResourceStorageConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
