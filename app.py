
from pathlib import Path
import pandas as pd
# issue with installing polars within the shinylive environment

from shiny import reactive
from shiny.express import input, render, ui


df = pd.read_csv(Path(__file__).parent / "mtcars.csv")

#pip install shinylive --upgrade

with ui.navset_card_pill(id="tab"):  

    with ui.nav_panel("Data frame"):
        @render.data_frame
        def frame():
            return dat()

    with ui.nav_panel("Table"):
        @render.table
        def table():
            return dat()
                

with ui.sidebar(title="Filters"):
    ui.input_slider(
        "mpg",
        "MPG",
        min=df["mpg"].min(),
        max=df["mpg"].max(),
        value=[df["mpg"].min(), df["mpg"].max()]
    )


@reactive.calc
def dat():
    return df[(df["mpg"] >= input.mpg()[0]) & (df["mpg"] <= input.mpg()[1])]
