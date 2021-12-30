from coord import *
def menu(title,*options):
	titleLength = len(title)
	print(f"\n {title.upper().rjust(round(titleLength*1.5),'=').ljust(titleLength*2,'=')} ")
	for option in range(len(options)):
		opt = f"{f'{option+1}'.rjust(round(titleLength/2.5))}. {options[option]}"
		print(f"|{opt.ljust(titleLength*2)}|")
	print(f' {"-"*(titleLength*2)} ')

main = lambda: menu('chương trình tính tọa độ của vector',
	'Tính tọa độ vector',
	'Phép tính với tọa độ vector',
	'Tính tích vô hướng của vector',
	'Tính độ dài của vector',
	'Thoát chương trình')
def changeTuple(func,pars):
	pars = pars.replace(';',',')
	return eval(f'{func}({pars})')
main() # Hiện lại menu chính
def option2(choice,point):
	opt2 = ['coord.add','coord.subtract','coord.multi','coord.average','coord.average']
	return changeTuple(opt2[choice],point)
def option4(choice,point):
	opt4 = ['coord.co_exp','coord.mid_angle']
	return changeTuple(opt4[choice,point])
option = int(input("---> Nhập lựa chọn mà bạn muốn: "))
while True:
	if option == 1:
		point = input("Nhập tọa độ của vector: ")
		print(f"Tọa độ là: {changeTuple('coord.create',point)}")
	elif option == 2:
		menu('phép tính với tọa độ vector',
			'Cộng tọa độ của các vector',
			'Trừ tọa độ của các vector',
			'Nhân tọa độ của các vector',
			'Tính tọa độ trung điểm của vector',
			'Tính tọa độ của trọng tâm trong tam giác')
		choice = int(input("---> Nhập lựa chọn mà bạn muốn: ")) - 1
		point = eval(input("Nhập tọa độ các của vector: "))
		print(f'Kết quả là: {option2(choice,point)}')
		main() # Hiện lại menu chính
		option = int(input("---> Nhập lựa chọn mà bạn muốn: "))
	elif option == 3:
		menu('tích vô hướng của vector',
			'Biểu thức tọa độ của vector',
			'Tính góc giữa của 2 vector')
		choice = int(input("---> Nhập lựa chọn mà bạn muốn: ")) - 1
		point = input("Nhập tọa độ các của vector: ")
		print(f'Kết quả là: {option4(choice,point)}')
		main() # Hiện lại menu chính
		option = int(input("---> Nhập lựa chọn mà bạn muốn: "))
		point = input("Nhập tọa độ của các vector: ")
	elif option == 4:
		point = input("Nhập tọa độ của vector: ")
		print(f"Tọa độ là: {changeTuple('coord.size',point)}")		
	elif option == 5: break
	else:
		print(f"Lựa chọn có tên {option} ko tồn tại, vui lòng chọn lại.")
		option = int(input("-> Nhập lựa chọn mà bạn muốn: "))