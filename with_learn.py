class Except_():
	def __init__(self,*args,**kwargs):
		pass
	def __enter__(self):
		return self
	def other_something(self):
		pass
	def __exit__(self,exc_type,exc_value,exc_trace):
		return True