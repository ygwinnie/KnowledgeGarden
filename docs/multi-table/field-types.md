# 多维表格字段类型与JSON表达方式

根据提供的图片示例，多维表格中不同类型的字段在JSON中有不同的表达方式。以下是各种字段类型及其对应的JSON格式总结：

## 1. 超链接 (Hyperlink)

超链接类型包含文本和链接两个部分：

```json
{
  "超链接": {
    "text": "这是一个超链接",
    "link": "https://www.baidu.com"
  }
}
```

## 2. 文本 (Text)

文本类型直接使用字符串值：

```json
{
  "文本": "这是一个文本"
}
```

## 3. 数字 (Number)

数字类型直接使用数值，不需要引号：

```json
{
  "数字": 100
}
```

注意：数字格式可以设置为整数、小数等不同格式。

## 4. 单选 (Single Choice)

单选类型直接使用字符串值：

```json
{
  "单选": "这是一个单选"
}
```

## 5. 多选 (Multiple Choice)

多选类型使用字符串数组：

```json
{
  "多选": ["标签1", "标签2"]
}
```

## 6. 日期 (Date)

日期类型使用时间戳（整数）：

```json
{
  "日期": 1740757596099
}
```

日期在界面上可以显示为各种格式（如"2025-01-30 14:00"），但在JSON中统一使用时间戳表示。

## 数据处理最佳实践

当处理这些不同类型的字段时，应当注意：

1. **类型一致性**：确保每种字段按照其对应的类型进行处理：
   - 文本、单选：字符串
   - 超链接：包含text和link的对象
   - 数字、日期：数值（不带引号）
   - 多选：字符串数组

2. **类型转换**：
   ```python
   # 数字类型转换示例
   try:
       number_field = int(item.get("number_field", 0)) if item.get("number_field") else 0
   except (ValueError, TypeError):
       number_field = 0
       
   # 日期类型处理示例 (假设输入是日期字符串)
   from datetime import datetime
   try:
       date_str = item.get("date_field")
       if date_str:
           date_timestamp = int(datetime.strptime(date_str, "%Y-%m-%d").timestamp() * 1000)
       else:
           date_timestamp = 0
   except:
       date_timestamp = 0
   ```

3. **构建记录结构**：
   ```python
   record = {
       "fields": {
           "超链接字段": {"text": "显示文本", "link": "https://example.com"},
           "文本字段": "文本内容",
           "数字字段": 123,
           "单选字段": "选项值",
           "多选字段": ["选项1", "选项2"],
           "日期字段": 1740757596099
       }
   }
   ```

## 完整代码示例

```python
async def main(args):
    params = args.params
    input_list = params.get("data_list", [])
    
    records = []
    for item in input_list:
        # 处理不同类型的字段
        try:
            number_value = int(item.get("number", 0)) if item.get("number") else 0
        except (ValueError, TypeError):
            number_value = 0
            
        # 多选处理 - 确保是数组
        tags = item.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]  # 如果是单个字符串，转换为数组
            
        record = {
            "fields": {
                "标题": {"text": item.get("title", ""), "link": item.get("url", "")},
                "内容": item.get("content", ""),
                "分数": number_value,
                "类型": item.get("type", ""),
                "标签": tags,
                "创建日期": item.get("timestamp", 0)
            }
        }
        records.append(record)
    
    return records
```

通过正确处理各种字段类型，可以确保数据在多维表格中正确显示和操作。