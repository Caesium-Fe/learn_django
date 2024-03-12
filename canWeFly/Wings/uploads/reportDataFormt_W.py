class API():
	def __init__(self, sheetname=None):
		self.__frist_row = Data1()
		self.sn_part = [Data2(), Data2()]
		self.item_part = [Data3, Data3]
	
	@property
	def frist_row(self):
		return self.__frist_row
	
	@property
	def sn_part(self):
		return self.__sn_part
	
	@property
	def item_part(self):
		return self.__item_part
		
		
	
class Data2():
	def __init__(self):
		self.sn = None
		self.config = None
		self.unit_no = None
		self.test_pass_fail_status = None
		self.special_build_description = None
		self.station_id = None
		self.start_time = None
		self.end_tiem = None
		self.version = None
		self.list_of_failing_test = None
		
		
class Data1():
	def __init__(self):
		self.station_type = str()
		self.app_version = str()


class Data3():
	def __init__(self):
		self.item = ''
		self.display_name = None
		self.pdca_priority = None
		self.upper2_limit = None
		self.lower2_limit = None
		self.upper_limit = None
		self.lower_limit = None
		self.measurement_unit = None
		self.short_key = []
		self.short = []
		self.values = []
		
def sheetnames_list():
	return 