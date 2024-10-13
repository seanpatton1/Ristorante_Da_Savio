$(document).ready(function () {
    let calendarEl = document.getElementById('calendar');

    if (calendarEl) { // Ensure calendar element exists
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
                failure: function () {
                    alert('There was an error while fetching events!');
                }
            },
            select: function (info) {
                let reservationDate = info.startStr;

                if (new Date(info.startStr) < new Date()) {
                    calendar.unselect();
                    alert("Past dates cannot be selected.");
                    return;
                }

                // $('#reservation-date-input').val(reservationDate);
                console.log("Selected date: " + reservationDate);
                $('#reservationModal').modal('show');
                document.getElementById('reservation-date-display').textContent = reservationDate;
                document.getElementById('reservation-date-input').value = reservationDate;
                console.log("Selected date: " + reservationDate);


            }
        });

        calendar.render(); // Render the calendar
    } else {
        console.error("Calendar element not found.");
    }
});

// Dynamic Date Dropdown Script
// This script dynamically populates the date dropdown with the next 30 days

document.addEventListener('DOMContentLoaded', function () {
    const dateDropdown = document.getElementById('reservation-date');
    const dateInput = document.getElementById('reservation-date-input');
    const dateDisplay = document.getElementById('reservation-date-display');

    // Get today's date
    const today = new Date();

    // Populate the dropdown with the next 30 days
    for (let i = 0; i < 30; i++) {
        const option = document.createElement('option');
        const futureDate = new Date(today);
        futureDate.setDate(today.getDate() + i); // Increment the date by 'i' days

        // Format the date for form submission (YYYY-MM-DD)
        const formattedDate = futureDate.toISOString().split('T')[0];

        // Format the date for display (e.g., "October 11, 2024")
        const displayDate = futureDate.toLocaleDateString('en-US', {
            weekday: 'short',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        });

        // Add the formatted date to the dropdown
        option.value = formattedDate;
        option.textContent = displayDate;
        dateDropdown.appendChild(option);
    }

    // Handle date selection changes
    dateDropdown.addEventListener('change', function () {
        const selectedDate = this.value;

        // Log the selected date (optional, for debugging)
        console.log("Selected date from dropdown: " + selectedDate);

        // Set the selected date into the hidden input field for form submission
        dateInput.value = selectedDate;

        // Display the selected date in the modal
        dateDisplay.textContent = selectedDate;
    });

    // Trigger the modal on the "Make a Reservation" button click
    document.getElementById('book-now-btn').addEventListener('click', function () {
        const selectedDate = dateDropdown.value;

        // Set the selected date into the hidden input field and display it
        dateInput.value = selectedDate;
        dateDisplay.textContent = selectedDate;

        // Show the modal
        $('#reservationModal').modal('show');
    });
});

document.getElementById('guests').addEventListener('input', function () {
    let guestsInput = parseInt(this.value);
    if (guestsInput > 15) {
        alert('The maximum number of guests allowed is 15.');
        this.value = 15;
    }
});