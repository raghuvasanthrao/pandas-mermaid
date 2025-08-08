**`README.md`**

```markdown
# pandas-mermaid

Convert a **pandas DataFrame** into a **Mermaid flowchart** definition.

## 📦 Installation

Install from **PyPI**:

```bash
pip install pandas-mermaid
```

Or install the latest development version from GitHub:

```bash
pip install git+https://github.com/raghuvasanthrao/pandas-mermaid.git
```

## 🚀 Usage

```python
import pandas as pd
from pandas_mermaid.converter import df_to_mermaid

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Node1', 'Node2', 'Node3'],
    'Value': [10, 20, 30],
})

# Get Mermaid string
mermaid_code = df_to_mermaid.df_to_mermaid(df, direction="LR")
print(mermaid_code)

# Create HTML content
html_content = df_to_mermaid.to_html(mermaid_code)

# Save HTML file
with open("diagram.html", "w", encoding="utf-8") as f:
    f.write(html_content)
```

**Output:**

```
flowchart LR
    node0[Name: Node1, Value: 10]
    node1[Name: Node2, Value: 20]
    node2[Name: Node3, Value: 30]
    node0 --> node1
    node1 --> node2
```

You can paste the above output into [Mermaid Live Editor](https://mermaid.live/) to visualize the flowchart.

## 📄 License

This project is licensed under the MIT License.

```
---

If you want, I can also **add a rendered Mermaid diagram directly into the README** so that when someone views your GitHub page, they’ll see the flowchart without leaving the page. That would make the repo look even more appealing.  

Do you want me to add that?
```
