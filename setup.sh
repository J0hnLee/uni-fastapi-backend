#!/bin/bash

# 檢查是否提供了參數
if [ $# -lt 2 ]; then
  echo "用法: $0 參數1 參數2"
  exit 1
fi



# 檢查是否已經有 SQL Server 2022 的 Docker 鏡像
if ! docker images mcr.microsoft.com/mssql/server:2022-latest --quiet | grep -q .; then
    echo "正在下載 SQL Server 2022 Docker 鏡像..."
    docker pull mcr.microsoft.com/mssql/server:2022-latest
    
    if [ $? -eq 0 ]; then
        echo "SQL Server 2022 Docker 鏡像下載成功"
    else
        echo "錯誤：SQL Server 2022 Docker 鏡像下載失敗"
        exit 1
    fi
else
    echo "SQL Server 2022 Docker 鏡像已存在，無需下載"
fi

# TODO: check container 是否存在，如果存在就啟動，如果不存在就重起一個
echo "正在啟動 SQL Server 2022 Docker 容器..."
if [ ! "$(docker ps -q -f name=sqlserver-clone)" ]; then
    if docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=12345678abd*" -e "MSSQL_PID=Developer" -p 1433:1433 --name sqlserver-clone --restart always -d mcr.microsoft.com/mssql/server:2022-latest; then
        echo "SQL Server 2022 Docker 容器啟動成功"
    else
        echo "錯誤：SQL Server 2022 Docker 容器啟動失敗"
        docker logs sqlserver-clone
        exit 1
    fi
else
    echo "SQL Server 2022 Docker 容器已經在運行中，無需重新啟動"
    docker restart sqlserver-clone

fi

echo "正在檢查備份目錄是否存在..."
if ! docker exec sqlserver-clone test -d /var/opt/mssql/backup; then
    echo "備份目錄不存在，正在創建..."
    docker exec -it sqlserver-clone mkdir -p /var/opt/mssql/backup
fi

# TODO: check SJDB.bak 是否已經在目標資料夾
echo "正在建立 SQL Server 2022 容器的備份..."
echo "正在將備份檔案SJDB從本機複製到 SQL Server 2022 容器..."
docker cp /Volumes/home/Drive/SJDB.bak sqlserver-clone:/var/opt/mssql/backup/SJDB.bak
docker exec -it -u root sqlserver-clone chmod 777 /var/opt/mssql/backup/SJDB.bak

echo "正在執行資料庫還原..."
docker exec -it sqlserver-clone /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P 12345678abd* -C -Q "
RESTORE DATABASE SJDB 
FROM DISK = '/var/opt/mssql/backup/SJDB.bak' 
WITH MOVE 'SJDB_Data' TO '/var/opt/mssql/data/SJDB.mdf',
MOVE 'SJDB_Log' TO '/var/opt/mssql/data/SJDB_log.ldf',
REPLACE;
GO"