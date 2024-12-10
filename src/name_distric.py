from typing import Optional
from fastapi import FastAPI, HTTPException

def get_name_from_district(district_id: Optional[int], file_path="list.txt"):
    if district_id is None:
        return None
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    file_district_id, name = line.strip().split(". ")
                except ValueError:
                    continue
                if int(file_district_id) == district_id:
                    return name.strip()
        raise ValueError(f"Không tìm thấy district_id {district_id} trong file.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# a = get_name_from_district(3)
# print(a)
