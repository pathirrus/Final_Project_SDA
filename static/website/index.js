// AJAX
// Ogólnie pomysł polega na tym, że:
// domyślnie pole z godziną wizyty jest puste (nie ma nic do wyboru).
// Następnie, kiedy użytkownik wprowadzi informacje o rodzaju usługi i dniu wizyty
// (w dowolnej kolejności) to wysyłamy zapytanie asynchroniczne (czyli zapytanie ajax)
// na serwer z pytaniem o dostępne godziny dla takiej usługi w takim dniu.
// To, że użytkownik wprowadził potrzebne informacje poznajemy w ten sposób:
// na sygnał zmiany wartości (zdarzenie onchange) w polu service_id lub visit_date
// sprawdzamy wartość w drugim polu. Jeżeli drugie pole nie jest puste to znaczy,
// że mamy już obie wartości i możemy wysyłać zapytanie o dostępne godziny.
// Wysyłamy zapytanie, odbieramy odpowiedź i odpowiedź wkładamy do elementu select.
// No i teraz pole z dostępnymi godzinami nie jest już puste.

// Kiedy dokument załadowany to
document.addEventListener('DOMContentLoaded', () => {
    // I tutaj dwa przypadki do obsłużenia. Bo możemy powiedzieć, które terminy są
    // dostępne kiedy mamy już wskazany rodzaj usługi i dzień wizyty. Czyli pierwszy
    // przypadek to mamy już wskazany rodzaj usługi i użytkownik wprowadza dzień wizyty
    // (przypadek 1). Drugi przypadek to mamy już wprowadzony dzień wizyty i użytkownik
    // wybiera rodzaj usługi.

    // Przypadek 1. Jeżeli zmieniona zostanie wartość w elemencie o id=id_visit_date
    // (czyli pole do wpisania terminu wizyty) to:
    document.querySelector('#id_visit_date').onchange = () => {
        // Do zmiennej service_id przypisujemy wartość w polu o id=id_service_id (czyli pole z typem usługi)
        const service_id = document.querySelector('#id_service_id').value

         // Sprawdzamy, czy jest już wprowadzony rodzaj usuługi. Jeżeli nie to nic jeszcze
         // nie możemy powiedzić. Ale Jeżeli zmienna service_id nie jest pusta
         // (czyli wartość w polu z typem usługi nie jest pusta) to:
        if (service_id) {
            // Przypisujemy do zmiennej visit_date wartość w polu o id=id_visit_date
            const visit_date = document.querySelector('#id_visit_date').value;

            // Inicjalizujemy nowe zapytanie ASYNCHRONICZNE (czyli to zapytanie uderzy
            // na serwer i wróci do klienta bez odświeżania całej strony). Na backendzie
            // zrobione jest tak, żeby wracało do klienta z kodem html gotowym do włożenia
            // do elementu select
            const request = new XMLHttpRequest();

            // zapytanie asynchroniczne będzie uderzało metodą get na url w którym
            // parametrami get - (service_id i date) przekazujemy wartości znajdujące
            // się w polach o id=id_visit_date i id=id_service_id formularza. Na backendzie
            // przygotowaliśmy już odpowiedni endpoint - get-available-hours do obsłużenia
            // tego zapytania.
            request.open('GET', `/get-available-hours/?service_id=${service_id}&date=${visit_date}`);

            // A to już obsługa po powrocie. Czyli kiedy otrzymamy odpowiedź od serwera to:
            request.onload = () => {

                // Przypisujemy zawartość tej odpowiedzi do zmiennej data
                const data = request.responseText;

                // A następnie zmienną data nadpisujemy zawartość pola o
                // id=id_start_time_visit (czyli pola z wyborem konkreten godziny)
                document.querySelector('#id_start_time_visit').innerHTML = data;
            }

            // Wysyłamy request
            request.send();
            return false;
        };
    };

    // Przypadek 2. Jeżeli zmieniona zostanie wartość w elemencie o id=id_service_id
    // (czyli pole do wpisania rodzaju usługi) rób:
    document.querySelector('#id_service_id').onchange = () => {
        // analogicznie jak do przypadku 1
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