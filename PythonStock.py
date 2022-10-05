import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf   #Yahoo的API
plt.style.use('fivethirtyeight')

#股票代號
#美股: TSLA , AAPL , GOOG ...etc
#台股: 2330.TW , 3008.TW , 2317.TW ...etc
print("請輸入股票代號，台股請加 .TW")
stock_no=input('')

#起始日期
print("請輸入起始日期 YYYY-MM-DD")
start_date=input('')
print("請輸入截止日期 YYYY-MM-DD")
end_date=input('')

#下載資料
df=yf.download(stock_no,start=start_date)

df.tail()

figure = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,

            open=df['Open'],    # 開
            high=df['High'],    # 高
            low=df['Low'],      # 低
            close=df['Close'],  # 收
            # 綠漲紅跌
            increasing_line_color='green',
            decreasing_line_color='red'
        )
    ]
)

figure.update_layout(
    title=stock_no+" K線（綠漲紅跌）",
    xaxis_title='Date',
    yaxis_title='Price',
)

# 秀圖
figure.show()