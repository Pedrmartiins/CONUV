document.getElementById('formAeronave').addEventListener('submit', function(e) {
  e.preventDefault();

  const modelo = document.getElementById('modelo').value;
  const fabricante = document.getElementById('fabricante').value;
  const horas_voo = document.getElementById('horas_voo').value;

  fetch('/aeronaves', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ modelo, fabricante, horas_voo })
  })
  .then(response => response.json())
  .then(data => {
      if (data.erro) {
          document.getElementById('mensagem').className = 'erro';
          document.getElementById('mensagem').innerText = data.erro;
      } else {
          document.getElementById('mensagem').className = 'mensagem';
          document.getElementById('mensagem').innerText = 'Aeronave cadastrada com sucesso!';
          document.getElementById('formAeronave').reset();
          carregarAeronaves();
      }
  })
  .catch(error => {
      console.error('Erro ao cadastrar aeronave:', error);
      document.getElementById('mensagem').className = 'erro';
      document.getElementById('mensagem').innerText = 'Erro ao cadastrar aeronave.';
  });
});

function carregarAeronaves() {
  fetch('/aeronaves')
      .then(response => response.json())
      .then(aeronaves => {
          const lista = document.getElementById('listaAeronaves');
          lista.innerHTML = '';
          aeronaves.forEach(a => {
              const item = document.createElement('li');
              item.innerText = `ID ${a.id}: ${a.modelo} (${a.fabricante}) - ${a.horas_voo} horas`;
              lista.appendChild(item);
          });
      })
      .catch(error => {
          console.error('Erro ao carregar aeronaves:', error);
          document.getElementById('mensagem').className = 'erro';
          document.getElementById('mensagem').innerText = 'Erro ao carregar aeronaves.';
      });
}

// Carrega a lista ao iniciar
carregarAeronaves();