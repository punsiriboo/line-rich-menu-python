import os
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dotenv import load_dotenv
from linebot.v3.insight import ApiClient, Configuration, Insight

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
insight_api = Insight(api_client)


def get_rich_menu_summary(rich_menu_id: str, from_date: str, to_date: str):
    try:
        response = insight_api.get_rich_menu_insight_summary(rich_menu_id, from_date, to_date)
        print(f"Summary {rich_menu_id} ({from_date} - {to_date})")
        pprint(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_rich_menu_daily(rich_menu_id: str, from_date: str, to_date: str):
    try:
        response = insight_api.get_rich_menu_insight_daily(rich_menu_id, from_date, to_date)
        print(f"Daily {rich_menu_id} ({from_date} - {to_date})")
        pprint(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def has_metrics(response):
    return bool(response and response.impression and response.impression.metrics)

def plot_summary(response):
    if not has_metrics(response):
        print("No summary metrics. LINE returns only richMenuId when:")
        print("- unique users are below privacy threshold, or")
        print("- no impressions/clicks yet, or")
        print("- stats are not ready (usually available next day)")
        return

    rows = [
        {"label": "Impressions", "metric": "Count", "value": response.impression.metrics.count},
        {"label": "Impressions", "metric": "Unique users", "value": response.impression.metrics.unique_users},
    ]
    for i, click in enumerate(response.clicks or []):
        rows.append({"label": f"Area {i + 1}", "metric": "Count", "value": click.metrics.count})
        rows.append({"label": f"Area {i + 1}", "metric": "Unique users", "value": click.metrics.unique_users})

    fig = px.bar(
        pd.DataFrame(rows),
        x="label",
        y="value",
        color="metric",
        barmode="group",
        title=f"Rich Menu Summary ({response.metrics_from} - {response.metrics_to})",
        labels={"label": "", "value": "Count", "metric": "Metric"},
    )
    fig.show()

def plot_daily(response):
    if not has_metrics(response):
        print("No daily metrics to plot (same reasons as summary)")
        return

    impression_rows = []
    for m in response.impression.metrics:
        impression_rows.append({"date": m.var_date, "metric": "Count", "value": m.count})
        impression_rows.append({"date": m.var_date, "metric": "Unique users", "value": m.unique_users})

    click_rows = []
    for i, click in enumerate(response.clicks or []):
        for m in click.metrics or []:
            click_rows.append({"date": m.var_date, "area": f"Area {i + 1}", "value": m.count})

    fig = make_subplots(rows=2, cols=1, subplot_titles=("Daily Impressions", "Daily Clicks by Area"), shared_xaxes=True)

    for metric, group in pd.DataFrame(impression_rows).groupby("metric"):
        fig.add_trace(go.Scatter(x=group["date"], y=group["value"], mode="lines+markers", name=metric), row=1, col=1)

    if click_rows:
        for area, group in pd.DataFrame(click_rows).groupby("area"):
            fig.add_trace(go.Scatter(x=group["date"], y=group["value"], mode="lines+markers", name=area), row=2, col=1)

    fig.update_xaxes(title_text="Date (yyyyMMdd)", row=2, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)
    fig.update_yaxes(title_text="Clicks", row=2, col=1)
    fig.update_layout(height=700, title_text="Rich Menu Daily Stats")
    fig.show()

if __name__ == "__main__":
    rich_menu_id = "richmenu-1d2e62eb1e49dc5e98de2a3a72ae4369"
    from_date, to_date = "20260701", "20260713"
    summary = get_rich_menu_summary(rich_menu_id, from_date, to_date)
    daily = get_rich_menu_daily(rich_menu_id, from_date, to_date)
    plot_summary(summary)
    plot_daily(daily)

