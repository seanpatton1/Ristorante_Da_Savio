$(document).ready(function() {
    let calendarEl = document.getElementById('calendar');
    
    if (calendarEl) {  // Ensure calendar element exists
        let calendar = new FullCalendar.Calendar(calendarEl, {
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            initialView: 'dayGridMonth',
            selectable: true,
            validRange: {
                start: new Date().toISOString().split('T')[0]
            },
            events: {
                url: '/booking/get-bookings/',
                method: 'GET',
                extraParams: {},
                failure: function() {
                    alert('There was an error while fetching events!');
                }
            },
            select: function(info) {
                let reservationDate = info.startStr;

                if (new Date(info.startStr) < new Date()) {
                    calendar.unselect();
                    alert("Past dates cannot be selected.");
                    return;
                }

                $('#reservation-date').val(reservationDate);
                $('#reservationModal').modal('show');
            }
        });

        calendar.render();  // Render the calendar
    } else {
        console.error("Calendar element not found.");
    }
});
