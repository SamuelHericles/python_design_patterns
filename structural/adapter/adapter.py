from adaptee import XMLDataProcessor
from target import JSONDataProcessor


class XMLToJSONAdapter(JSONDataProcessor):
    def __init__(self, xml_processor: XMLDataProcessor):
        self._xml_processor = xml_processor

    def process(self, data: dict) -> str:
        xml_string = self._dict_to_xml(data)
        return self._xml_processor.process_xml(xml_string)

    def _dict_to_xml(self, data: dict) -> str:
        items = "".join(f"<{k}>{v}</{k}>" for k, v in data.items())
        return f"<root>{items}</root>"
