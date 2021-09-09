# Face Recognition

Face recognition using python and mysql.

*******

## Useage

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

You'll obtain an account and password after installation, then you should modify the `faces.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

*******

## Run

### 1. Face Recognition

#### 1.1 Collect Face Data
```
"""
user_name = "Jack"   # the name
NUM_IMGS = 400       # the number of saved images
"""
python face_capture.py
```
The camera will be activated and the captured images will be stored in `data/Jack` folder.      
**Note:** Only one person’s images can be captured at a time.

#### 1.2 Train a Face Recognition Model
```
python train.py
```
`train.yml` and `labels.pickle` will be created at the current folder.



### 2. Database Design

#### 2.1 Define Database
**You need to** create tables in `facerecognition.sql`.      
Here is a sample code for `Student`.
```
# Create TABLE 'Customer'
CREATE TABLE `Customer` (
  `customer_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `login_time` time NOT NULL,
  `login_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1, "JACK", NOW(), '2021-09-01');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;
```

#### 2.2 Import Database
Open mysql server and import the file `facerecognition.sql`.
```
# login the mysql command
mysql -u root -p

# create database.  'mysql>' indicates we are now in the mysql command line
mysql> CREATE DATABASE facerecognition;
mysql> USE facerecognition;

# import from sql file
mysql> source facerecognition.sql
```



### 3. Login Interface

#### 3.1 OpenCV GUI
```
python faces.py
```

#### 3.2 PySimpleGUI GUI
```
python faces_gui.py
```

The camera will be activated and recognize your face using the pretrained model.    
**You need to** implement other useful functions in this part.

