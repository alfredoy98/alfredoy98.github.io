import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['2000', '2004', '2008', '2012', '2016', '2020'],
    y=[5800000000000, 7300000000000, 10000000000000, 15500000000000, 19300000000000, 21100000000000],
    name='Primary Product',
    marker=dict(
        color='rgb(49,130,189)'
    )

)
data = [trace0]
layout = go.Layout(
    xaxis=dict(
        # set x-axis' labels direction at 45 degree angle
        tickangle=-45,
    ),
    barmode='group',
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='angled-text-bar')
