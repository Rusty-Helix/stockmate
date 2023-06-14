# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        if 'stock-information' in load_template:
            if 'overview' in load_template:
                pass
            elif 'rankings' in load_template:
                pass
            elif 'heatmap' in load_template:
                pass
            elif 'news' in load_template:
                pass
        elif 'strategy-gallery' in load_template:
            if 'pool' in load_template:
                context['strategies'] = strategies
                # print(strategies[0]['策略名稱'])

            elif 'decks' in load_template:
                pass
        elif 'investment-notes' in load_template:
            if 'all' in load_template:
                pass
            elif 'highlights' in load_template:
                pass
        elif 'review' in load_template:
            if 'execution' in load_template:
                pass
            elif 'roi' in load_template:
                pass
            elif 'timeline' in load_template:
                pass
            elif 'line-chart' in load_template:
                pass
            elif 'report' in load_template:
                pass

        

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

# ======================== #


    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def profile(request):
#     load_template = request.path.split('/')[-1]
    
#     context = {}
#     context['segment'] = load_template
    
#     html_template = loader.get_template('home/' + load_template)
#     return HttpResponse(html_template.render(context, request))


strategies = [
  {
    "id": 1,
    "title": "兩隻烏鴉",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "第一天長紅，第二天高開收綠，第三天再次高開繼續收綠，收盤比前一日收盤價低。",
    "cover": "Two_Crows.png",
    "footnote": "三日K線"
  },
  {
    "id": 2,
    "title": "三隻烏鴉",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "連續三根長綠，每日收盤價都下跌且接近最低價，每日開盤價都在上根K線實體內",
    "cover": "Three_Crows.png",
    "footnote": "三日K線"
  },
  {
    "id": 3,
    "title": "三內部上漲",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "K線為綠紅紅，第三天收盤價高於第一天開盤價，第二天K線在第一天K線內部。",
    "cover": "Three_Inside_Up_Bullish.png.png",
    "footnote": "三日K線"
  },
  {
    "id": 4,
    "title": "三內部下跌",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "K線為紅綠綠，第三天收盤價低於第一天開盤價，第二天K線在第一天K線內部。",
    "cover": "Three_Inside_Down_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 5,
    "title": "三線震盪(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "前三根紅K，每日收盤價都比前一日高，開盤價在前一日實體內，第四日市場高開，收盤價低於第一日開盤價，預示股價下跌。",
    "cover": "Three_Line_Strike_Bearish.png",
    "footnote": "四日K線"
  },
  {
    "id": 6,
    "title": "三線震盪(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "前三根綠K，每日收盤價都比前一日低，開盤價在前一日實體內，第四日市場高低，收盤價高於第一日開盤價，預示股價上漲。",
    "cover": "Three_Line_Strike_Bullish.png",
    "footnote": "四日K線"
  },
  {
    "id": 7,
    "title": "三外部上漲",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "K線為綠紅紅，但第一日與第二日的K線形態相反，第一日K線在第二日K線內部，預示著股價上漲",
    "cover": "Three_Outside_Up_Bullish.png.png",
    "footnote": "三日K線"
  },
  {
    "id": 8,
    "title": "三內部下跌",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "K線為紅綠綠，但第一日與第二日的K線形態相反，第一日K線在第二日K線內部，預示著股價下跌",
    "cover": "Three_Outside_Down_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 9,
    "title": "南方三星",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "三日K線皆綠，第一日有長下影線，第二日與第一日類似，K線整體小於第一日，第三日無下影線實體信號，成交價格都在第一日振幅之內，預示下跌趨勢反轉，股價上升",
    "cover": "Three_White_Soliders.png",
    "footnote": "三日K線"
  },
  {
    "id": 10,
    "title": "三白兵",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "三日K線皆紅，每日收盤價變高且接近最高價，開盤價在前一日實體上半部，預示股價上升",
    "cover": "Three_Stars_In_The_South.png",
    "footnote": "三日K線"
  },
  {
    "id": 11,
    "title": "棄嬰(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "第一天是一根堅挺的紅K，第二天是向上跳空十字線，第三天是一根向下跳空的疲軟綠K且收盤價位於第一天蠟燭線的實體內。",
    "cover": "Abandoned_Baby_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 12,
    "title": "棄嬰(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "第一天是一根疲軟綠K，第二天是向上跳空十字線，第三天是一根向上跳空的堅挺的紅K且收盤價涵蓋第一天蠟燭線的實體。",
    "cover": "Abandoned_Baby_Bullish.png",
    "footnote": "三日K線"
  },
  {
    "id": 13,
    "title": "大敵當前/推進",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "三日都收紅，每日收盤價都比前一日高，開盤價都在前一日實體以內，實體變短，上影線變長。",
    "cover": "Advance_Block.png",
    "footnote": "三日K線"
  },
  {
    "id": 14,
    "title": "執帶(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "第一日紅K，第二日開盤價為最高價的綠K且收盤價接近最低價",
    "cover": "Belt_Hold_Bearish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 15,
    "title": "執帶(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "第一日綠K，第二日開盤價為最低價的紅K且收盤價接近最高價",
    "cover": "Belt_Hold_Bullish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 16,
    "title": "脫離(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，第一日長綠K，第二日跳空綠K，延續趨勢開始震盪，第五日長紅K，收盤價在第一天收盤價與第二天開盤價之間，預示價格上漲。",
    "cover": "Break_Away_Bullish.png",
    "footnote": "五日K線"
  },
  {
    "id": 17,
    "title": "脫離(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "上漲趨勢中，第一日長紅K，第二日跳空紅K，延續趨勢開始震盪，第五日長綠K，收盤價在第一天收盤價與第二天開盤價之間，預示價格下跌。",
    "cover": "Break_Away_Bearish.png",
    "footnote": "五日K線"
  },
  {
    "id": 18,
    "title": "捉腰帶線(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "最低價低於開盤價，收盤價等於最高價，預示著趨勢持續。",
    "cover": "Closing_Marubozu_Bullish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 19,
    "title": "捉腰帶線(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "最高價高於開盤價，收盤價等於最低價，預示著趨勢持續。",
    "cover": "Closing_Marubozu_Bearish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 20,
    "title": "藏嬰吞沒",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，前兩日綠K無影線，第二日開盤、收盤價皆低於第二日，第三日倒鎚頭，第四日開盤價高於前一日最高價，收盤價低於前一日最低價，預示著底部反轉。",
    "cover": "Concealing_Baby_Swallow.png",
    "footnote": "四日K線"
  },
  {
    "id": 21,
    "title": "反擊線(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "後一個紅K僅回升超過前一綠K天的收盤價位置。",
    "cover": "Counter_Attack_Bullish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 22,
    "title": "反擊線(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "後一個綠K僅下跌超過前一天紅K的收盤價位置。",
    "cover": "Counter_Attack_Bearish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 23,
    "title": "烏雲蓋頂",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "第一天是一根堅挺的紅K，第二天開盤價超過了第一天的最高價，但收盤價位於第一天的K棒實體中。",
    "cover": "Dark_CloudCover.png",
    "footnote": "兩日K線"
  },
  {
    "id": 24,
    "title": "CCI 正穿越",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "CCI值由下向上穿越+100或-100",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 25,
    "title": "CCI 負穿越",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "CCI值由上向下穿越-100或+100",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 26,
    "title": "MACD柱線(hist)多頭",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "柱線由負轉正",
    "cover": "",
    "footnote": "talib macd 範例"
  },
  {
    "id": 27,
    "title": "MACD柱線(hist)空頭",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "柱線由正轉負",
    "cover": "",
    "footnote": "https://reurl.cc/y7yQE6"
  },
  {
    "id": 28,
    "title": "RSI 黃金交叉",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "「6天的 RSI 」向上突破「20天的 RSI 」",
    "cover": "",
    "footnote": "talib rsi 範例"
  },
  {
    "id": 29,
    "title": "RSI 死亡交叉",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "「6天的 RSI 」向下跌破「20天的 RSI 」",
    "cover": "",
    "footnote": "https://reurl.cc/65gEak"
  },
  {
    "id": 30,
    "title": "RSI 超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "RSI < 20",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 31,
    "title": "RSI 超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "RSI > 80",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 32,
    "title": "KD 超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "20下方",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 33,
    "title": "KD 超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "80以上",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 34,
    "title": "KD黃金交叉",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "K線從下向上突破D線",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 35,
    "title": "KD死亡交叉",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "K線從上向下突破D線",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 36,
    "title": "KD 高檔背離",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "市場價格創出新高，KD指標卻沒有創出新高",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 37,
    "title": "KD 低檔背離",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "市場價格創出新低，KD指標卻沒有創出新低",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 38,
    "title": "WR 超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "負80到 負100",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 39,
    "title": "WR 超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "0 到 負20 範圍",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 40,
    "title": "WR 高檔背離",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "市場價格創出新高，威廉指標卻沒有創出新高",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 41,
    "title": "WR 低檔背離",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "市場價格創出新低，威廉指標卻沒有創出新低",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 42,
    "title": "Bias 6日超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "大於3.5%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 43,
    "title": "Bias 6日超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "小於-3%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 44,
    "title": "Bias 12日超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "大於＋5%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 45,
    "title": "Bias 12日超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "小於-4.5%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 46,
    "title": "Bias 24日超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "大於8%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 47,
    "title": "Bias 24日超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "小於-7%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 48,
    "title": "Bias 72日超買",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "大於＋11%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 49,
    "title": "Bias 72日超賣",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "小於-11%",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 50,
    "title": "蜻蜓十字/T形十字",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "開盤後價格一路走低，之後收復，收盤價與開盤價相同，預示趨勢反轉",
    "cover": "Dragonfly_Doji.png",
    "footnote": "一日K線"
  },
  {
    "id": 51,
    "title": "多頭吞沒模式",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "多頭吞噬，第一日為綠線，第二日紅線，第一日的開盤價和收盤價在第二日開盤價收盤價之內，但不能完全相同。",
    "cover": "Engulfing_Pattern_Bullish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 52,
    "title": "空頭吞沒模式",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "空頭吞噬，第一日為紅線，第二日綠線，第一日的開盤價和收盤價在第二日開盤價收盤價之內，但不能完全相同。",
    "cover": "Engulfing_Pattern_Bearish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 53,
    "title": "黃昏十字星",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "基本模式為暮星，第二日收盤價和開盤價相同，預示頂部反轉。",
    "cover": "Evening_Doji_Star.png",
    "footnote": "三日K線"
  },
  {
    "id": 54,
    "title": "黃昏之星",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與晨星相反，上升趨勢中，第一日紅線，第二日價格振幅較小，第三日綠線，預示頂部反轉。",
    "cover": "Evening_Star.png",
    "footnote": "三日K線"
  },
  {
    "id": 55,
    "title": "向上跳空並列紅線",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上升趨勢向上跳空，第一日與第二日有相同開盤價，實體長度差不多，則趨勢持續。",
    "cover": "Up_gap_White_Lines.png",
    "footnote": "二日K線"
  },
  {
    "id": 56,
    "title": "向下跳空並列綠線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢向下跳空，第一日與第二日有相同開盤價，實體長度差不多，則趨勢持續。",
    "cover": "Down_gap_White_Lines.png",
    "footnote": "二日K線"
  },
  {
    "id": 57,
    "title": "墓碑十字/倒T十字",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "開盤價與收盤價相同，上影線長，無下影線，預示底部反轉。",
    "cover": "Gravestone_Doji.png",
    "footnote": "一日K線"
  },
  {
    "id": 58,
    "title": "鎚頭",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "實體較短，無上影線，下影線大於實體長度兩倍，處於下跌趨勢底部，預示反轉。",
    "cover": "Hammer.png",
    "footnote": "一日K線"
  },
  {
    "id": 59,
    "title": "上吊線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "形狀與錘子類似，處於上升趨勢的頂部，預示著趨勢反轉。",
    "cover": "Hanging_Man.png",
    "footnote": "一日K線"
  },
  {
    "id": 60,
    "title": "多頭母子線",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "多頭母子，在下跌趨勢中，第一日K線長綠，第二日開盤價收盤價在第一日價格振幅之內，為紅線，預示趨勢反轉，股價上升。",
    "cover": "Harami_Pattern_Bullish.png",
    "footnote": "二日K線"
  },
  {
    "id": 61,
    "title": "空頭母子線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "空頭母子，在上漲趨勢中，第一日K線長紅，第二日開盤價收盤價在第一日價格振幅之內，為綠線，預示趨勢反轉，股價下跌。",
    "cover": "Harami_Pattern_Bearish.png",
    "footnote": "二日K線"
  },
  {
    "id": 62,
    "title": "看漲十字孕線",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "與多頭母子線類似，若第二日K線是十字線，便稱為十字孕線，預示著趨勢反轉。",
    "cover": "Harami_Cross_Pattern_Bullish.png",
    "footnote": "二日K線"
  },
  {
    "id": 63,
    "title": "看跌十字孕線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與空頭母子線類似，若第二日K線是十字線，便稱為十字孕線，預示著趨勢反轉。",
    "cover": "Harami_Cross_Pattern_Bearish.png",
    "footnote": "二日K線"
  },
  {
    "id": 64,
    "title": "風高浪大線/長腳十字線",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "具有極長的上/下影線與短的實體，預示著趨勢反轉。",
    "cover": "High_Wave_Candle.png",
    "footnote": "三日K線"
  },
  {
    "id": 65,
    "title": "多頭陷阱",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "與多頭母子類似，第二日價格在前一日實體範圍內，第三日收盤價高於前兩日，反轉失敗，趨勢繼續。",
    "cover": "Hikkake_Pattern_Bullish.png",
    "footnote": "三日K線"
  },
  {
    "id": 66,
    "title": "空頭陷阱",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與空頭母子類似，第二日價格在前一日實體範圍內，第三日收盤價高於前兩日，反轉失敗，趨勢繼續。",
    "cover": "Hikkake_Pattern_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 67,
    "title": "改良的多頭陷阱",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "與陷阱類似，上升趨勢中，第三日跳空高開；下跌趨勢中，第三日跳空低開，反轉失敗，趨勢繼續。",
    "cover": "Modified_Hikkake_Pattern_Bullish.png",
    "footnote": "三日K線"
  },
  {
    "id": 68,
    "title": "改良的空頭陷阱",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與陷阱類似，上升趨勢中，第三日跳空高開；下跌趨勢中，第三日跳空低開，反轉失敗，趨勢繼續。",
    "cover": "Modified_Hikkake_Pattern_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 69,
    "title": "AR 150以上",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "AR 50以下，表示進入超賣區，可買進股票 AR＝SUM(HIGH-OPEN,N)/SUM(OPEN-LOW,N)*100",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 70,
    "title": "AR 50以下",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "AR 150以上則進入超買區，則請注意回檔或下跌，為賣出時機  AR＝SUM(HIGH-OPEN,N)/SUM(OPEN-LOW,N)*100",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 71,
    "title": "正DI線向上穿越負DI線",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當+DI線向上穿越-DI線時，是買進的交易信號",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 72,
    "title": "正DI線向下穿越負DI線",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當+DI線向下穿越-DI線時，是賣出的交易信號",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 73,
    "title": "VR上升但股價未動",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當VR開始上升但股價未動時，即呈現背離，此時是買進訊號",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 74,
    "title": "VR超過160%-450%",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "當VR超過160%-450%時，很可能會出現多頭後繼無力的情況，應伺機賣出",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 75,
    "title": "VR在40~70%",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "低價區域:70~40為可買進區域",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 76,
    "title": "BR300以上",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "BR300以上為超買區，股價可能隨時回檔，為賣出時機",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 77,
    "title": "BR50以下",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "BR50以下為超賣區，股價可能隨時反彈，為買進時機",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 78,
    "title": "ARBR應用",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當AR及BR急速下降時，表示股價已近高峰，應獲利了結",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 79,
    "title": "ARBR應用",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當BR急速上升，但AR小跌或盤整時，應逢高出貨",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 80,
    "title": "ARBR應用",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當BR比AR低時，可逢低買進",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 81,
    "title": "AD同步上漲",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當AD指標與股價走勢變化同步上漲時，代表行情有機率能夠持續上漲",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 82,
    "title": "AD同步下降",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當AD指標與股價走勢變化同步下降時，代表行情有機率能夠持續下跌",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 83,
    "title": "AD看漲背離",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當股市價格下跌，但AD指標卻呈現上漲趨勢，即是稱為看漲背離。雖然當下是處於下跌，但可以預期行情及香反轉變動往上漲。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 84,
    "title": "AD看跌背離",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當股市價格上漲，但AD指標卻呈現下跌趨勢，即是稱為看跌背離。雖然當下是處於上漲，但可以預期行情及香反轉變動往下跌。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 85,
    "title": "ATR停損",
    "strategyType": "stop loss",
    "signalType": "sell",
    "explanation": "止損設置成某個價格點位下方的1倍或0.5倍ATR",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 86,
    "title": "家鴿",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "與母子線類似，二日K線顏色相同，第二日最高價、最低價都在第一日實體之内。",
    "cover": "Homing_Pigeon_Bullish.png",
    "footnote": "二日K線"
  },
  {
    "id": 87,
    "title": "三胞胎烏鴉",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "上漲趨勢中，三日都為綠線，長度大致相等，每日開盤價等於前一日收盤價，收盤價接近當日最低價，預示價格下跌。",
    "cover": "Identical_Three_Crows_Bearish.png",
    "footnote": "三日K線"
  },
  {
    "id": 88,
    "title": "頸內線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢中，第一日長綠線，第二日開盤價較低，收盤價略高於第一日收盤價，紅線，實體較短。",
    "cover": "In_Neck _Pattern_Bearish.png",
    "footnote": "二日K線"
  },
  {
    "id": 89,
    "title": "倒錘頭",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上影線較長，長度為實體2倍以上，無下影線，在下跌趨勢底部，預示著趨勢反轉。",
    "cover": "Inverted_Hammer_Bullish.png",
    "footnote": "一日K線"
  },
  {
    "id": 90,
    "title": "反沖型態",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "與分離線類似，兩日K線為禿線，顏色相反，存在跳空缺口。",
    "cover": "Kicking_Bullish.png",
    "footnote": "二日K線"
  },
  {
    "id": 91,
    "title": "反沖型態",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與分離線類似，兩日K線為禿線，顏色相反，存在跳空缺口。",
    "cover": "Kicking_Bearish.png",
    "footnote": "二日K線"
  },
  {
    "id": 92,
    "title": "反沖型態（由較長缺影線決定的反沖型態)",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "與反沖型態類似，較長缺影線決定價格的漲跌。",
    "cover": "Kicking_bullbear_determined_by_the_longer_marubozu_Block.png",
    "footnote": "二日K線"
  },
  {
    "id": 93,
    "title": "梯底",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，前三日綠線，開盤價與收盤價皆低於前一日開盤、收盤價，第四日倒錘頭，第五日開盤價高於前一日開盤價，紅線，收盤價高於前幾日價格振幅。",
    "cover": "Ladder_Bottom_Bullish.png",
    "footnote": "五日K線"
  },
  {
    "id": 94,
    "title": "長腳十字",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "開盤價與收盤價相同居當日價格中部，上下影線長，表達市場不確定性。",
    "cover": "Long_Legged_Doji_Bullish.png",
    "footnote": "一日K線"
  },
  {
    "id": 95,
    "title": "長蠟燭線",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "K線實體長，無上下影線。",
    "cover": "Long_Line_Candle_Block.png",
    "footnote": "一日K線"
  },
  {
    "id": 96,
    "title": "光頭光腳/缺影線(熊)",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "上下兩頭都沒有影線的實體，綠線預示著熊市持續或者牛市反轉，紅線相反。",
    "cover": "Marubozu_Bearish.png",
    "footnote": "一日K線"
  },
  {
    "id": 97,
    "title": "光頭光腳/缺影線(牛)",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上下兩頭都沒有影線的實體，紅線預示著熊市持續或者牛市反轉，綠線相反。",
    "cover": "Marubozu_Bullish.png",
    "footnote": "一日K線"
  },
  {
    "id": 98,
    "title": "相同低價/匹配低價",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，第一日長綠K線，第二日綠K線，收盤價與前一日相同，預示底部確認，該價格為支撐位。",
    "cover": "Matching_Low_Bullish.png",
    "footnote": "二日K線"
  },
  {
    "id": 99,
    "title": "鋪墊",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "第一日紅K線，第二日跳空高開影線，第三、四日短實體影線，第五日紅K線，收盤價高於前四日，預示趨勢持續。",
    "cover": "Mat_Hold_Bullish.png",
    "footnote": "五日K線"
  },
  {
    "id": 100,
    "title": "十字晨星/早晨十字星",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "基本模式為晨星，第二日K線為十字星，預示底部反轉。。",
    "cover": "Morning_Doji_Star_Bullish.png",
    "footnote": "三日K線"
  },
  {
    "id": 101,
    "title": "晨星",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢，第一日綠K線，第二日價格振幅較小，第三天紅K線，預示底部反轉。",
    "cover": "Morning_Star_Bullish.png",
    "footnote": "三日K線"
  },
  {
    "id": 102,
    "title": "頸上線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢中，第一日長綠K線，第二日開盤價較低，收盤價與前一日最低價相同，紅線，實體較短，預示著延續下跌趨勢",
    "cover": "On_Neck_Pattern_Bearish.png",
    "footnote": "兩日K線"
  },
  {
    "id": 103,
    "title": "刺透型態",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，第一日綠K線，第二日收盤價低於前一日最低價，收盤價處在第一日實體上部，預示著底部反轉。",
    "cover": "Piercing Pattern.png",
    "footnote": "兩日K線"
  },
  {
    "id": 104,
    "title": "黃包車夫線",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "與長腿十字線類似，若實體正好處於價格振幅中點，稱為黃包車夫。",
    "cover": "Rickshaw Man.png",
    "footnote": "一日K線"
  },
  {
    "id": 105,
    "title": "上升三法",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上漲趨勢中，第一日長紅K線，中間三日價格在第一日範圍內小幅震盪，第五日長紅K線，收盤價高於第一日收盤價，預示股價上升。",
    "cover": "Rising Three Methods.png",
    "footnote": "五日K線"
  },
  {
    "id": 106,
    "title": "下降三法",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢中，第一日長綠K線，中間三日價格在第一日範圍內小幅震盪，第五日長綠K線，收盤價低於第一日收盤價，預示股價下跌。",
    "cover": "Falling Three Methods.png",
    "footnote": "五日K線"
  },
  {
    "id": 107,
    "title": "上升分離/分割線",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上漲趨勢中，第一日綠K線，第二日紅K線，第二日開盤價與第一日相同且為最低價，預示著趨勢繼續。",
    "cover": "Rising Separating Lines.png",
    "footnote": "兩日K線"
  },
  {
    "id": 108,
    "title": "下降分離/分割線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢中，第一日紅K線，第二日綠K線，第二日開盤價與第一日相同且為最高價，預示著趨勢繼續。",
    "cover": "Falling Separating Lines.png",
    "footnote": "兩日K線"
  },
  {
    "id": 109,
    "title": "射擊之星/流星線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "上影線至少為實體長度兩倍，沒有下影線，預示著股價下跌",
    "cover": "Shooting Star.png",
    "footnote": "一日K線"
  },
  {
    "id": 110,
    "title": "短蠟燭線",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "具有較短實體和上下影線的一根蠟燭線。此型態並不表示任何看漲或者看跌。",
    "cover": "Short Line Candle.png",
    "footnote": "一日K線"
  },
  {
    "id": 111,
    "title": "紡錘線",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "實體小。",
    "cover": "Spinning Top.png",
    "footnote": "一日K線"
  },
  {
    "id": 112,
    "title": "停頓形態",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "上漲趨勢中，第二日長紅K線，第三日開盤於前一日收盤價附近，短紅K線，預示著上漲結束。",
    "cover": "Stalled Pattern.png",
    "footnote": "三日K線"
  },
  {
    "id": 113,
    "title": "條形三明治",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "第一日長綠K線，第二日紅K線，開盤價高於前一日收盤價，第三日開盤價高於前兩日最高價，收盤價於第一日收盤價相同。",
    "cover": "Stick Sandwich.png",
    "footnote": "三日K線"
  },
  {
    "id": 114,
    "title": "探水竿",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "大致與蜻蜓十字相同，下影線長度長。",
    "cover": "Takuri.png",
    "footnote": "一日K線"
  },
  {
    "id": 115,
    "title": "跳空並列紅線",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "前兩日紅K線，第二日跳空，第三日綠K線，收盤價於缺口中，上升趨勢持續。",
    "cover": "Upside Tasuki Gap.png",
    "footnote": "三日K線"
  },
  {
    "id": 116,
    "title": "跳空並列綠線",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "前兩日綠K線，第二日跳空，第三日紅K線，收盤價於缺口中，下跌趨勢持續。",
    "cover": "Downside Tasuki Gap.png",
    "footnote": "三日K線"
  },
  {
    "id": 117,
    "title": "插入形態",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "與頸上線類似，下跌趨勢中，第一日長綠K線，第二日開盤價跳空，收盤價略低於前一日實體中部，與頸上線相比實體較長，預示著趨勢持續。",
    "cover": "Thrusting Pattern.png",
    "footnote": "兩日K線"
  },
  {
    "id": 118,
    "title": "三星形態",
    "strategyType": "candlestick pattern",
    "signalType": "non",
    "explanation": "由三個十字組成，第二日十字必須高於或者低於第一日和第三日，預示著反轉。",
    "cover": "Tristar Pattern.png",
    "footnote": "三日K線"
  },
  {
    "id": 119,
    "title": "獨特三河",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "下跌趨勢中，第一日長綠K線，第二日為鎚頭，最低價創新低，第三日開盤價低於第二日收盤價，收紅K線，收盤價不高於第二日收盤價，預示著反轉，第二日下影線越長可能性越大。",
    "cover": "Unique Three River.png",
    "footnote": "三日K線"
  },
  {
    "id": 120,
    "title": "向上跳空的兩隻烏鴉/雙飛烏鴉",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "第一日紅K線，第二日跳空以高於第一日最高價開盤，收綠K線，第三日開盤價高於第二日，收綠K線，與第一日比仍有缺口。",
    "cover": "Upside Gap Two Crows.png",
    "footnote": "三日K線"
  },
  {
    "id": 121,
    "title": "上升跳空三法",
    "strategyType": "candlestick pattern",
    "signalType": "buy",
    "explanation": "上漲趨勢中，第一日長紅K線，第二日短紅K線，第三日跳空紅K線，第四日綠K線，開盤價與收盤價於前兩日實體內，第五日長紅K線，收盤價高於第一日收盤價，預示股價上升。",
    "cover": "Upside Gap Three Methods.png",
    "footnote": "五日K線"
  },
  {
    "id": 122,
    "title": "下降跳空三法",
    "strategyType": "candlestick pattern",
    "signalType": "sell",
    "explanation": "下跌趨勢中，第一日長綠K線，第二日短綠K線，第三日跳空綠K線，第四日紅K線，開盤價與收盤價於前兩日實體內，第五日長綠K線，收盤價高於第一日收盤價，預示股價下跌。",
    "cover": "Downside Gap Three Methods.png",
    "footnote": "五日K線"
  },
  {
    "id": 123,
    "title": "ROC於極低位置",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "ROC下降到極低位置時，指標達到超賣水平，產生買入信號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 124,
    "title": "ROC於極高位置",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "ROC上升到極高位置時，指標達到超買水平，產生賣出信號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 125,
    "title": "MFI買入",
    "strategyType": "index value",
    "signalType": "buy",
    "explanation": "MFI低於 20",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 126,
    "title": "MFI賣出",
    "strategyType": "index value",
    "signalType": "sell",
    "explanation": "MFI高於 80",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 127,
    "title": "MFI與股價反向背離買入",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當股價和 MFI 反向背離時，股價出現新低點，而 MFI 出現較高點，可以視為買入訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 128,
    "title": "MFI與股價反向背離賣出",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當股價和 MFI 反向背離時，股價出現新高點，而 MFI 出現較低點，可以視為賣出訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 129,
    "title": "OBP",
    "strategyType": "index trend",
    "signalType": "non",
    "explanation": "整日對比股價上升日的交易量累計 - 整日對比股價下跌的交易量累計。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 130,
    "title": "PVI向上穿越均線",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "PVI指標由下往上穿越其200天移動平均線，代表買進訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 131,
    "title": "PVI向下穿越均線",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "PVI指標由上往下穿越其200天移動平均線時，代表賣出訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 132,
    "title": "NVI向上穿越均線",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "NVI指標由下往上穿越其200天移動平均線，代表買進訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 133,
    "title": "NVI向下穿越均線",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "NVI指標由上往下穿越其200天移動平均線時，代表賣出訊號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 134,
    "title": "MTM與均值線在中心線上方",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "當動量值曲線和均值曲線都在中心線（0水平）上方時，如果動量值高於均值，此次為買入信號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 135,
    "title": "MTM與均值線在中心線下方",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "當動量值曲線和均值線都在中心線（0水平）下方時，如果動量值低於均值，此次為賣出信號。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 136,
    "title": "MTM向下穿越中心線",
    "strategyType": "index trend",
    "signalType": "sell",
    "explanation": "MTM曲線由上向下跌破中心線（0水平）時，指示價格走勢進入下行趨勢，為賣出時機。",
    "cover": "",
    "footnote": ""
  },
  {
    "id": 137,
    "title": "MTM向上穿越中心線",
    "strategyType": "index trend",
    "signalType": "buy",
    "explanation": "MTM曲線由下向上突破中心線（0水平）時，指示價格進入上行趨勢，為買進時機。",
    "cover": "",
    "footnote": ""
  }
]

filter = [
    {'candlestick pattern': True},
    {'index trend': True},
    {'index number': True},
    {'strategic stop': True},
    {'buy': True},
    {'sell': True},
    {'wait': True},
    ]

for strategy in strategies:
    if strategy['cover'] == '':
        strategy['cover'] = 'question-mark.jpg'
    if strategy['footnote'] == '':
        strategy['footnote'] = '備註備註備註'
    if strategy['explanation'] == '':
        strategy['explanation'] = '描述描述描述'
    strategy['cover'] = f'/static/assets/img/candlestick-patterns/' + strategy['cover']
    print(strategy['cover'])
    # for key, value in strategy.items():
    #     print(value)
    # print('-'*40)