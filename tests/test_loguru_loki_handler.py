import unittest
from unittest.mock import patch, Mock, MagicMock
from loguru_loki_handler import loki_handler
from tests.helper import LevelObject, TimeObject,  RecordValueMock, FileObject
from snapshottest import TestCase
import json

class TestLokiHandler(TestCase):

    @patch('requests.post', new_callable=Mock)
    @patch('time.time_ns', MagicMock(return_value=12345))
    def test_write_method(self, mock_post):
  
        mock_message = Mock()
       
        mock_message.record = {
            "level": LevelObject(name="INFO"),
            "message": "Sample error message1",
            "time": TimeObject("2023-10-12T10:00:00Z"),
            "process": RecordValueMock(123, "123"),
            "thread":RecordValueMock(456, "456"),
            "function": "sample_function",
            "module": "sample_module",
            "name": "sample_name",
            "extra": {}
        }
        
        loki = loki_handler(url='your_url', labels={"application":"Test", "envornment":"Develop"}, labelKeys={})

        loki.write(mock_message)
        
        self.assertMatchSnapshot(loki.steam.values)
        self.assertMatchSnapshot(loki.request.serialize())

        mock_post.assert_called_once_with(
            loki.url,
            data=loki.request.serialize(),
            headers={"Content-type": "application/json"}
        )

    @patch('requests.post', new_callable=Mock)
    @patch('time.time_ns', MagicMock(return_value=12345))
    def test_write_method_level_error(self, mock_post):
  
        mock_message = Mock()
       
        mock_message.record = {
            "level": LevelObject(name="ERROR"), 
            "message": "Sample error message1",
            "time": TimeObject("2023-10-12T10:00:00Z"),
            "process": RecordValueMock(123, "123"),
            "thread":RecordValueMock(456, "456"),
            "function": "sample_function",
            "module": "sample_module",
            "name": "sample_name",
            "extra": {},
            "file": FileObject(name="sample_file",path="/path/to/file"),
            "line": 42
        }
        
        loki = loki_handler(url='your_url', labels={"application":"Test", "envornment":"Develop"}, labelKeys={})

        loki.write(mock_message)
        
        self.assertMatchSnapshot(loki.steam.values)
        self.assertMatchSnapshot(loki.request.serialize())

        mock_post.assert_called_once_with(
            loki.url,
            data=loki.request.serialize(),
            headers={"Content-type": "application/json"}
        )


    @patch('requests.post', new_callable=Mock)
    @patch('time.time_ns', MagicMock(return_value=12345))
    def test_write_method_extra(self, mock_post):
  
        mock_message = Mock()
       
        mock_message.record = {
            "level": LevelObject(name="INFO"),
            "message": "Sample error message1",
            "time": TimeObject("2023-10-12T10:00:00Z"),
            "process": RecordValueMock(123, "123"),
            "thread":RecordValueMock(456, "456"),
            "function": "sample_function",
            "module": "sample_module",
            "name": "sample_name",
            "extra": {"key1": "value1", "key2": "value2"},
            "file": FileObject(name="sample_file",path="/path/to/file"),
            "line": 42
        }
        
        loki = loki_handler(url='your_url', labels={"application":"Test", "envornment":"Develop"}, labelKeys={"key1":"Test"})

        loki.write(mock_message)

        self.assertMatchSnapshot(loki.steam.values)
        self.assertMatchSnapshot(loki.request.serialize())

        mock_post.assert_called_once_with(
            loki.url,
            data=loki.request.serialize(),
            headers={"Content-type": "application/json"}
        )        

if __name__ == '__main__':
    unittest.main()
