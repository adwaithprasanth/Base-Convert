document.addEventListener('DOMContentLoaded', function() {
    const numberInput = document.getElementById('numberInput');
    const fromBaseSelect = document.getElementById('fromBase');
    const toBaseSelect = document.getElementById('toBase');
    const convertBtn = document.getElementById('convertBtn');
    // REMOVED: const resultOutput = document.getElementById('resultOutput');
    const container = document.querySelector('.container'); // Get the container for positioning floating results

    // Function to create and animate the floating result
    function showFloatingResult(resultText, isError = false) { // Added isError flag
        const floatingResult = document.createElement('span');
        floatingResult.classList.add('floating-result');
        if (isError) {
            floatingResult.classList.add('error'); // Add error class for different styling
            floatingResult.textContent = resultText;
            // Adjust error text shadow/color for better visibility if desired
        } else {
            floatingResult.textContent = resultText;
        }


        // Position it approximately where the convert button is clicked
        const btnRect = convertBtn.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();

        // Calculate position relative to the *container*
        // Center horizontally on the button's center
        floatingResult.style.left = `${btnRect.left + btnRect.width / 2 - containerRect.left}px`;
        // Start slightly below the button, or at the bottom of the container
        floatingResult.style.top = `${btnRect.bottom + 10 - containerRect.top}px`; // 10px below button

        // Use transform: translateX(-50%) to truly center it based on its own width
        floatingResult.style.transform = `translateX(-50%)`;

        container.appendChild(floatingResult); // Append to the container to manage positioning

        // Remove the element after the animation completes
        floatingResult.addEventListener('animationend', () => {
            floatingResult.remove();
        });
    }

    convertBtn.addEventListener('click', async function() {
        const number = numberInput.value.trim();
        const fromBase = fromBaseSelect.value;
        const toBase = toBaseSelect.value;

        // Client-side validation (improved)
        if (!number) {
            showFloatingResult("Enter a number!", true); // Pass true for error
            return;
        }

        const validationRegex = {
            '2': /^[01]+$/,
            '8': /^[0-7]+$/,
            '10': /^\d+$/,
            '16': /^[0-9A-Fa-f]+$/i
        };

        if (!validationRegex[fromBase].test(number)) {
            showFloatingResult(`Invalid input for Base ${fromBase}!`, true); // Pass true for error
            return;
        }


        try {
            const response = await fetch('/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    number: number,
                    from_base: fromBase,
                    to_base: toBase
                }),
            });

            const data = await response.json();
            // REMOVED: resultOutput.value = data.result;

            // Trigger the floating animation
            showFloatingResult(data.result);

        } catch (error) {
            console.error('Error during conversion:', error);
            showFloatingResult("Server error!", true); // Pass true for error
        }
    });

    // Optional: No need to clear resultOutput.value since it's removed.
    // numberInput.addEventListener('input', () => resultOutput.value = '');
    // fromBaseSelect.addEventListener('change', () => resultOutput.value = '');
    // toBaseSelect.addEventListener('change', () => resultOutput.value = '');
});