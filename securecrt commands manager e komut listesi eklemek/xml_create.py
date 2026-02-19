import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_securecrt_xml(excel_file_path, output_xml_path):
    # Excel dosyasını oku ve NaN değerleri boş string ile değiştir
    df = pd.read_excel(excel_file_path).fillna("")
    
    # Ana XML yapısını oluştur
    root = ET.Element("VanDyke", version="3.0")
    commands_root = ET.SubElement(root, "key", name="Commands")
    
    # Vendor gruplarına göre işle
    for vendor in df["Vendor"].unique():
        if not vendor:  # Vendor boşsa atla
            continue
            
        vendor_key = ET.SubElement(commands_root, "key", name=str(vendor))
        
        # Kategoriye göre komutları grupla
        vendor_data = df[df["Vendor"] == vendor]
        for category in vendor_data["Category"].unique():
            if pd.isna(category) or category == "":  # Kategori boşsa genel komutlara ekle
                continue
                
            category_data = vendor_data[vendor_data["Category"] == category]
            category_key = ET.SubElement(vendor_key, "key", name=str(category))
            commands_key = ET.SubElement(category_key, "key", name="__Commands__")
            default_array = ET.SubElement(commands_key, "array", name="Default")
            
            # Komutları ekle
            for _, row in category_data.iterrows():
                if not row["Command"] or pd.isna(row["Command"]):
                    continue
                command_str = f"SEND,{row['Command']},{row['Command']},,,0,1,{row['Command']},"
                ET.SubElement(default_array, "string").text = command_str
        
        # Vendor için genel komutlar (kategori yoksa)
        general_commands = vendor_data[vendor_data["Category"].isna() | (vendor_data["Category"] == "")]
        if not general_commands.empty:
            commands_key = ET.SubElement(vendor_key, "key", name="__Commands__")
            default_array = ET.SubElement(commands_key, "array", name="Default")
            for _, row in general_commands.iterrows():
                if not row["Command"] or pd.isna(row["Command"]):
                    continue
                command_str = f"SEND,{row['Command']},{row['Command']},,,0,1,{row['Command']},"
                ET.SubElement(default_array, "string").text = command_str
    
    # XML'i düzgün formatla ve kaydet
    xml_str = ET.tostring(root, encoding="utf-8")
    dom = minidom.parseString(xml_str)
    # toprettyxml encoding="utf-8" belirtilirse bytes döndürür, biz manuel yazıyoruz
    body = dom.toprettyxml(indent="\t")
    # toprettyxml'in ürettiği ilk satırı (<?xml ...?>) çıkar, yerine istediğimizin koy
    lines = body.splitlines()
    lines[0] = '<?xml version="1.0" encoding="UTF-8"?>'
    # Boş satırları temizle (toprettyxml bazen ekstra boş satır ekler)
    clean_lines = [l for l in lines if l.strip() != ""]
    pretty_xml = "\n".join(clean_lines) + "\n"
    
    with open(output_xml_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

if __name__ == "__main__":
    excel_file_path = "commands.xlsx"  # Excel dosyası yolu
    output_xml_path = "securecrt_commands.xml"  # Çıktı XML dosyası yolu
    create_securecrt_xml(excel_file_path, output_xml_path)
    print(f"XML dosyası oluşturuldu: {output_xml_path}")
