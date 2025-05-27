const form = document.getElementById('manutencaoForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const aeronave_id = document.getElementById('aeronave_id').value;
  const peca = document.getElementById('peca_id').value;
  const motivo = document.getElementById('motivo').value;
  const tipo = document.getElementById('tipo_manutencao').value;

  const response = await fetch('/manutencao', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ aeronave_id, peca, motivo, tipo })
  });

  const result = await response.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 4);
});

async function listarFaturas() {
  const res = await fetch('http://localhost:5001/manutencao');
  const result = await res.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
}
