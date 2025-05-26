const form = document.getElementById('pacienteForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const nome = document.getElementById('nome').value;
  const cpf = document.getElementById('cpf').value;

  const response = await fetch('http://localhost:5001/paciente', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ nome, cpf })
  });

  const result = await response.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
});

async function buscarPaciente() {
  const cpf = document.getElementById('cpfBusca').value;
  const res = await fetch(`http://localhost:5001/paciente/${cpf}`);
  const result = await res.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
}
