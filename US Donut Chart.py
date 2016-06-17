# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
py.sign_in('alfredoyax98' , '8mdj5hjrms')
import plotly.graph_objs as go

fig = {
  "data": [
    {
      "values": [28, 25, 21, 10, 6, 3, 2, 2, 2, 1],
      "labels": [
        "Health Care",
        "Pensions",
        "Defense",
        "Welfare",
        "Interest",
        "Education",
        "Protection",
        "Transportation",
        "Other Spending",
        "General Government"
        
      ],
      "domain": {"x": [0, .48]},
      "name": "2016 US Spending",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [26, 26, 23, 11, 7, 3, 3, 1, 1],
      "labels": [
        "Health Care",
        "Pensions",
        "Defense",
        "Welfare",
        "Interest",
        "Education",
        "Protection",
        "Transportation",
        "General Government"
      ],
      "text":"2016 US Spending",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "2014 US Spending",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"US Spending 2016 vs 2014",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "2016",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "2014",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}

url = py.plot(fig, filename='US Spendings')