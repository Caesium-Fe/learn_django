OTA Daily Report Tool

Report.py 的 4243行开始整理出summary数据





在使用cx_oracle组件时，需要环境中有instancetclient包中所有的.dll文件，将这些dll文件放在python.exe同级目录下就可以了。





字典在进行copy时，只是深复制字典本身，但是字典中的对象任然是引用，所以如果字典中出现新对象，则需要使用 new_dict = copy.deepcopy(old_dict)



# 重构

## UI

```

_is_vswr 判断是否为vswr， 走特殊处理逻辑，报告名称，  对应Data source

_delete_retest 判断是否删除重测数据 对应Keep Re-test Data
_if_fa 判断是否为fa 对应Keep Re-test Data

_t_distance 中间时间跨度时间 对应Keep FA time

_isNA， _isNA_ether， _isNA_sota， _isNA_mars， _isNA_aoa 判断是否删除NA limit数据

_data_type 为 por还是doe数据 对应 Data Type

_is_apple_pass 判断是否需要apple pass 对应 Apple Pass

_auto_select_item 需要打开一份excel，给用户填写，用于不走keyword逻辑， 逻辑在 _get_item_data 中

_if_consum 判断是否需要config summary， 对应Config-Summary

_if_del_format 是否需要删除删除数据样式， 对应Remove data style

_top10 用于summary页展示失败和重测数据个数 对应Fail item amount

_if_slim 用来处理数据时走特殊处理（dataprocess， _process_keyword_info）对应 Slimming data

_sota_pass_fail_mode 各工站算pass和fail的依照（items还是status）
_mars_pass_fail_mode
_omnia_pass_fail_mode
_other_pass_fail_mode

_omnia_empty_value ota工站的空数据算pass还是fail

_same_sn 对重复SN有关， 对应 Only Report Same SN
```

## Keyword

- **ItemSelection**

  ```
  ItemSelection  筛选
  检索：select_item.py的get_select_sheet()
  ```
  
- **Map**

  ```
  通过map获取Expect Scenairo。
  keyword中的Real Scenario，对应csv中的第一个格子的值。
  检索：select_item.py中的read_omnia_station_map()
  影响范围：如果map中没有对应上的，才走获取Omnia Split staton sheet、Omnia Summary SKU mapping sheet的逻辑，检索select_item.py的is_omnia_ota()
  ```

- **SelectConfig**

  ```
  保留sheet填写的config数据，其他不要
  检索：ReportData.py的_select_user_care_configs()
  ```

  

- **DeleteConfig**

  ```
  selectconfig sheet没填时，删除这个sheet的config，填了就不跑删除的逻辑了
  检索：ReportData.py的_select_user_care_configs()
  ```

  

- **station order**

  ```
  csv文件排序根据这个index顺序
  检索：Report.py的 _sorted_by_stationorder_sheet()
  ```

- **Delete SN**

  ```
  删除sn在这个sheet的数据
  检索：Report.py的_get_delete_sn_keyword()
  ```

- **Limits Keyword**

  ```
  讀取limits keyword的對應工站的關鍵字組合的测试项的lower、upper limits
  對應值填寫到daily report中,即根据keyword修改report中对应测试项的limit值
  检索：Report.py的_limits_keyword()  change_limits.py的change_limits()
  ```

- **SplitData**

  ```
  根据这个sheet，对一个csv数据，分割成多个，按照config分割，这里的config是csv中的Special Build Description列的‘_’分割的末尾的值
  ！！keyword里面需要包含csv的全部config，否则raise
  检索：Report.py的_split_csv_data()
  ```

- **Omnia Summary SKU mapping**

  ```
  Key可能是Product、Version，
  匹配csvKey对应的Value来分SKU，value的‘/’为或
  检索：ReportData.py的_stay_sku_sn()
  ```

  

- **Omnia Split staon**

  ```
  会判断是否Omnia数据：Report.py的omnia_station和omnia_station_all，str和list类型。根据这个类型改掉csv的第一个数据值
  ```

  

- **REDSIG-OTA-LAT**

- **combine csv**

- **AntGroup**

- **Report name**

  ```
  Report name  报告名称  检索：get_report_name
  ```

- 

- ```
  split_for_tech
  ```



## sn文件

```
_is_sn bool值，取决于是否有sn文件
1. 读取文件
ReportData.py	_get_key_part()
2. 主要操作
	2.1 目录中需要有sn.xlsx
	2.2 通过SN.xlsx文件获取keypart 信息，为后面的byconfig, bykeypart工具做准备
	2.3 
3. 影响范围


```

## Auto Select

```
item_excel_path  item select文件的路径，用于_get_item_data方法
1. 读取文档
ReportInterface.py set_item_excel()->item_excel_path
2. 主要操作
	2.1 在ui上需要选择Auto-select Item选N
	2.2 自动生成item.xlsx文档，Item sheet
	2.3 填写后筛选item
3. 影响范围
最后item
```



对DailyReport进行需求整理，做好记录

（整理keyword、ui、sn.xlsx、bandsequence.xlsx影响范围，整理报表数据的生成逻辑、标色逻辑）

## bandsequence.xlsx

```
1. 读取文档
bandsequence.py， xlsx三个sheet:tx,rx,bandgroup
2. 主要操作
	2.1 tx sheet读取band的这一列，保存在变量self.band_tx中，band_tx_dict是self.band_tx值作为key，index作为value的dict。rx sheet相同
	2.2 没有传bandsequence.xlsx的路径时，有一个默认的band_tx，在defalut_keyword()中
	2.3 bandgroup sheet保存在self.bandorder、self.band_dict里，bandorder是第一行的band值，band_dict = {'tx':{band类型1800-2000M:[一列的band值B17]}}
	2.4 main_band_label()中，把tx和rx的每个band对应的band type对应保存在self.band_label_dict中
3. 影响范围
sort_item() 方法中tx， rx排序会用到	ReportData.py by_band()
```

