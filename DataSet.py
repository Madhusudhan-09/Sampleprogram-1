import csv
class DataSet:
	def __int__(self, d, t, v):
		self.d = d
		self.t = t
		self.v = v

class Userinput:
	def __init__(self):
		self.Attr = []
		self.res = []

	def lst_add(self, d, t):
		self.Attr += [(d, t)]

	def get_dt(self):
		if self.Attr != []:
			return self.Attr.pop(0)

		return ()

	def push_res(self, tup):
		self.res += [tup]

	def get_res(self):
		return self.res

class Measure:
	def calculate(self, n, input_obj):
		res = []
		for i in range(n):
			tup = input_obj.get_dt()
			if tup == ():
				break
			else:
				d, t = tup
				input_obj.push_res([d, t, d/t])

class ShowResults:
	def __init__(self, input_obj):
		res = input_obj.get_res()
		with open('output.csv', 'a', newline='', encoding="utf-8") as opf:
			w= csv.writer(opf)
			for row in res:
				print(row)
				w.writerow(row)


if __name__ == "__main__":
	n = int(input('length of data: '))
	input_obj = Userinput()
	for i in range(n):
		print('input d and t')
		d = int(input('distance: '))
		t = int(input('time    : '))
		input_obj.lst_add(d, t)

	mes_obj = Measure()
	mes_obj.calculate(n, input_obj)

	res_obj = ShowResults(input_obj)