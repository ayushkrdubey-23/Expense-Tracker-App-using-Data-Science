# Step 6 - Installation Guide: Expense Tracker App

This guide covers Python setup, library installation, virtual environment creation, and platform-specific commands for Windows and Mac.

---

## Prerequisites

- Python 3.8 or higher (3.10+ recommended)
- pip (comes with Python)
- Internet connection (to install libraries)
- Git (optional, for version control and GitHub upload)

---

## Step 6.1: Check Python Installation

Open a terminal/command prompt and run:

```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.x.x`

If Python is not installed, download it from https://www.python.org and install it. During installation on Windows, **check "Add Python to PATH"**.

---

## Step 6.2: Create Project Folder and Navigate

```powershell
# Windows (PowerShell)
mkdir Expense-Tracker-App-using-Data-Science
cd Expense-Tracker-App-using-Data-Science
```

```bash
# Mac / Linux
mkdir Expense-Tracker-App-using-Data-Science
cd Expense-Tracker-App-using-Data-Science
```

---

## Step 6.3: Create Virtual Environment

A virtual environment isolates project dependencies so they don't conflict with other projects.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### Mac / Linux (Terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Verify activation:**
- Your terminal prompt should now show `(.venv)` at the beginning.
- Run `which python` (Mac/Linux) or `Get-Command python` (Windows) to confirm it points to the `.venv` folder.

---

## Step 6.4: Install Required Libraries

Create `requirements.txt` with the following content:

```
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
streamlit>=1.28.0
```

Install all libraries:

```powershell
# Windows / Mac / Linux (same command after venv activation)
pip install -r requirements.txt
```

**Expected output:** `Successfully installed pandas-... numpy-... matplotlib-... seaborn-... streamlit-...`

Verify installation:

```bash
pip list
```

You should see `pandas`, `numpy`, `matplotlib`, `seaborn`, and `streamlit` in the list.

---

## Step 6.5: Initialize Git (Optional but Recommended)

```bash
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"
```

---

## Platform-Specific Notes

### Windows
- Use PowerShell or Command Prompt
- Activation script: `.venv\Scripts\Activate.ps1`
- Path separator: `\`
- If `python` command is not found, try `py` or `python3`

### Mac
- Use Terminal
- Activation script: `source .venv/bin/activate`
- Python may be `python3` instead of `python`
- If you installed Python via Homebrew, use `python3 -m venv .venv`

---

## Step 6.6: Verify the Setup

Create a quick test file `test_setup.py`:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

print("pandas:", pd.__version__)
print("numpy:", np.__version__)
print("matplotlib:", plt.matplotlib.__version__)
print("seaborn:", sns.__version__)
print("streamlit:", st.__version__)
print("All libraries installed successfully!")
```

Run it:

```bash
python test_setup.py
```

Expected output:
```
pandas: 2.x.x
numpy: 1.x.x
matplotlib: 3.x.x
seaborn: 0.x.x
streamlit: 1.x.x
All libraries installed successfully!
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `pip` not found | Use `python -m pip install ...` or `pip3 install ...` |
| Activation blocked (Windows) | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `streamlit` command not found | Run `python -m streamlit ...` or ensure venv is activated |
| Permission denied on Mac | Use `python3 -m pip install --user ...` or fix folder permissions |
| Library version conflicts | Delete `.venv` and recreate, then reinstall |

---

## Next Step

After installation is complete, proceed to **Step 7 (Full Project Code)** where you will create `main.py` and the `src/` modules.

---

**Step 6 complete.** Installation guide defined for Windows and Mac with virtual environment, library installation, and verification.

Please reply with **"c"** to acknowledge Step 6, and I will proceed to Step 7 (Full Project Code).