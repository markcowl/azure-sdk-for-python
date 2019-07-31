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

from .copy_sink_py3 import CopySink


class SalesforceServiceCloudSink(CopySink):
    """A copy activity Salesforce Service Cloud sink.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the sink data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param table_option: The option to handle sink table, such as autoCreate.
     For now only 'autoCreate' value is supported. Type: string (or Expression
     with resultType string).
    :type table_option: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param write_behavior: The write behavior for the operation. Default is
     Insert. Possible values include: 'Insert', 'Upsert'
    :type write_behavior: str or
     ~azure.mgmt.datafactory.models.SalesforceSinkWriteBehavior
    :param external_id_field_name: The name of the external ID field for
     upsert operation. Default value is 'Id' column. Type: string (or
     Expression with resultType string).
    :type external_id_field_name: object
    :param ignore_null_values: The flag indicating whether or not to ignore
     null values from input dataset (except key fields) during write operation.
     Default value is false. If set it to true, it means ADF will leave the
     data in the destination object unchanged when doing upsert/update
     operation and insert defined default value when doing insert operation,
     versus ADF will update the data in the destination object to NULL when
     doing upsert/update operation and insert NULL value when doing insert
     operation. Type: boolean (or Expression with resultType boolean).
    :type ignore_null_values: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'table_option': {'key': 'tableOption', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'write_behavior': {'key': 'writeBehavior', 'type': 'str'},
        'external_id_field_name': {'key': 'externalIdFieldName', 'type': 'object'},
        'ignore_null_values': {'key': 'ignoreNullValues', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, write_batch_size=None, write_batch_timeout=None, sink_retry_count=None, sink_retry_wait=None, max_concurrent_connections=None, table_option=None, write_behavior=None, external_id_field_name=None, ignore_null_values=None, **kwargs) -> None:
        super(SalesforceServiceCloudSink, self).__init__(additional_properties=additional_properties, write_batch_size=write_batch_size, write_batch_timeout=write_batch_timeout, sink_retry_count=sink_retry_count, sink_retry_wait=sink_retry_wait, max_concurrent_connections=max_concurrent_connections, table_option=table_option, **kwargs)
        self.write_behavior = write_behavior
        self.external_id_field_name = external_id_field_name
        self.ignore_null_values = ignore_null_values
        self.type = 'SalesforceServiceCloudSink'
