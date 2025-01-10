from pathlib import Path
import json

path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/recent_eq/eq_data_7_day_m1.geojson')
path.exists()
contents = path.read_text(encoding='utf-8')
eq_data = json.loads(contents)

path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/recent_eq/readable_eq_data.geojson')
readable_contents = json.dumps(eq_data, indent=4)
path.write_text(readable_contents)

print(eq_data['metadata']['title'])