"""
学生记录批量处理示例

这个脚本展示了如何处理学生记录并将其格式化为多维表格API所需的格式。
包含了数据类型转换、错误处理等最佳实践。
"""

import asyncio
from datetime import datetime
from typing import List, Dict, Any, Optional


async def main(args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    处理学生记录并格式化为多维表格API所需格式
    
    Args:
        args: 包含params字段的参数对象
        
    Returns:
        格式化后的学生记录列表
    """
    params = args.get("params", {})
    input_list = params.get("stu_info", [])  # 获取stu_info数据列表
    
    records = []
    # 遍历input_list生成records
    for item in input_list:
        # 安全地将小学号转换为整数
        try:
            minor_id = int(item.get("minor_id", 0)) if item.get("minor_id") else 0
        except (ValueError, TypeError):
            minor_id = 0
            
        record = {
            "fields": {
                "姓名": item.get("name", ""),
                "学号": item.get("student_id", ""),
                "小学号": minor_id,
                "班级": item.get("class", "")
            }
        }
        records.append(record)
    
    return records


# 测试数据示例
test_data = {
    "params": {
        "stu_info": [
            {
                "name": "小明",
                "student_id": "001",
                "minor_id": "1",
                "class": "7年级4班"
            },
            {
                "name": "小红",
                "student_id": "002",
                "minor_id": "2",
                "class": "7年级4班"
            },
            {
                "name": "小王",
                "student_id": "003",
                "minor_id": "3",
                "class": "7年级4班"
            }
        ]
    }
}


# 本地测试用代码
if __name__ == "__main__":
    # 创建事件循环
    loop = asyncio.get_event_loop()
    # 执行异步函数
    result = loop.run_until_complete(main(test_data))
    # 打印结果
    import json
    print(json.dumps(result, ensure_ascii=False, indent=2))
