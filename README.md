## Step 1
Download and extract the Carla server.

https://github.com/carla-simulator/carla/releases

## Step 2

Make a backup of the following files inside the directroy 

```
...CARLA_0.9.13/WindowsNoEditor/PythonAPI/carla/agents/navigation
behavior_agent
behavior_types.py
```
Place the files from the modified_carla_files folder inside the same directory.


## Step 3

Copy the repository folder inside the 
```
...CARLA_0.9.13/WindowsNoEditor/PythonAPI
```

## Step 4

Start the Carla Server

```
...CARLA_0.9.13/CarlaUE4.exe
```
## Step 5
Start the client, but before you start modify the rabbitmq_host argument with the ip address of the Teaching Platform deployed system

```
cd ...CARLA_0.9.13/WindowsNoEditor/PythonAPI/teaching_carla_client

automatic_control.py --filter vehicle.tesla.* --rabbitmq_host 172.17.176.221
```
