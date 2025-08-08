import pandas as pd

def df_to_mermaid(df: pd.DataFrame, direction: str = "TD") -> str:
    """
    Convert a pandas DataFrame to a Mermaid flowchart string.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame where each row represents a node.
    direction : str
        Flowchart direction ("TD", "LR", etc.).

    Returns
    -------
    str
        Mermaid flowchart definition.
    """
    if df.empty:
        raise ValueError("DataFrame is empty.")

    chart = [f"flowchart {direction}"]

    # Convert each row into a node label
    for i, row in df.iterrows():
        label = ", ".join(f"{col}: {val}" for col, val in row.items())
        chart.append(f"    node{i}[{label}]")

    # Add edges
    for i in range(len(df) - 1):
        chart.append(f"    node{i} --> node{i+1}")

    return "\n".join(chart)
