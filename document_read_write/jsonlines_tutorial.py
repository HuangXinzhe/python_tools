import jsonlines

# 写jsonl文件
url = ""
all_paragraph_data = [{}]
with jsonlines.open(url, mode="a") as writer:
    writer.write_all(all_paragraph_data)


# 读jsonl文件
import jsonlines
with open("xxxx.jl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        print(item)