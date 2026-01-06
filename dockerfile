# 使用官方 Python 基底映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製應用程式和需求檔案
COPY app.py /app/
COPY requirements.txt /app/

# 安裝所需套件
RUN pip install --no-cache-dir -r requirements.txt

# 暴露容器內的 5000 埠
EXPOSE 5000

# 指定啟動指令
CMD ["python", "app.py"]

