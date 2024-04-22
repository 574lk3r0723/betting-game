document.getElementById('betForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const userId = document.getElementById('userId').value;
    const numbers = document.getElementById('numbers').value.split(',').map(num => parseInt(num.trim(), 10));
  
    fetch('/games', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_id: userId, numbers: numbers })
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to place bet');
      }
    })
    .then(data => {
      document.getElementById('result').innerHTML = `<p>Game created successfully. Game ID: ${data.game_id}</p>`;
    })
    .catch(error => {
      document.getElementById('result').innerHTML = `<p id="error">${error.message}</p>`;
    });
  });
  