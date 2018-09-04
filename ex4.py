cars=100#定义cars变量并赋值
space_in_a_car=4.0#定义space_in_a_car变量并赋值
drivers=30#定义drivers变量并赋值
passengers=90#定义pssengers变量并赋值
cars_not_driven=cars-drivers#将cars-drivers运算结果传递给cars_not_drivern变量
cars_driven=drivers#将drivers的值传递给cars_driven
carpool_capacity=cars_driven*space_in_a_car#同第五行注释
average_passengers_per_car=passengers/cars_driven#同上
#打印各个变量的值
print("There are",cars,"cars available.")
print("There are only", drivers,"drivers available")
print("There will be", cars_not_driven,"empty cars today.")
print("we can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")