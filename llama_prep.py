from pathlib import Path
import csv
import json

_p = "./Data_数据/"
llama_res_file = "./med.dialog.data.json"
SKIP_DIRS = ["temp", "logs"]

plist = Path(_p)

llama_res = []


def append_to_list(data: Path, res: list):
    with open(data, encoding="gb18030") as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            res.append({
                "instruction": row["title"],
                "input": row["ask"],
                "output": row["answer"],
            })


def get_all_items(root: Path, exclude=SKIP_DIRS):
    for item in root.iterdir():
        if item.name in exclude:
            continue
        yield item
        if item.is_dir():
            yield from get_all_items(item)


for item in get_all_items(plist):
    # print(f"{item} - {'dir' if item.is_dir() else 'file'}")
    # print(item, str(item)[-3:])
    if not item.is_dir() and str(item)[-3:] == "csv":
        append_to_list(item, llama_res)
        pass

# append_to_list(Path("样例_内科5000-6000.csv"), llama_res)

with open(llama_res_file, 'w') as outfile:
    json.dump(llama_res, outfile, ensure_ascii=False, indent=4)

print("done")
