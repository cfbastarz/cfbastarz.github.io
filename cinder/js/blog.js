// Bootstrap 3 closes dropdowns on document clicks; keep date groups open.
document.querySelectorAll('.archive-group summary').forEach(function (summary) {
    summary.addEventListener('click', function (event) {
        event.stopPropagation();
    });
});
