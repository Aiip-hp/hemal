'''Problem 1:Generate a dummy dataset
ACCEPTANCE CRITERIA
1.The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region.
2.Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats. 
3.The 16 floats returned will be between 0 and 1 ''' 
    
sensor_cluster_id = list(range(1, 33))          #sensor clusters of 32

print("List of Sensor Cluster id= ",sensor_cluster_id) 

# Import random module to use the random method => generates numbers between 0 and 1
import random as rand

# Create a list to hold all the generated sensor data
sensorData = []

#Generate a list of 512 random numbers using a for loop (32sensor cluster*16sensors)
#Assumptions 1-512 sensor readings are arranged based on the 32 clusters sequentially. 
for s in range((32*16)+1):
    # variable to hold each number generated
    sensorDataNumber = rand.random() 
    # Append that number to the sensorData list
    sensorData.append(sensorDataNumber)

print ("\nNumber of Sensors(16nos. for 32 clusters)= ",s) #Total No. of Sensors=512
print("\nSensor Data (sensor values 1-512 respectively)=  ",sensorData) #View of the 512 sensor instaneous float data reading on the console that is appended to the data file in line 39

'''Problem 2:Storage of data
ACCEPTANCE CRITERIA
1.Every time your data set is generated the output should be stored and saved
2.Write the data to a file
3.New data should not overwrite historical data
4.Date and time stamp for each interval of data collection'''

with open("Sensor_data.txt", "a") as f:
    from datetime import datetime
    now = datetime.now()
    print("\nDate & Time =", now,file=f)#Time stamp for the sensor readings
    print('\n',sensorData, file=f) #Record Sensor data float reading for 512 sensors


'''Problem 3:Write a function that will test the incoming data for possible strings entries
ACCEPTANCE CRITERIA
1.Create a copy of a "corrupted" data set containing at least one entry where the value is "err"
2.Your function should check for this error
3.Convert the string to a numerical value that can be uniquely identified as the error
4.Create an error log that records that the error happened and which of the sensors the error occurred with
5.For a challenge you can try to date and time stamp the log entries'''


#def test():
#   with open("Sensor_data_analysis.txt", "a") as data:
 #       A = copy."Sensor_data.txt"("Sensor_data_analysis.txt")
  #      print(data)
   # return;
def data_analysis():
    filename="Sensor_data.txt"
    with open(filename) as file_object:
        lines=file_object.readlines()
        print('\n',lines[3])#'First Instantenous data set to be analysed for errors 
        #if lines[3]==type(float):
        #    print('No error')
        #else:
        #    print('Error')
data_analysis()        

#Copy data set for analysis on to another txt file
with open("Sensor_data_Analysis.txt", "a") as g: 
    print(data_analysis(), file=g)
