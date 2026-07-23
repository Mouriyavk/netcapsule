from flowbuilder import update_flowTable
from resolver import resolve 
from parse import PacketInfo


flowTable = {}
for items in PacketInfo():
	update_flowTable(items)



for flow in flowTable.values():
	val = resolve(flow)
	print(val)