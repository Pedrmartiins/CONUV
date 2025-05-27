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
    body: JSON.stringify({ aeronave_id, peca_id, motivo, tipo })
  });

  const result = await response.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 4);
});

async function listarFaturas() {
  const res = await fetch('http://localhost:5001/manutencao');
  const result = await res.json();
  document.getElementById('resultado').innerText = JSON.stringify(result, null, 2);
}




async function carregarOpcoes() {
  const [aeronaveRes, pecaRes] = await Promise.all([
    fetch('/aeronaves'),
    fetch('/pecas')
  ]);

  const aeronaves = await aeronaveRes.json();
  const pecas = await pecaRes.json();

  const aeronaveSelect = document.getElementById('aeronave_id');
  const pecaSelect = document.getElementById('peca_id');

  aeronaves.forEach(a => {
    const option = document.createElement('option');
    option.value = a.id;
    option.textContent = a.nome;
    aeronaveSelect.appendChild(option);
  });

  pecas.forEach(p => {
    const option = document.createElement('option');
    option.value = p.id;
    option.textContent = p.nome;
    pecaSelect.appendChild(option);
  });
}
// Chama quando a página carrega
window.addEventListener('DOMContentLoaded', carregarOpcoes);
