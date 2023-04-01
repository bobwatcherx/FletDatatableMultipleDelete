from flet import *

def main(page:Page):

	# CHANGE THEME
	page.theme_mode = "light"

	# CREATE DATA OF YOU table
	mydata = [
	{"name":"jon","age":12,"selected":False},
	{"name":"daa","age":22,"selected":False},
	{"name":"boo","age":32,"selected":False},
	{"name":"jun","age":44,"selected":False},
	]

	you_selected = Column()


	# FUNCTION FOR SELECT ALL OF yoU SELECTED
	def selectedall(e):
		# AND NOW SELECT ALL CHECKBOX IF yoU SELECT ALL
		# AND REMOVE 
		# AND NOW CHECK STATUS TRUE OR FAlSE IN CHECKBOX
		# IF TRUE AND PUSH all mydata to you_selected FOR remove
		# AND NOW CHECK CHECKBOX IF TRUE
		if e.control.value == True:
			for x in mydata:
				# SET ALL TO TRUE CHECBOX
				x['selected'] = True
				# AND REFRESH TABLE
				mytable.rows.clear()
				load_table()
				# AND ADD TO you_selected FOR REMOVE
				you_selected.controls.append(
					Row([
						Text(x['name'],size=25),
						Text(x['age'],size=25),
						])

					)
		# AND NOW IF CHECKBOX STATUS IS fALSE THE REMOVE ALL
		# FROM you_selected FOr remove

		if e.control.value == False:
			for x in mydata:
				# SET ALL TO TRUE CHECBOX
				x['selected'] = False
				# AND REFRESH TABLE
				mytable.rows.clear()
				load_table()
				# AND REMOVE ALL FROM you_selected
				for c in you_selected.controls:
					if isinstance(c,Row) and c.controls[0].value == x['name'] and c.controls[1].value == x['age']:
							you_selected.controls.remove(c)
							# AND CLOSE FROM loop if name and age found and remove
							break
		page.update()


	# NOW CREATE DATATABLE
	mytable = DataTable(
		# AND ENABLE CHECKBOX FOR SELECT multiple
		show_checkbox_column=False,
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("age")),
			DataColumn(
				Column([
					Text("actions"),
					# AND CREATE CHECKBOX FOR SELECT ALL
					Checkbox(value=False,
						on_change=selectedall
						)
					])
				),
			],
		rows=[]

		)

	def this_seledted(e):
		# AND NOW PUSH DATA TO you_selected FROM TABLE IF YOU SELECT
		# AND GET NAME AND AGE FROM YOU CLICK CHECKBOX
		select_name = Text(e.control.data.controls[0].value,size=20)
		select_age = Text(e.control.data.controls[1].value,size=20)

		# IF VALUE IF CHECKBOX IS TRUE THEN APPEND DATA TO 
		# you_selected
		if e.control.value == True:
			you_selected.controls.append(Row([select_name,select_age]))
		# AND IF YOU UNCHECK CHECKBOX AGAIN THE REMOVE YOU SELECTED
		# FROM you_selected	
		else:
			for c in you_selected.controls:
				if isinstance(c,Row):
					if c.controls[0].value == select_name.value and c.controls[1].value == select_age.value:
						you_selected.controls.remove(c)
						# AND CLOSE FROM loop if name and age found and remove
						break

		page.update()


	def removemultiple(e):
		# AND NOW FETCH ALL DATA FROM you_selected
		# LIKE NAME AND AGE
		for x in you_selected.controls:
			delete_name = x.controls[0].value
			delete_age = x.controls[1].value
			# AND NOW DELETE multiple FROM YOU SLECT CHECKBOX
			for i in range(len(mydata)):
				# AND IF data in mydata equal in you you_selected
				# THEN REMOVE multiple
				if mydata[i]['name'] == delete_name and mydata[i]['age'] == delete_age:
					# AND DELETE multiple
					del mydata[i]
					# AND break
					break
			# AND NOW DataTable WILL CLEAR ALL DATA THEN LOAD AGAIN
			# FROM mydata
			mytable.rows.clear()
			load_table()
			# AND SHOW SNACK BAR IF YOU SUCCESS DELETE 
			page.snack_bar = SnackBar(
				Text("You Success delete guys",size=30),
				bgcolor="red"
				)
			page.snack_bar.open = True
			page.update()
		# AND NOW CLEAR you_selected 
		you_selected.controls.clear()
		page.update()



	# NOW PUSH mydata to DATATABLE 
	def load_table():
		for x in mydata:
			mytable.rows.append(
				DataRow(
					# ENABLE SELECTED IN FIELD tables
					selected=True,
					cells=[
						DataCell(Text(x['name'])),
						DataCell(Text(x['age'])),
						# AND NOW CREATE TOGGLE CHECKBOX
						DataCell(
							Checkbox(
								value=x['selected'],
								# AND CHANGE COLOR TO RED
								fill_color="red",
								data=Row([
									Text(x['name']),
									Text(x['age']),

									]),
								# AND IF CHANGE TRUE OR False
								# THE RUN FUNCTION
								on_change=this_seledted

								)

							)
						]
					)

				)
	# AND RUN FUNCTION LOAD table
	load_table()


	page.add(
	Column([
		Text("Delete multiple table",size=30,
			weight="bold"),
		mytable,
		FilledButton("delete now",
			# NOW REMOVE multiple
			on_click=removemultiple
			),
		Text("You selected",weight="bold",size=25),
		you_selected


		])
		)
flet.app(target=main)
