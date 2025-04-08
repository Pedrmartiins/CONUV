const ctx = document.getElementById('sensorChart').getContext('2d');

const chart = new Chart(ctx,{
    type: 'line',
    data: {
        labels:[],
        datasets: [
            {label: 'Temperatura(°C)', data: [], borderColor: 'red', fill: false},
            {label: 'Umidade (%)', data: [], borderColor: 'blue', fill: 'false'},
            {label: 'Pressao (hPa)', data: [], borderColor: 'green', fill: 'false'}
        ]
    },
    options: {
        responsive: true,
        scales:{
            x: {title: {display: true, text: 'Tempo'}}
        }
    }
});

async function atualizarSensores(){
    try{
        const response = await fetch('http://127.0.0.1:5000/sensores');

        const data = await response.json();

        document.getElementById('temp').innerText = data.temperatura;
        document.getElementById('hum').innerText = data.umidade;
        document.getElementById('pres').innerText = data.pressao;

        const now = new Date().toLocaleDateTimeString();

        chart.data.labels.push(now);
        chart.data.datasets[0].data.push(data.temperatura);
        chart.data.datasets[1].data.push(data.umidade);
        chart.data.datasets[2].data.push(data.pressao);

        if(chart.data.labels.length > 10){
            chart.data.labels.shift();
            chart.data.datasets.forEach(dataset => dataset.data.shift());
            }
            chart.update();
        
        }catch(error){
            console.error('erro ao buscar dados: ', error);
        }   
}

setInterval(atualizarSensores, 2000);