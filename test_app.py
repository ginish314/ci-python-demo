import importlib.util
import sys
from pathlib import Path

# Dynamically load app.py as module
spec = importlib.util.spec_from_file_location("app", Path(__file__).parent / "app.py")
app = importlib.util.module_from_spec(spec)
sys.modules["app"] = app
spec.loader.exec_module(app)

def test_add():
    assert app.add(2, 3) == 5


