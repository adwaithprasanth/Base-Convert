// Simple script to handle form submission and validation
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        const numberInput = form.querySelector('input[name="number"]');
        const fromBaseInput = form.querySelector('input[name="from_base"]');
        const toBaseInput = form.querySelector('input[name="to_base"]');

        // Basic validation
        if (!numberInput.value || !fromBaseInput.value || !toBaseInput.value) {
            alert('Please fill out all fields.');
            event.preventDefault(); // Prevent form submission
        }
    });
});
