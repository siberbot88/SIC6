# kita bikin database
db = client['MyDatabase']
my_collection = db['SensorData']

data_1 = {'temperature':88, 'humidity':45, 'timestamp':'12-05-2024 00:30:15'}
data_2 = {'temperature':38.6, 'humidity':77, 'timestamp':'13-05-2024 00:30:15'}
data_3= {'temperature':27.7, 'humidity':55.1, 'timestamp':'14-05-2024 00:30:15'}

result = my_collection.insert_many([data_1,data_2,data_3])
print(result.inserted_ids)

get_result = my_collection.find()
for x in get_result:
    print(x)

# my_query = {"temperature":88}
# my_collection.delete_one(my_query)

# print('Setelah di delete_________')
# get_result = my_collection.find()
# for x in get_result:
#     print(x)

