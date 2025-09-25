import json
import pandas as pd

# Baca file JSON
file_path = "/mnt/data/Maria Teofani Evernita Sagala_V3925048.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Konversi setiap bagian ke DataFrame
df_media = pd.DataFrame(data["media_sosial"])
df_cctv = pd.DataFrame(data["video_cctv_drone"])
df_sensor = pd.DataFrame(data["sensor_iot"])
df_lokasi = pd.DataFrame(data["data_lokasi_waktu"])

# Simpan ke CSV
csv_media = "/mnt/data/media_sosial.csv"
csv_cctv = "/mnt/data/video_cctv_drone.csv"
csv_sensor = "/mnt/data/sensor_iot.csv"
csv_lokasi = "/mnt/data/data_lokasi_waktu.csv"

df_media.to_csv(csv_media, index=False, encoding="utf-8")
df_cctv.to_csv(csv_cctv, index=False, encoding="utf-8")
df_sensor.to_csv(csv_sensor, index=False, encoding="utf-8")
df_lokasi.to_csv(csv_lokasi, index=False, encoding="utf-8")

# Simpan ke Excel (semua sheet dalam 1 file)
excel_output = "/mnt/data/data_output.xlsx"
with pd.ExcelWriter(excel_output) as writer:
    df_media.to_excel(writer, sheet_name="media_sosial", index=False)
    df_cctv.to_excel(writer, sheet_name="video_cctv_drone", index=False)
    df_sensor.to_excel(writer, sheet_name="sensor_iot", index=False)
    df_lokasi.to_excel(writer, sheet_name="data_lokasi_waktu", index=False)

csv_media, csv_cctv, csv_sensor, csv_lokasi, excel_output
