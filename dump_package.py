import os
import json

os.environ['DJANGO_SETTINGS_MODULE'] = 'editor.settings'

from django.conf import settings

from apps.goodspackage.models import Package


FIXTURE_DIR = settings.FIXTURE_DIRS[0]

data = {}
for p in Package.objects.all():
    data[p.id] = p.export_data()

with open(os.path.join(FIXTURE_DIR, 'package.json'), 'w') as f:
    f.write(json.dumps(data, indent=4))

