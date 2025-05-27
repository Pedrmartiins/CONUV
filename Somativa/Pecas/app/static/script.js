async function carregarPecas() {
  const res = await fetch('/api/pecas');
  const pecas = await res.json();

  const listaDiv = document.getElementById('listaPecas');
  listaDiv.innerHTML = '';

  pecas.forEach(peca => {
    const div = document.createElement('div');
    div.innerHTML = `
      <strong>${peca.nome}</strong> - Quantidade: ${peca.quantidade}
      <input type="number" min="1" placeholder="Adicionar" id="add-${peca.id}" />
      <button onclick="adicionarQuantidade(${peca.id})">Adicionar</button>
    `;
    listaDiv.appendChild(div);
  });
}

document.getElementById('formPeca').addEventListener('submit', async (e) => {
  e.preventDefault();
  const nome = document.getElementById('nome').value;
  const quantidade = parseInt(document.getElementById('quantidade').value);

  const res = await fetch('/api/pecas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, quantidade })
  });

  const resultado = await res.json();
  alert(resultado.mensagem || resultado.erro);
  carregarPecas();
  e.target.reset();
});

async function adicionarQuantidade(id) {
  const input = document.getElementById(`add-${id}`);
  const quantidade = parseInt(input.value);
  if (!quantidade || quantidade <= 0) return alert('Informe um valor válido');

  const res = await fetch(`/api/pecas/${id}/adicionar`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ quantidade })
  });

  const resultado = await res.json();
  alert(resultado.mensagem || resultado.erro);
  carregarPecas();
}

window.addEventListener('DOMContentLoaded', carregarPecas);
