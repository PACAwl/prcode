import qrcode

data = input("请输入一个任意的数据：")
img=qrcode.make(data)
img.save("qrcode.jpg")
img.show()

input("\n\n按回车键退出！")