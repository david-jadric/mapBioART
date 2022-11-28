
import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('Art_Sci_Gallaries_World.csv')
fig = px.choropleth(df, locations="ISO",
                    color = 'Gallaries',
                    hover_name= "Countries",
                    color_continuous_scale="Viridis"
                    )
fig.show()


pio.write_html(fig, file='index.html', auto_open=True)
