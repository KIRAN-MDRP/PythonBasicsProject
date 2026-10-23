class Variables:
	staticVariable1 = "Static Variable One"
	_var1 = "Var 1"
	_var2 = "Var 2"
	def __init__(self, var1,var2):
		self._var1 = var1
		self._var2 = var2
		print("Variable values at constructor:", self._var1, self._var2)
	def methodOne(self):
		methodOneLocalV = "MethodOne Local Variable"
		print(methodOneLocalV)

var = Variables("Variable1","Varible2")
print(var.methodOneLocalV)
