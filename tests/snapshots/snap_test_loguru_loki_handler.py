# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestLokiHandler::test_write_method 1'] = [
    [
        '12345',
        '{"message": "Sample error message1", "timestamp": "2023-10-12T10:00:00Z", "process": 123, "thread": 456, "function": "sample_function", "module": "sample_module", "name": "sample_name"}'
    ]
]

snapshots['TestLokiHandler::test_write_method 2'] = '{"streams": [{"stream": {"application": "Test", "envornment": "Develop", "level": "INFO"}, "values": [["12345", "{\\"message\\": \\"Sample error message1\\", \\"timestamp\\": \\"2023-10-12T10:00:00Z\\", \\"process\\": 123, \\"thread\\": 456, \\"function\\": \\"sample_function\\", \\"module\\": \\"sample_module\\", \\"name\\": \\"sample_name\\"}"]]}]}'

snapshots['TestLokiHandler::test_write_method_extra 1'] = [
    [
        '12345',
        '{"message": "Sample error message1", "timestamp": "2023-10-12T10:00:00Z", "process": 123, "thread": 456, "function": "sample_function", "module": "sample_module", "name": "sample_name", "key1": "value1", "key2": "value2"}'
    ]
]

snapshots['TestLokiHandler::test_write_method_extra 2'] = '{"streams": [{"stream": {"application": "Test", "envornment": "Develop", "level": "INFO", "key1": "value1"}, "values": [["12345", "{\\"message\\": \\"Sample error message1\\", \\"timestamp\\": \\"2023-10-12T10:00:00Z\\", \\"process\\": 123, \\"thread\\": 456, \\"function\\": \\"sample_function\\", \\"module\\": \\"sample_module\\", \\"name\\": \\"sample_name\\", \\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\"}"]]}]}'

snapshots['TestLokiHandler::test_write_method_level_error 1'] = [
    [
        '12345',
        '{"message": "Sample error message1", "timestamp": "2023-10-12T10:00:00Z", "process": 123, "thread": 456, "function": "sample_function", "module": "sample_module", "name": "sample_name", "file": "sample_file", "path": "/path/to/file", "line": 42}'
    ]
]

snapshots['TestLokiHandler::test_write_method_level_error 2'] = '{"streams": [{"stream": {"application": "Test", "envornment": "Develop", "level": "ERROR"}, "values": [["12345", "{\\"message\\": \\"Sample error message1\\", \\"timestamp\\": \\"2023-10-12T10:00:00Z\\", \\"process\\": 123, \\"thread\\": 456, \\"function\\": \\"sample_function\\", \\"module\\": \\"sample_module\\", \\"name\\": \\"sample_name\\", \\"file\\": \\"sample_file\\", \\"path\\": \\"/path/to/file\\", \\"line\\": 42}"]]}]}'
