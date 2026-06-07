function updateDashboard() {
    $.ajax({
        url: '/api/dashboard',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#system').text(data.system);
            $('#memory').text(data.disk_static[1] + ' / ' + data.disk_static[3] + ' GB use');
            $('#ssh').text(data.ssh);
            $('#ram').text(data.memory_static + '%');
            $('#network').text('↓ ' + data.network_traffic[0] + ' Mb/s ↑ ' + data.network_traffic[1] + ' Mb/s');
            $('#ip').text(data.ip_address);
            $('#cpu').text(data.cpu_static + '% cores');
            $('#uptime').text(data.uptime + ' days');
        }
    });
}

// Обновляем данные при загрузке страницы
updateDashboard();

// Обновляем каждые 10 секунд
setInterval(updateDashboard, 10000);