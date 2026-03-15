from abstract_class import DataMiner


# ---- template_method/concrete_classes.py
class CSVMiner(DataMiner):
    def extract_data(self, path: str) -> str:
        return "a,b,c\n1,2,3\n4,5,6"

    def parse_data(self, raw: str) -> list:
        lines = raw.split("\n")
        headers = lines[0].split(",")
        return [dict(zip(headers, l.split(","))) for l in lines[1:] if l]


class JSONMiner(DataMiner):
    def extract_data(self, path: str) -> str:
        return '[{"id":1,"val":"x"},{"id":2,"val":"y"}]'

    def parse_data(self, raw: str) -> list:
        import json

        return json.loads(raw)
