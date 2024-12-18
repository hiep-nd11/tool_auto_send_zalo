from typing import Optional
from fastapi import FastAPI, HTTPException

# def get_name_from_district(district_id: Optional[str], file_path="list.txt"):
#     # Chuyển district_id thành chuỗi nếu nó là kiểu int
#     if district_id is None:
#         return None
    
#     district_id = str(district_id)  # Đảm bảo district_id là chuỗi
    
#     try:
#         with open(file_path, "r") as file:
#             for line in file:
#                 try:
#                     file_district_id, name = line.strip().split(". ")
#                 except ValueError:
#                     continue
#                 if file_district_id == district_id:  # So sánh district_id là chuỗi
#                     return name.strip()
#         raise ValueError(f"Không tìm thấy district_id {district_id} trong file.")
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

district_data = """
1. hoàn kiếm
2. ba vì
3. hoài đức
4. hoàng mai
5. thạch thất
6. chương mỹ
7. sóc sơn
8. gia lâm
9. hai bà trưng
10. tây hồ
11. mê linh
12. thanh trì
13. ứng hòa
14. cầu giấy
15. phúc thọ
16. thanh oai
17. mỹ đức
18. sơn tây
19. đan phượng
20. long biên
21. quốc oai
22. ba đình
23. thanh xuân
24. đống đa
25. nam từ liêm
26. bắc từ liêm
27. phú xuyên
28. đông anh
30. hà đông
31. thường tín
"""


def get_name_from_district(district_id: Optional[str]):
    if district_id is None:
        return None
    
    district_id = str(district_id)  # Đảm bảo district_id là chuỗi
    
    try:
        # Duyệt qua các dòng trong chuỗi district_data
        for line in district_data.strip().splitlines():
            try:
                file_district_id, name = line.strip().split(". ")
            except ValueError:
                continue
            if file_district_id == district_id:  # So sánh district_id là chuỗi
                return name.strip()
        raise ValueError(f"Không tìm thấy district_id {district_id} trong dữ liệu.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Thử gọi hàm với district_id là 3
a = get_name_from_district(3)
print(a)

