$(document).ready(function() {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        selectable: true,
        selectHelper: true,
        // Disable past dates using validRange
        validRange: {
            start: moment().format('YYYY-MM-DD')  // Ensures past dates are disabled
        },
        // Fetch events from the server to display reserved slots
        events: function(start, end, timezone, callback) {
            $.ajax({
                url: '/booking/get-bookings/',  // URL of the Django view that returns JSON data with reservations
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
            console.log('Selected date: ' + start.format('YYYY-MM-DD'));  // Debugging line
            
            // Prevent selecting past dates as an extra precaution
            if (start.isBefore(moment(), 'day')) {
                console.log('Past date selected, not allowed.');  // Debugging line
                $('#calendar').fullCalendar('unselect');
                alert("Past dates cannot be selected.");
                return false;
            }

            let reservationDate = start.format('YYYY-MM-DD');
            $('#reservation-date').val(reservationDate); 
            $('#reservationModal').modal('show');
        },
        
        minDate: moment().format('YYYY-MM-DD')
    });
});