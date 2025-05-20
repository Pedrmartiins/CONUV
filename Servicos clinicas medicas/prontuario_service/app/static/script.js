const API_BASE_URL = 'http://localhost:5003'; // seu backend Flask está na porta 5003

const createForm = document.getElementById('createForm');
const prontuarioData = document.getElementById('prontuarioData');
const createdId = document.getElementById('createdId');

const searchForm = document.getElementById('searchForm');
const prontuarioId = document.getElementById('prontuarioId');
const prontuarioResult = document.getElementById('prontuarioResult');

const messageDiv = document.getElementById('message');

// Criar novo prontuário
createForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  messageDiv.textContent = '';
  createdId.textContent = '';
  prontuarioResult.textContent = '';

  let jsonData;
  try {
    jsonData = JSON.parse(prontuarioData.value);
  } catch {
    messageDiv.textContent = 'JSON inválido. Corrija e tente novamente.';
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/prontuario`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(jsonData)
    });

    if (!response.ok) throw new Error('Erro ao criar prontuário.');

    const data = await response.json();
    createdId.textContent = `Prontuário criado com ID: ${data.id}`;
    prontuarioData.value = '';
  } catch (error) {
    messageDiv.textContent = error.message;
  }
});

// Buscar prontuário pelo ID
searchForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  messageDiv.textContent = '';
  prontuarioResult.textContent = '';
  createdId.textContent = '';

  const id = prontuarioId.value.trim();
  if (!id) {
    messageDiv.textContent = 'Informe um ID válido.';
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/prontuario/${id}`);
    if (!response.ok) throw new Error('Prontuário não encontrado.');

    const data = await response.json();
    prontuarioResult.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    messageDiv.textContent = error.message;
  }
});
