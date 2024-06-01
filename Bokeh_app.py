# Required Libraries
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.models import ColorBar, LinearColorMapper
import pandas as pd

# Load Dataset
dataset_path = '/mnt/data/Date_final_dataset_balanced_float32.parquet.zip'
df = pd.read_parquet(dataset_path)

# Prepare Data
source = ColumnDataSource(df)

# Create Figures
p1 = figure(title="NDVI over Time", x_axis_type='datetime', plot_height=400, plot_width=800)
p1.line('acq_date', 'NDVI', source=source, color='green')

p2 = figure(title="Soil Moisture over Time", x_axis_type='datetime', plot_height=400, plot_width=800)
p2.line('acq_date', 'SoilMoisture', source=source, color='blue')

p3 = figure(title="Temperature over Time", x_axis_type='datetime', plot_height=400, plot_width=800)
p3.line('acq_date', 'average_temperature_yearly_mean', source=source, color='orange', legend_label='Average Temp')
p3.line('acq_date', 'maximum_temperature_yearly_mean', source=source, color='red', legend_label='Max Temp')
p3.line('acq_date', 'minimum_temperature_yearly_mean', source=source, color='blue', legend_label='Min Temp')
p3.legend.location = "top_left"

p4 = figure(title="Precipitation over Time", x_axis_type='datetime', plot_height=400, plot_width=800)
p4.line('acq_date', 'precipitation_yearly_mean', source=source, color='purple')

# Correlation Heatmap
correlation_matrix = df.corr()
correlation_matrix.index.name = 'Features'
correlation_matrix.columns.name = 'Features'

corr_source = ColumnDataSource(correlation_matrix.stack().rename("value").reset_index())

mapper = LinearColorMapper(palette="Viridis256", low=correlation_matrix.values.min(), high=correlation_matrix.values.max())

p5 = figure(title="Correlation Heatmap", x_range=list(correlation_matrix.index), y_range=list(correlation_matrix.columns),
            plot_height=400, plot_width=800, toolbar_location=None, tools="", x_axis_location="above")

p5.rect(x="Features", y="Features", width=1, height=1, source=corr_source,
        fill_color={'field': 'value', 'transform': mapper}, line_color=None)

color_bar = ColorBar(color_mapper=mapper, location=(0, 0), title="Correlation")

p5.add_layout(color_bar, 'right')

# Create Interactions
select = Select(title="Select Data", value="NDVI", options=["NDVI", "SoilMoisture", "Average Temp", "Max Temp", "Min Temp", "Precipitation"])

def update_plot(attr, old, new):
    selected = select.value
    if selected == "NDVI":
        p1.line('acq_date', 'NDVI', source=source, color='green')
    elif selected == "SoilMoisture":
        p2.line('acq_date', 'SoilMoisture', source=source, color='blue')
    elif selected == "Average Temp":
        p3.line('acq_date', 'average_temperature_yearly_mean', source=source, color='orange', legend_label='Average Temp')
    elif selected == "Max Temp":
        p3.line('acq_date', 'maximum_temperature_yearly_mean', source=source, color='red', legend_label='Max Temp')
    elif selected == "Min Temp":
        p3.line('acq_date', 'minimum_temperature_yearly_mean', source=source, color='blue', legend_label='Min Temp')
    elif selected == "Precipitation":
        p4.line('acq_date', 'precipitation_yearly_mean', source=source, color='purple')

select.on_change('value', update_plot)

# Layout
layout = column(select, row(p1, p2), row(p3, p4), p5)

# Add to Document
curdoc().add_root(layout)
