const form = document.getElementById('consultaForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const id_paciente = document.getElementById('id_paciente').value;
  const data = document.getElementById('data').value;

  const response = await fetch('http://localhost:5002/consulta', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ id_paciente, data })
  });

  const result = await response.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
});

async function listarConsultas() {
  const res = await fetch('http://localhost:5002/consulta');
  const result = await res.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
}
