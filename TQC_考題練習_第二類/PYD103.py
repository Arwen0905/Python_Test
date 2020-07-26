# 載入 yaml 與 json 模組
import yaml
import json

# 讀取 json 檔案
with open("read_103.json", encoding='utf-8-sig') as file:
    data = json.load(file)
    print(data)
# 寫入 yaml 檔案
with open("write_103.yaml", "w+", encoding="utf-8") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
