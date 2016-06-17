import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Ireland', 'UK', 'US', 'Japan', 'Greece', 'Spain', 'France', 'Poland', 'Czech Republic', 'Portugal'],
    y=[10.8, 10.3, 8.9, 8.3, 7.1, 7, 6.9, 6.5, 5.7, 5.6],
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
