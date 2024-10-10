// Initialize FullCalendar when the document is readypython3 manage.py runserver

$(document).ready(function() {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        selectable: true,
        selectHelper: true,
        // Fetch events from the server to display reserved slots
        events: function(start, end, timezone, callback) {
            $.ajax({
                url: '/booking/get-bookings/', // URL of the Django view that returns JSON data with reservations
                dataType: 'json',
                success: function(data) {
                    let events = [];
                    $(data).each(function() {
                        events.push({
                            title: 'Reserved',
                            start: this.start,
                            end: this.end
                        });
                    });
                    callback(events);
                }
            });
        },
        // Handle date selection for a new booking
        select: function(start, end) {
            let reservationDate = start.format('YYYY-MM-DD');
            $('#reservation-date').val(reservationDate); 
            $('#reservationModal').modal('show');
        }
    });
});