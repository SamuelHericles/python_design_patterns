from target import JSONDataProcessor
from adaptee import XMLDataProcessor
from adapter import XMLToJSONAdapter


# ---- adapter/main.py
def adapter_demo():
    print("=== ADAPTER ===")
    data = {"name": "Alice", "age": 30}
    json_proc = JSONDataProcessor()
    xml_proc = XMLDataProcessor()
    adapter = XMLToJSONAdapter(xml_proc)

    print(f"  {json_proc.process(data)}")
    print(f"  {adapter.process(data)}")
    print()


if __name__ == "__main__":
    adapter_demo()
