import pandas as pd

class df_to_mermaid:
    @staticmethod
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

    @staticmethod
    def to_html(mermaid_code: str) -> str:
        """
        Wrap Mermaid flowchart code into an HTML document 
        that can be opened in a browser.

        Parameters
        ----------
        mermaid_code : str
            Mermaid flowchart definition.

        Returns
        -------
        str
            HTML content containing the rendered Mermaid diagram.
        """
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Mermaid Diagram</title>
            <script type="module">
              import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
              mermaid.initialize({{ startOnLoad: true }});
            </script>
        </head>
        <body>
            <div class="mermaid">
{mermaid_code}
            </div>
        </body>
        </html>
        """
        return html_template
