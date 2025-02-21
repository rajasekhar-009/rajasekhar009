document.getElementById('startButton').addEventListener('click', function() {
    document.querySelector('.data-flow').style.display = 'block';

    // Simulating data flow (you can expand this with more logic)
    setTimeout(() => {
        alert("Data flow completed.");
        document.querySelector('.data-flow').style.display = 'none';
    }, 5000); // 5 seconds simulation
});
