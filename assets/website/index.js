document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#id_visit_date').onchange = () => {
        const service_id = document.querySelector('#id_service_id').value
        if (service_id) {
            const visit_date = document.querySelector('#id_visit_date').value;
            const request = new XMLHttpRequest();
            request.open('GET', `/get-available-hours/?service_id=${service_id}&date=${visit_date}`);
            request.onload = () => {
                const data = request.responseText;
                document.querySelector('#id_start_time_visit').innerHTML = data;
            }
            request.send();
            return false;
        };
    };

    document.querySelector('#id_service_id').onchange = () => {
        const visit_date = document.querySelector('#id_visit_date').value

        if (visit_date) {
        const service_id = document.querySelector('#id_service_id').value;

            const request = new XMLHttpRequest();
            request.open('GET', `/get-available-hours/?service_id=${service_id}&date=${visit_date}`);
            request.onload = () => {

                const data = request.responseText;

                document.querySelector('#id_start_time_visit').innerHTML = data;
            }

            request.send();
            return false;
        };
    };
});
