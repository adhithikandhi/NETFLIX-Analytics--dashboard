import plotly.express as px

def retention_chart(df):

    fig = px.line(
        df,
        x="Watch_Time",
        y="User_ID",
        title="Viewer Retention Curve",
        markers=True,
        template="plotly_dark"
    )

    fig.update_layout(
        height=450
    )

    return fig


def device_chart(df):

    fig = px.pie(
        df,
        names="Device",
        hole=.55,
        title="Device Distribution",
        template="plotly_dark"
    )

    return fig


def network_chart(df):

    fig = px.bar(
        df,
        x="Network",
        y="Speed",
        color="Network",
        template="plotly_dark",
        title="Network Speed"
    )

    return fig