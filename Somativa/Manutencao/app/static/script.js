const form = document.getElementById('faturaForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const consulta_id = document.getElementById('consulta_id').value;
  const valor = document.getElementById('valor').value;

  const response = await fetch('http://localhost:5004/fatura', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ consulta_id, valor })
  });

  const result = await response.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
});

async function listarFaturas() {
  const res = await fetch('http://localhost:5004/fatura');
  const result = await res.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
}
