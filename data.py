import zipfile
import re
import csv
from datetime import datetime

pattern0 = r"^2022"
pattern1 = r"([0-9]|1[0-9]|2[0-3]):00" 

# 匹配结果
matches = []

for month in range(4, 13):
    zip_file_path = f"data/2022-2023/2022{month:02d}_power_usage.zip"

    # 解压后
    extracted_dir = f"extracted_files/{month}/"

    # 解压
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extracted_dir)

    for day in range(1, 32):
        try:
            # 读取匹配
            csv_file_path = extracted_dir + f"2022{month:02d}{day:02d}_power_usage.csv"

            with open(csv_file_path, newline="", encoding="Shift JIS") as csvfile:
                csv_reader = csv.reader(csvfile)
                # print(csv_reader)
                for row in csv_reader:
                    try:
                        # print(type(row))
                        match = re.match(pattern0, row[0]) and re.match(pattern1, row[1])
                        if match and len(row) >= 6:
                            # print(row)
                            matches.append(row[0:3])
                    except IndexError:
                        pass
                        # print("This is an IndexError")
        except FileNotFoundError as e:
            print("这个月没有31天", e)

print(len(matches))

csv_file_path = "data/juyo-2022.csv"

with open(csv_file_path, "w", newline="", encoding="Shift JIS") as csvfile:
    csv_writer = csv.writer(csvfile)
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M")
    csv_writer.writerow([current_time + " UPDATE"])
    csv_writer.writerow([])
    csv_writer.writerow(["DATE", "TIME", "実績(万kW)"])  
    csv_writer.writerows(matches)  

print("Done!!!")