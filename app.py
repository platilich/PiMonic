from flask import Flask, render_template, request, redirect, url_for
import psutil
import requests
import getpass


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('login.html')




def get_disk_usage():
    static = []

    disk_usage = psutil.disk_usage('/')  # Получаем информацию о диске
    used_disk = disk_usage.used  # Используемый объём диска в байтах
    total_disk = disk_usage.total  # Общий объём диска в байтах
    free_disk = disk_usage.free  # Свободный объём диска в байтах


    user_disk_percent = disk_usage.percent

    # Преобразуем в гигабайты и округляем
    used_disk_gb = round(used_disk / (1024 ** 3), 2)
    free_disk_gb = round(free_disk / (1024 ** 3), 2)
    total_disk_gb = round(total_disk / (1024 ** 3), 2)


    static.append(user_disk_percent)
    static.append(used_disk_gb)
    static.append(free_disk_gb)
    static.append(total_disk_gb)

    return static


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu = sum(cpu_percent) / len(cpu_percent)



    return round(cpu)


def get_memory_usage():
    memory = psutil.virtual_memory()

    return round(memory.percent)




def get_external_ip():
    response = requests.get("https://api.ipify.org")

    return response.text



def get_network_traffic():
    static = []

    net_io = psutil.net_io_counters()

    static.append(round(net_io.bytes_sent / (1024 * 1024)))
    static.append(round(net_io.bytes_recv / (1024 * 1024)))

    return static


def connect_ssh():
    username = getpass.getuser()
    print(f"Имя пользователя (getpass): {username}")

    return f'ssh {username}@{get_external_ip()}'


@app.route('/', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        password = request.form['password']

        if password == 'Alex09':
            return redirect(url_for('dashboard'))

        else:
            return render_template('login.html')

    return render_template('login.html')




@app.route('/dashboard', methods=['GET'])
def dashboard():
    # возрат данных только по get
    return render_template(
        template_name_or_list='dashboard.html',
        disk_static=get_disk_usage(),
        cpu_static=get_cpu_usage(),
        memory_static=get_memory_usage(),
        ip_address=get_external_ip(),
        network_traffic=get_network_traffic(),
        ssh=connect_ssh()

    )



if __name__ == '__main__':
    app.run(debug=True)