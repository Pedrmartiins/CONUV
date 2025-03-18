document.addEventListener('DOMContentLoaded', function(){

    const form = document.getElementById('cadastroForm');

    form.addEventListener('submit', function (event){
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/cadastrar',{

            method: 'POST',
            body:JSON.stringify(Object.fromEntries(formData)),
            headers:{
                'Content-Type': 'application/json'
            }
        })
        .then(response=>response.json())
        .then(data=> {
            alert(data.message);
            if(data.message === "Cadastro realizado com sucesso!"){
                form.reset();
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });
});