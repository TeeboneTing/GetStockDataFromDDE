# 用凱基全球理財通擷取即時期貨資訊
### 更新日誌：
2016 Feb 15 第一版

2016 Feb 18 更新：連結DDE sever有誤時會隔五分鐘再連線一次

### 系統需求(測試環境)：
- Windows 7 (64 bit)
- 凱基[全球理財通]
- Python 2.7 (Anaconda 2 64bit)
- 網友 kynix 提供的 [python DDE library]

### 使用方法：
1. 開啟 凱基全球理財通
2. 開啟windows command line(命令提示字元)，移到程式碼所在位置，輸入 `python get_stock_dde.py`
3. 當有資料更新時則會及時顯示在螢幕上，並存入`data\stock_xx.csv`當中

### 資料欄位：
- 使用分號(;)做分隔
- 目前收集的資料為**2月份小台近月期貨交易資訊**
- 股票/期貨代號,名稱,時間,買進,賣出,成交,單量,總量,高點,低點,開盤
- 最後附上local time in millisecond，因為期貨交易為tick等級，一秒會有多次交易，附上millisecond以標示更精確的時間

### 已知問題/未來更新：
1. 倒數最後第二個欄位(開盤價)有時候會有換行符號(亂碼？)亂跳，有時候又正常。
2. 把分號分隔(;)改成逗號分隔(,)以符合csv檔精神
3. 更加參數化放在程式碼開頭，以適合不同看盤軟體DDE API
4. 自動換月收集小台期貨資訊
5. 自動排程化，每日開盤前自動開啟程式

### 參考資料：
- 如果需要瞭解DDE欄位怎麼自己改，可以看[幣圖誌]這一篇

[python DDE library]: <http://pykynix.blogspot.tw/2013/03/ddepython3dde.html>
[全球理財王]: <http://www.kgieworld.com.tw/service/service_4_4.aspx>
[幣圖誌]: <http://www.bituzi.com/2013/08/DDE.html>