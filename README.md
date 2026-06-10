# 🍓 PiMonic
Web-based resource monitoring for Raspberry Pi (and other servers)


## Functions

* **Resource Monitoring:**
* **CPU:** Average processor load percentage.
* **RAM:** Percentage of memory usage.
* **Disk:** Total, used, and free space (in GB), plus usage percentage.
* **Network:** Real-time incoming and outgoing traffic in MB.
* **Network Info:** Displays the server's external IP address.
* **Auto-refresh:** The dashboard automatically updates every 10 seconds.




## How to Run

### Installing Python and a virtual environment


```bash
sudo apt install python3

```

```bash
python3 -m venv venv
source venv/bin/activate

```

### Install Dependencies

Install the required Python libraries using pip:

```bash
pip install requirements.txt

```

### Generate a secret key:

```bash
openssl rand -hex 32
```


### Specify it in the key variable in config.py


### Run the code

```bash
python app.py
```



### Open your browser and navigate to: `http://your_external_ip:5500`


### Ready


---
JL с нами малина становится вкуснее
