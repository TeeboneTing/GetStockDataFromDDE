import PyWinDDE
import datetime


f = open("data/stock_02.csv","a")

def recTickData(value,item):
	out_string =  "%s;%s"%(value,datetime.datetime.now())
	print out_string
	f.write(out_string + "\n")


dde = PyWinDDE.DDEClient("XQKGIAP","Quote")

dde.advise("FIMTX02.TF-ID,Name,Time,Bid,Ask,Price,Volume,TotalVolume,High,Low,Open",callback = recTickData)
PyWinDDE.WinMSGLoop()

#Test cases
#dde.advise("0050.TW-ID,Name,Time,Bid,Ask,Price,PriceChange,PriceChangeRatio,Amplitude,AvgPrice")
#dde.advise("TSE.TW-PreClose",callback = recTickData)
#dde.advise("FITX03.TF-PreClose",callback = recTickData)
#dde = PyWinDDE.DDEClient("HTS","KS")
#dde = PyWinDDE.DDEClient("CATDDE","FUTOPT<FO>TXFB6    ")
#dde.advise("CurPrice,TickVol,Diff,DiffRate,Open,High,Low")
#dde.advise("CurPrice")