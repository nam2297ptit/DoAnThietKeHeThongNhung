## **Guide**

---
### __Requirements__
- Python3+
- Django ~= 2.1.5
- SQLite – included with Django, no need to install
- Python pip – for installing packages
- Git: Can be installed by command: ```sudo apt-get install git```

---

### __Usage__

* **Step 1: Download the project directory from Github**
```
$ git clone https://github.com/nam2297ptit/DoAnThietKeHeThongNhung.git
```

* **Step 2: Create Virtual environment**

```
$ python3 -m venv django
$ source django/bin/activate
```

* **Step 3: Installing Django**
```
(django)$ python -m pip install --upgrade pip
(django)$ pip install -r requirements.txt
```
* **Step 4: Set up a database & Django admin**
```
(django)$ python manage.py migrate
(django)$ python manage.py createsuperuser
```
* **Step 5: Run Server**
```
(django)$ python manage.py runserver
```
* **Step 6: Insert values to the database**

##### **Publish sensor values :**

* **Method 1: Code Python**

Run the following file in the DHT11 folder: 
```
$ python3 Publish.py
```

* **Method 2:Code arduino with DHT11 sensor**

Run the file ```sensor.ino``` with **Arduino IDE software**

**Get data sensor to database:**

Run the following file in the DHT11 folder:
```
$ python3 Subscribe.py
```

---
### **Result**

* Signin page:

![SignIn](https://i.imgur.com/R7PpJB2.png)

* Sensor page:

![Sensor1](https://i.imgur.com/xaq80vU.png)

![Sensor2](https://i.imgur.com/SvrGpRW.png)


