#with open("apache_acess.bib", "r") as file:
#   for line in file:
#       elements = line.split(" ")
#       transaction = {
#           'ip' : elements[0],
#           'timestamp' : "".join([elements[3].strip("[]"),elements[4].strip("[]")]),
#           'kind_of_petition' : elements[5],
#          'route' : elements[6],
#          'version' : elements[7].strip('"'),
#          'status' : elements[8],
#           'completed_time' : elements[9].strip('/n')
#     }
        

with open("number.txt","a") as file:
    for number in range(16,21):
        file.write(str(number) + "\n")