from flask import Flask, render_template, redirect, url_for, jsonify

from utils import *
from config import key




app = Flask(__name__)


app.secret_key = key



@app.route('/')
def index():
    return redirect(url_for('dashboard'))




@app.route('/dashboard', methods=['GET'])
def dashboard():
    try:
        return render_template(
            template_name_or_list='dashboard.html',
            system=get_name_os(),
            disk_static=get_disk_usage(),
            cpu_static=get_cpu_usage(),
            memory_static=get_memory_usage(),
            ip_address=get_external_ip(),
            network_traffic=get_network_traffic(),
            ssh=connect_ssh(),
            uptime=get_uptime()
        )
    except Exception as e:
        print(f"Ошибка в dashboard: {e}")
        return f"Ошибка: {str(e)}", 500




@app.route('/api/dashboard', methods=['GET'])
def api_dashboard():
    """API endpoint для динамического обновления"""
    try:
        return jsonify({
            'system': get_name_os(),
            'disk_static': get_disk_usage(),
            'cpu_static': get_cpu_usage(),
            'memory_static': get_memory_usage(),
            'ip_address': get_external_ip(),
            'network_traffic': get_network_traffic(),
            'ssh': connect_ssh(),
            'uptime': get_uptime()
        })


    except Exception as e:
        print(f"Ошибка в API: {e}")
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0')