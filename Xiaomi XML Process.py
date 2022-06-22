import json
import sys
import xmltodict
import dicttoxml
import collections

collections.Iterable = collections.abc.Iterable

try:
    config_file = sys.argv[1]
except Exception:
    print('没有传入小米备份descript.xml文件')
    sys.exit()

with open(config_file, 'r', encoding='utf8') as f1:
    data = xmltodict.parse(f1.read())

data['MIUI-backup'].pop('filesModifyTime')
need_delete_index = []
for index, value in enumerate(data['MIUI-backup']['packages']['package']):
    if value['packageName'] == 'files_for_backup':
        need_delete_index.append(index)

while len(need_delete_index) > 0:
    data['MIUI-backup']['packages']['package'].pop(need_delete_index.pop(0))
    need_delete_index = [i - 1 for i in need_delete_index]

data['MIUI-backup']['packages'] = data['MIUI-backup']['packages']['package']

item_func = lambda x: 'package'

with open(config_file, 'w', encoding='utf8') as f2:
    f2.write(dicttoxml.dicttoxml(data['MIUI-backup'], attr_type=False, custom_root='MIUI-backup', item_func=item_func).decode('utf-8'))
