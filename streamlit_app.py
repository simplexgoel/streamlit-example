from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

"""
# Welcome to Aflatoon!



We are busy building this website....


"""
st.sidebar.image('./Aflatoon.jpg', caption='Aflatoon', use_column_width=True, output_format="auto")



widgetStr = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_c2bcc"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/AMEX-SPY/" rel="noopener" target="_blank"><span class="blue-text">SPY Chart</span></a> </div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 600,
  "height": 400,
  "symbol": "AMEX:SPY",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_c2bcc"
  }
      );
      </script>
  </div>
<!-- TradingView Widget END -->
"""
# bootstrap 4 collapse example
components.html(widgetStr, height=600,    )
st.balloons()
#with st.echo(code_location='below'):
total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns

for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    radius = curr_point_num / total_points
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    data.append(Point(x, y))

st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)
    .encode(x='x:Q', y='y:Q'))
